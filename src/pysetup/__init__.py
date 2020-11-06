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
    
    for x in files:
        Path(x).touch()

    os.makedirs("src/"+args.name)
    os.mkdir("tests")
    os.mkdir("data")
    Path("src/"+args.name+"/__init__.py").touch()
    os.chmod("src/"+args.name+"/__init__.py", 755)
    os.chmod("setup.py", 755)

if __name__ == "__main__":
    main()
