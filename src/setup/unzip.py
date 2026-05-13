import os
from pathlib import Path
import yaml

def find_zip_files(directory):
    """Find all .zip files in the given directory."""
    return list(Path(directory).glob("**/*.zip"))


def unzip_files_in_directory(path): 
    zip_files = find_zip_files(path)

    for zip_file in zip_files:
        print(f"unzipping file {zip_file} ...")

        os.system(f"unzip -q {zip_file} -d {path}")
        os.system(f'rm {zip_file}')

        print(f"file {zip_file} unzipped")

if __name__ == '__main__':
    setup_dir = Path(__file__).resolve().parent
    repo_root = setup_dir.parents[1]
    with open(setup_dir / 'config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    data_dir = config['data_dir']
    if not os.path.isabs(data_dir):
        data_dir = str(repo_root / data_dir)
    unzip_files_in_directory(data_dir)
