import wget
import os
import zipfile
from tqdm import tqdm


def downloadAndUnzip(url, zipFile, folder):
    if not os.path.isfile(zipFile):
        wget.download(url, zipFile) # download .zip file from url source
    if not os.path.isdir(zipFile.replace('.zip','')):
        with zipfile.ZipFile(zipFile, 'r') as zip_: # unzip in a given folder
            for member in tqdm(zip_.infolist(), desc='Extracting'):
                try:
                    zip_.extract(member, folder)
                except zipfile.error as e:
                    pass
    print(f'zip file {zipFile} has been downloaded and extracted in {folder}')

if __name__ == '__main__':
    # create data folder if inexistent
    folder = 'data/'
    folders = os.listdir()
    if not 'data' in folders:
        os.makedirs(folder)
        
    urls = ['http://images.cocodataset.org/zips/train2014.zip',
            'http://images.cocodataset.org/zips/val2014.zip',
        'http://images.cocodataset.org/annotations/annotations_trainval2014.zip'] 

    zipFiles = ['data/train2014.zip',
                'data/val2014.zip',
                'data/annotations_trainval2014.zip']
    
    for url, zipFile in zip(urls, zipFiles):
        downloadAndUnzip(url, zipFile, folder)
        
