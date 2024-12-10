# PhotoVideoSort
A program for automating sorting photos and videos into year/month/photo or year/month/video directories

The current implementation of this program has the following constraints:
1. first renames all files according to the timestamp in their metadata format YYYYMMDD_HHMMSS + the file extension.
2. It parses the file name for date format YYYYMMDD
3. Any files without a photo or video file extension are "quarantined" to a folder called other in the source directory. (This folder is created by the script)

Future implementations will strive to make a standalone gui application or cli tool out of this script.



##
Need to add functioality for "recurse" in case there are directories inside directories -> all the way to the bottom level