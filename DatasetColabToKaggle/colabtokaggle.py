import os
import shutil
from pathlib import Path
import subprocess
import zipfile
import json
import argparse
class UpKaggle(object):
  def __init__(self, pathEnv) -> None:
    self.env = pathEnv
    with open(f"{self.env}/kaggle.json", "r") as file:
      self.dtAPI = json.load(file)
    self.setEnv(pathEnv)

  def setEnv(self, pathEnv):
    subprocess.run("pip install --upgrade --force-reinstall --no-deps kaggle", shell=True)
    os.environ['KAGGLE_CONFIG_DIR'] = self.env

  def checkSize(self, path) -> bool:
    sz = os.path.getsize(path) / (1024**3)
    print(f"size file {path.stem}.zip:", round(sz, 4))
    return  sz < 20

  def splitZipFolder(self):
    size = shutil.disk_usage(self.pathData).used / (1024**3)
    self.nfolder = int(size // 15 + 1)
    pathfile = [f"{self.pathData}/{file}" for file in os.listdir(self.pathData)]
    self.nfile = len(pathfile)
    self.fpf = int(self.nfile // self.nfolder)
    self.pwd = Path.cwd()/"PushKaggle"

    if os.path.exists(self.pwd):shutil.rmtree(self.pwd)
    if not os.path.exists(self.pwd):
      os.makedirs(self.pwd)
    for i in range(self.nfolder):
      pt = self.pwd/f"{self.namefile}-{str(i).zfill(3)}"
      if not os.path.exists(pt):
        os.makedirs(pt)
      self.zipFolder(pathfile[(i * self.fpf) : ((i + 1) * self.fpf)], pt/f"{self.namefile}-{str(i).zfill(3)}.zip")
      self.createMetaData(pt)
      if not self.checkSize(pt/f"{self.namefile}-{str(i).zfill(3)}.zip"):
        raise "Size Exceeds the size limit of the zip file."

  def zipFolder(self, urls, pathsave):
    with zipfile.ZipFile(pathsave,"w",zipfile.ZIP_DEFLATED) as zipf:
      for file in urls:
        zipf.write(file)

  def createMetaData(self, pathsave):
    dictionary = {
      "title": f"{pathsave.stem}",
      "id": f"{self.dtAPI['username']}/{pathsave.stem}",
      "licenses": [
        {
          "name": "CC0-1.0"
        }
      ]
    }
    with open(f"{pathsave}/dataset-metadata.json", "w") as file:
      json.dump(dictionary, file)

  def push(self):
    for i in range(self.nfolder):
      pt = self.pwd/f"{self.namefile}-{str(i).zfill(3)}"
      result = subprocess.run(f"kaggle datasets create -p {pt} --dir-mode skip", shell=True, capture_output=True, text=True)
      print("_________________________________________________________________________")
      print(f"Path data: {self.namefile}-{str(i).zfill(3)}{self.pathData}")
      print(result.stdout)

    print("successfull!!!!!!!!!!!!!!!!!")

  def run(self, pathData, namefile):
    self.pathData = pathData
    self.namefile = namefile
    self.splitZipFolder()
    self.push()

if __name__ == "__main__":
  parse = argparse.ArgumentParser(description="Cmd Python")
  parse.add_argument("-env", required=True)
  parse.add_argument("-data", required=True)
  parse.add_argument("-name", required=True)
  args = parse.parse_args()
  upkaggle = UpKaggle(args.env)
  upkaggle.run(args.data, args.name)
