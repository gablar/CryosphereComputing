"""
Created on Sun Oct 21 13:36:16 2018
@author: Nico Sun

The script decompresses and NOAA Northern Hemisphere Snow Cover Data
https://nsidc.org/data/g02156
"""

import os
import io
import re
import gzip
import numpy as np


def mass_converter(text_file,filename):
	'''This function saves all data in a cropped and unit8 format'''
	snow = np.genfromtxt(text_file,skip_header =30,delimiter=1)
	snowmap = np.flip(snow,axis=1)
	snowmap = snowmap[220:830,250:700]
	snowmap = np.rot90(snowmap,k=2)
	snowbinary = np.array(snowmap,dtype='uint8')
	with open(os.path.join('DataFiles',filename+'.bin'), 'wb') as writer:
		writer.write(snowbinary)


		
def decompress():
	'''this function decompresses all files'''
	filepath = 'X:/SnowCover/DataFiles/gzip_files'
	pattern = r'NOAA'
	for file in os.listdir(filepath):		
		match = re.search(pattern,file)
		if match:
			#print(os.path.join(filepath,file))
			print(os.path.join('X:/SnowCover/ DataFiles/gzip_files',file[0:17]+'.dat'))
			with gzip.open(os.path.join(filepath,file), mode='rb') as fr:
				file_content = fr.read()
			text_file = io.BytesIO(file_content)
			mass_converter(text_file,file[0:17])
				
def dailyupdate(filenameformatted):
	'''this function handels daily automated updates'''
	with gzip.open(os.path.join('X:/SnowCover/DataFiles/gzip_files',filenameformatted), mode='rb') as fr:
		file_content = fr.read()
				

	text_file = io.BytesIO(file_content)
	snow = np.genfromtxt(text_file,skip_header =30,delimiter=1)
	snowmap = np.flip(snow,axis=1)
	snowmap = snowmap[220:830,250:700]
	snowmap = np.rot90(snowmap,k=2)
	snowbinary = np.array(snowmap,dtype='uint8')
	with open(os.path.join('X:/SnowCover/DataFiles',filenameformatted[0:17]+'.bin'), 'wb') as writer:
		writer.write(snowbinary)
#	os.remove(os.path.join('X:/SnowCover/DataFiles/gzip_files',filenameformatted[0:17]+'.asc'))


year = 1997
day = 36
daycount = 1

#for year in range(2004,2019):
if __name__ == "__main__":
	print('main')
#	decompress()
#	mass_converter()

#for day in range(1,366):
	#decompress(str(day).zfill(3))

#rename(year,month)
