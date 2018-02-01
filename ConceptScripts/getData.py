#!/usr/bin/evn python2.7

#Author: Thomas Noelcke
#purpose: The pourpose of this script is to prove that we can get data from the Thredds database using 
#OPENDAP getting a netcdf4 file for a specific lat long. We will then take the file and turn it in to
#JSON file and output the result to a file.


from netCDF4 import Dataset
import numpy as np
import sys
import math


#this will check the nearest one hundered points and will return -1 -1 if data cannot be found with in a 10 by 10 grid
#near the point.
#this function takes the lat index Lon index and the data handle and 
def searchForData(lat_index, lon_index, maxLat, maxLon, datahandle):
	#check every point with in 5 points of lon_index and lat_index.
	for i in range(-5, 5, 1):
		for j in range(-5, 5, 1):
			#check to make sure that adding j and i to the indexes don't cause them to go out of range
			if(i + lat_index < maxLat and i + lat_index >= 0 and lon_index + j < maxLon and lon_index + j >= 0):
				#if you find a point with data in it return it.
				if(not math.isnan(datahandle[lat_index + i, lon_index + j, 0])):
					return (lat_index + i, lon_index + j)
	return (-1, -1)


#this function takes the target_lat, target_lon, lathandle and lonhandle
#and returns the nearest point with data to the lat lon passed in.
def getIndex(latTarget, lonTarget, lathandle, lonhandle, datahandle):
	#gets the list of possible lat long values.
	lat = lathandle[:]
	lon = lonhandle[:]
	#searches through the possible options and selects the closest option
	lat_index = np.searchsorted(lat, latTarget, side='right')
	lon_index = np.searchsorted(lon, lonTarget, side='right') 
	
	print("Lat Index: ", lat_index, " Lon Index: ",lon_index)
	
	#Does a bounds check
	if(lat[lat_index] > latTarget):
		if(lat_index != 0):
			lat_index = lat_index - 1
	if(lat[lat_index] < latTarget):
		if(lat_index != len(lat)):
			lat_index = lat_index + 1
	if(lon[lon_index] > lonTarget):
		if(lon_index != 0):
			lon_index = lon_index - 1
	if(lon[lon_index] < lonTarget):
		if(lon_index != len(lon)):
			lon_index = lon_index + 1
			
	print(" Estimated Lat: ", lat[lat_index]," Estimated Lon: ", lon[lon_index])
	#in this section we will peak at the data and make sure that we have data at indexes we've specified.
	#if we don't we will change them slightly and check again until we have the nearest point that has data.
	check = datahandle[lat_index, lon_index, 0]
	print(check)
	if not math.isnan(check):
		return (lat_index, lon_index)
	(lat_index, lon_index) = searchForData(lat_index, lon_index, len(lat), len(lon), datahandle)
	print(lat[lat_index], lon[lon_index])
	print(latTarget, lonTarget)
	return (lat_index, lon_index)
	
	
# set up target data later we will set this up to take command line args.
latTarget = -1
lonTarget = -1
if(len(sys.argv) >= 3):
	latTarget = float(sys.argv[1])
	lonTarget = float(sys.argv[2])
else:
	print("Usage: python getData.py [lat] [long]")
	exit(1)
#set the OPENDAP Path
path = "http://thredds.northwestknowledge.net:8080/thredds/dodsC/NWCSC_INTEGRATED_SCENARIOS_ALL_CLIMATE/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_ENSMEAN_forecast_1monthAverage_nochunk.nc"


#set up the data handles to filter the data
filehandle = Dataset(path, 'r', format="netcdf3")
lathandle = filehandle.variables['lat']
lonhandle = filehandle.variables['lon']
datahandle = filehandle.variables['prate_anom']

print(datahandle[466, 1083, 0])

(latI, lonI) = getIndex(latTarget, lonTarget, lathandle, lonhandle, datahandle)
print(latI, lonI)


#get the actual climate data but only if the data exists.
data = []
if(latI >= 0 and latI >= 0 and latI < 435 and lonI < 435):
	for i in range(7):
		data.append(datahandle[latI, lonI, i])
	print(data)
else:
	print("No Luck Jo")
			










		
