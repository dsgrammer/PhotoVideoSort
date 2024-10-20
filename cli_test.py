from argparse import ArgumentParser, Namespace
import time
from pvsort.sort import Sort

def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    #parser.usage = "this is how you use the cli -h"

    parser.add_argument('sourceDir', type=str, help="")
    parser.add_argument('targetDir', type=str, help="", default="", nargs="?") # add default here for if nothing is provided make target the same as source

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
    Sort.changeFileName(result1)
    print("Done renaming files.")
    print("")
    time.sleep(2)
    print("Begin photo sort.")
    print("")
    Sort.sort_photos(result1, result2)
    print("Done.")


if __name__ == '__main__':
	main()
     