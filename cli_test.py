from argparse import ArgumentParser, Namespace
import time
from pvsort.sort import Sort
from pathlib import Path

def main():
    parser = ArgumentParser()
    # group = parser.add_mutually_exclusive_group()

    parser.usage = "cli_test.py [-h] sourceDir [targetDir] \n \
        example: python3 cli_test.py 'C:/files'"

    parser.add_argument('sourceDir', type=str, help="Source directory where the photos/videos that need to be sorted reside.")
    # add default here for if nothing is provided make target the same as source
    parser.add_argument('targetDir', type=str, help="Optional: Target directory where you want to sorted files. \
                        If not provided target directory will default to source directory.", default="", nargs="?")

    args: Namespace = parser.parse_args()
    result1: str = args.sourceDir
    if args.targetDir == "":
        result2 = result1
    else:
        result2: str = args.targetDir

    print(f"Source directory is {result1}")
    print(f"Target directory is {result2}")

    print("")
    print("Begin renaming files.")
    Sort.changeFileName(Path(result1))
    print("Done renaming files.")
    print("")
    time.sleep(2)
    print("Begin photo sort.")
    print("")
    Sort.sortPhotos(Path(result1), Path(result2))
    print("Done.")


if __name__ == '__main__':
	main()
     