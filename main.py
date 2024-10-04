
# Import Libraries
import os
import shutil
import re

# Function for moving files (photos and videos) from one directory to a new sorted by Year/month directory
def sort_photos(source_dir, target_dir):
	# This pattern is used to parse the file name for the date pattern used in this program
	# ^[A-Z]{3,4}_ this pattern is used to ignore the first 3-4 characters in the file name
	# (\d{4})(\d{2})(\d{2}) This pattern is obtaining the date in format YYYYMMDD
	date_pattern = re.compile(r"^[A-Z]{3,4}_(\d{4})(\d{2})(\d{2})")

	photo_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
	video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv'}

	# Checks if target directory entered exists or not, if not will create the target directory.
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)

	# This is the for loop for iterating over every file in the source directory.
	for filename in os.listdir(source_dir):
		# Join the source directory path and the file name to create the full path of the file.
		file_path = os.path.join(source_dir, filename)

		# print the file name and the created full path to display as a checkpoint.
		print(filename)
		print(file_path)

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
				year_month_dir = os.path.join(target_dir, f"{year}/{month}")

				# if the new target directories do not already exist, create them.
				if not os.path.exists(year_month_dir):
					os.makedirs(year_month_dir)

				# split the filename on the '.' like filename.jpg -> filename, .jpg and save '.jpg' as file_extension
				file_extension = os.path.splitext(filename)[1].lower()

				if file_extension in photo_extensions:
					photos_dir = os.path.join(year_month_dir, 'photos')
					if not os.path.exists(photos_dir):
						os.makedirs(photos_dir)
					# This function moves the file from the source directory (using the full path as the identifier)
					# and creates new file paths for the new Year/Month/photos/filename
					shutil.move(file_path, os.path.join(photos_dir, filename))
					# Output progress
					print(f"Moved {filename} to {year}/{month}/photos")


				elif file_extension in video_extensions:
					video_dir = os.path.join(year_month_dir, 'videos')
					if not os.path.exists(video_dir):
						os.makedirs(video_dir)
					# This function moves the file from the source directory (using the full path as the identifier)
					# and creates new file paths for the new Year/Month/videos/filename
					shutil.move(file_path, os.path.join(video_dir, filename))
					# Output progress
					print(f"Moved {filename} to {year}/{month}/videos")

				else:
					print(f"Skipping {filename} (unknown file type)")

			else:
				print(f"No date found in {filename}")

def main():
	source_dir = "/home/derek/Pictures/Isaac Photo Backups"
	target_dir = "/home/derek/Documents/WorkSpace/Python_Projects/PhotoSort/targetpic"
	sort_photos(source_dir, target_dir)


if __name__ == '__main__':
	main()