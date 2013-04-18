#------------------------------------------------------------------------------
# pyutils.py
#------------------------------------------------------------------------------

import string
import os, fnmatch

#------------------------------------------------------------------------------
# Returns unique elements from a list
#------------------------------------------------------------------------------
def unique(list):
	return dict.fromkeys(list).keys()

#------------------------------------------------------------------------------
# Returns a basename of a file
#------------------------------------------------------------------------------
def basename(file):
	return os.path.splitext(os.path.basename(file))[0]

#------------------------------------------------------------------------------
# Returns a list of filtered files of a directory
#------------------------------------------------------------------------------
def getFiles(dir, filters):
	if isinstance(filters,list) == False:
		filters = [filters]
	files=[]
	for file in os.listdir(dir):
		for filter in filters:
			if fnmatch.fnmatch(file, filter):
				files.append(file)
	# print 'getFiles file list:', files
	return unique(files)

#------------------------------------------------------------------------------
# Returns a list of filtered files of a directory including subdirs
#------------------------------------------------------------------------------
def getFilesRecursive(currdir, filters):
	if isinstance(filters,list) == False:
		filters = [filters]
	filelist=[]
	for root, dirs, files in os.walk(currdir):
		# remove unwanted dirs
		if '.svn' in dirs:
			dirs.remove('.svn')
		# get file names and retrieve 
		for file in files:
			# print os.path.join(root, file)
			for filter in filters:
				if fnmatch.fnmatch(file, filter):
					filelist.append(os.path.join(root, file))
	# remove base path (get relative to the given dir)
	rellist = []
	for fname in filelist:
		rellist.append(string.replace(fname,currdir,'.'))
	filelist = rellist
	return unique(filelist)
