import sys, os, time, shutil

path = "/Users/slnburg/Desktop/Folder A/"
files = os.listdir(path)
files.sort()

for f in files:
	src = path+f
	dst = "/Users/slnburg/Desktop/Folder B/"
	shutil.move(src, dst)
print files
