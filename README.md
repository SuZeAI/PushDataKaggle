# PushDataKaggle
Push data in drive to kaggle use Colab

    !python colabtokaggle.py -env .... -data .... - name
    
# Result:

Version old: dataset private

    size file test-000.zip: 3.6987
    _________________________________________________________________________
    Path data: test-000/content/drive/MyDrive/Datasetnew100/Malware
    Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /content/Env/kaggle.json'
    Starting upload for file test-000.zip
    Upload successful: test-000.zip (4GB)
    Your private Dataset is being created. Please check progress at https://www.kaggle.com/datasets/cuonon/test-000

    successfull!!!!!!!!!!!!!!!!!

    -> Path data: test-000/content/drive/MyDrive/Datasetnew100/Malware
    -> Link private: https://www.kaggle.com/datasets/cuonon/test-000
    
Version new: dataset public

    Zipping.......
    size file Mal-new-000.zip: 0.0061
    Zip successfull!!!!!!!!!!!!!!!!!
    Pushing.......
    _________________________________________________________________________
    Path data: Mal-new-000/content/drive/MyDrive/Datasetnew100/Malware
    Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /content/Env/kaggle.json'
    Starting upload for file Mal-new-000.zip
    Upload successful: Mal-new-000.zip (6MB)
    Your public Dataset is being created. Please check progress at https://www.kaggle.com/datasets/cuonon/Mal-new-000

    All successfull!!!!!!!!!!!!!!!!!
    -> Path: Mal-new-000/content/drive/MyDrive/Datasetnew100/Malware
    -> Link Public: https://www.kaggle.com/datasets/cuonon/Mal-new-000