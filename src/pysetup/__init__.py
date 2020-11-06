import argparse, os, subprocess
from pathlib import Path


files = ["setup.py", "setup.cfg", "Manifest.in", "README.md", "LICENSE.txt"]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("name", help = "Name of the package")
    args = parser.parse_args()

    try:
        os.mkdir(args.name)
    except FileExistsError:
        print("A package with this name already exists")
        exit(-1)
    
    os.chdir(args.name)
    
    for file in files:
        fd = os.open(file, os.O_CREAT, 644) 
        os.close(fd)

    os.makedirs("src/"+args.name)
    os.mkdir("tests")
    os.mkdir("data")
    os.open("src/"+args.name+"/__init__.py", os.O_CREAT, 0o755)
    os.close(fd)
    os.chmod("setup.py", 0o755)

if __name__ == "__main__":
    main()
