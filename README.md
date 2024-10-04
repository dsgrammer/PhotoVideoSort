# PhotoVideoSort
A program for automating sorting photos and videos into year/month/photo or year/month/video directories

The current implementation of this program has the following constraints:
1. It parses the file name for date format YYYYMMDD
2. It can only process files that look like 'PXL_20240525_022448208.jpg' where the first 3-4 characters are ignored and the next 8 characters are parsed as the date.

Future versions will look to change how the date is managed by utilizing photo metadata to provide more robust coverage for files from different devices where file names do not fit the required format.
