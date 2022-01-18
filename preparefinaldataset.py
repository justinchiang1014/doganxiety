# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
# create directories
dataset_home = 'happy_vs_anxiety/'
# create label subdirectories
labeldirs = ['happydog/', 'anxiety/']
for labldir in labeldirs:
	newdir = dataset_home + labldir
	makedirs(newdir, exist_ok=True)
# copy training dataset images into subdirectories
src_directory = 'train/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	if file.startswith('anxiety'):
		dst = dataset_home + 'anxiety/'  + file
		copyfile(src, dst)
	elif file.startswith('happydog'):
		dst = dataset_home + 'happydog/'  + file
		copyfile(src, dst)