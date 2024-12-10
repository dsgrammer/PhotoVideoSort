from pvsort.date_conversion import DateProcessing
from datetime import datetime
import os
import shutil
import re
from pathlib import Path

class Sort():
    def __init__(self) -> None:
            pass

    def changeFileName(source_dir) -> None:
        photo_extensions: set[str] = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic'}
        video_extensions: set[str] = {'.mp4', '.mov', '.avi', '.mkv', '.flv'}
        in_case_duplicates: int = 1

        for item in source_dir.iterdir():
            if item.is_file():
                print(f"Prcessing File in Root: {item}")
                # for path in pathlib.Path(item).iterdir():
                info = item.stat()
                ctime: float = info.st_ctime
                mtime: float = info.st_mtime

                if mtime <= ctime:
                    date_created: datetime = DateProcessing.dateConversion(mtime)
                else:
                    date_created: datetime = DateProcessing.dateConversion(ctime)

                file_name, file_extension = os.path.splitext(item)
                file_extension = file_extension.lower()

                if file_extension in photo_extensions or file_extension in video_extensions:
                    new_filename: str = date_created + '_' + str(in_case_duplicates) + file_extension
                    os.rename(item, new_filename)

                    print(f"{file_name} -> {new_filename}")
                    shutil.move(f"./{new_filename}", os.path.join(source_dir, new_filename))
                    in_case_duplicates = in_case_duplicates + 1
                else:
                    pass
                
            elif item.is_dir():
                for file in item.iterdir():
                    print(f"Processing file in subdirectory: {item} : {file}")
                    if file.is_file():
                        #for path in pathlib.Path(file).iterdir():
                        info = file.stat()
                        ctime: float = info.st_ctime
                        mtime: float = info.st_mtime

                        if mtime <= ctime:
                            date_created: datetime = DateProcessing.dateConversion(mtime)
                        else:
                            date_created: datetime = DateProcessing.dateConversion(ctime)

                        file_name, file_extension = os.path.splitext(file)
                        file_extension = file_extension.lower()

                        if file_extension in photo_extensions or file_extension in video_extensions:
                            new_filename: str = date_created + '_' + str(in_case_duplicates) + file_extension
                            os.rename(file, new_filename)

                            print(f"{file_name} -> {new_filename}")
                            shutil.move(f"./{new_filename}", os.path.join(source_dir, new_filename))
                            in_case_duplicates = in_case_duplicates + 1
                        else:
                            pass

        # add loop for directory and then nest the below inside, then test if it works as intended even if there are not subdirectories in the provided root.
        

    # Function for moving files (photos and videos) from one directory to a new sorted by Year/month directory
    def sortPhotos(source_dir, target_dir) -> None:
        # This pattern is used to parse the file name for the date pattern used in this program
        # ^[A-Z]{3,4}_ this pattern is used to ignore the first 3-4 characters in the file name
        # (\d{4})(\d{2})(\d{2}) This pattern is obtaining the date in format YYYYMMDD
        date_pattern = re.compile(r"(\d{4})(\d{2})(\d{2})")

        # -- Can make these a constant? --
        photo_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic'}
        video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv'}

        # Checks if target directory entered exists or not, if not will create the target directory.
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print("created target directory - parent folder")
            
        print("checked if target directory exists")

        # This is the for loop for iterating over every file in the source directory.
        for filename in os.listdir(source_dir):
            # Join the source directory path and the file name to create the full path of the file.
            file_path = os.path.join(source_dir, filename)

            # print the file name and the created full path to display as a checkpoint.
            print(filename)
            print(file_path)

            # split the filename on the '.' like filename.jpg -> filename, .jpg and save '.jpg' as file_extension
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension not in photo_extensions and file_extension not in video_extensions:
                other_dir = os.path.join(source_dir, 'others')
                if not os.path.exists(other_dir):
                    os.makedirs(other_dir)
                shutil.move(file_path, os.path.join(other_dir, filename))

            # Check if the fullpath is a file and not a directory.
            if os.path.isfile(file_path):
                # if the filename is indeed a file, search for the date pattern using the predefined pattern as date_pattern.
                match = date_pattern.search(filename)

                # If the date in the file name matches the date_pattern the file will be processed. If not will output an error message.
                if match:
                    # group(1) group(2) and group(3) correspond with the values in the date pattern (\d{4})(\d{2})(\d{2}) in order from left to right.
                    year, month, day = match.group(1), match.group(2), match.group(3)

                    # Using the input target directory path, create the new destination directories for the files to be moved.
                    # The year/month format will create a directory for Year and then inside it create a seperate directory for each month.
                    year_month_dir = os.path.join(target_dir, f"{year}\{month}")

                    # if the new target directories do not already exist, create them.
                    if not os.path.exists(year_month_dir):
                        os.makedirs(year_month_dir)

                    # split the filename on the '.' like filename.jpg -> filename, .jpg and save '.jpg' as file_extension
                    #file_extension = os.path.splitext(filename)[1].lower()

                    if file_extension in photo_extensions:
                        photos_dir = os.path.join(year_month_dir, 'photos')
                        if not os.path.exists(photos_dir):
                            os.makedirs(photos_dir)
                        # This function moves the file from the source directory (using the full path as the identifier)
                        # and creates new file paths for the new Year/Month/photos/filename
                        shutil.move(file_path, os.path.join(photos_dir, filename))
                        # Output progress
                        print(f"Moved {filename} to {year}\{month}\photos")


                    elif file_extension in video_extensions:
                        video_dir = os.path.join(year_month_dir, 'videos')
                        if not os.path.exists(video_dir):
                            os.makedirs(video_dir)
                        # This function moves the file from the source directory (using the full path as the identifier)
                        # and creates new file paths for the new Year/Month/videos/filename
                        shutil.move(file_path, os.path.join(video_dir, filename))
                        # Output progress
                        print(f"Moved {filename} to {year}\{month}\videos")

                    else:
                        print(f"Skipping {filename} (unknown file type)")
                        

                else:
                    print(f"No date found in {filename}")

