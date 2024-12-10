# PhotoVideoSort
A program for automating sorting photos and videos into year/month/photo or year/month/video directories

The current implementation of this program has the following constraints:
1. first renames all files according to the timestamp in their metadata format YYYYMMDD_HHMMSS + the file extension.
2. It parses the file name for date format YYYYMMDD
3. Any files without a photo or video file extension are "quarantined" to a folder called other in the source directory. (This folder is created by the script)
4. Latest version includes recursion when renaming files to go through every subdirectory in a hierarchy.

# How to Use (Assumes you have the latest version of Python installed)
1. Place the PhotoVideoSort directory somewhere on the same drive as the files you will sort. e.g. your C:\ drive.
2. Open terminal/cmd and use the following command to move to the PhotoVideoSort folder
    > cd "C:\PhotoVideoSort\"
3. Then to run the scrip use the following command, replaceing the source and target directories with the directories you want to use. (If you only specify the source directory, the target directory will default to the same as the source.)
    > python3 main.py "C:\source" "C:\target"
4. Congratulations, your photos and videos are now sorted in a nice and manageable way.

