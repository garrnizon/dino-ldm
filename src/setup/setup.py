import os
from pathlib import Path

import yaml

from unzip import unzip_files_in_directory
from yfile import download_from_yadisk

_SETUP_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SETUP_DIR.parents[1]


if __name__ == '__main__':
    with open(_SETUP_DIR / 'config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    data_dir = config['data_dir']
    if not os.path.isabs(data_dir):
        data_dir = str(_REPO_ROOT / data_dir)
    os.makedirs(data_dir, exist_ok=True)

    for file_url in config['yadisk']:
        download_from_yadisk(file_url, data_dir)
    
    imagenet_dir = f'{data_dir}/imagenet'
    os.makedirs(imagenet_dir, exist_ok=True)

    for class_ in config['imagenet_classes']:
        os.system(f'wget https://image-net.org/data/winter21_whole/{class_}.tar')
        
    for class_ in config['imagenet_classes']:
        class_dir = f'{imagenet_dir}/{class_}'
        os.makedirs(class_dir, exist_ok=True)
        os.system(f'tar -xf {class_}.tar -C {class_dir}')
        os.remove(f'{class_}.tar')
    
    unzip_files_in_directory(data_dir)
