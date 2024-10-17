from argparse import ArgumentParser, Namespace

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