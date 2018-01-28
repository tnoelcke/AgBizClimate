#!/usr/bin/evn python2.7

#Author: Thomas Noelcke
#purpose: The pourpose of this script is to prove that we can get data from the Thredds database using 
#OPENDAP getting a netcdf4 file for a specific lat long. We will then take the file and turn it in to
#JSON file and output the result to a file.


from netCDF4 import Dataset
import numpy as np


# set up target data later we will set this up to take command line args.
latTarget = 43.1
lonTarget = -123


#set the OPENDAP Path
path = 'http://tds-proxy.nkn.uidaho.edu/thredds/dodsC/NWCSC_INTEGRATED_SCENARIOS_ALL_CLIMATE/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_ENSMEAN_forecast_1monthAverage.nc'


#set up the data handles to filter the data
filehandle = Dataset(path, 'r', format="NETCDF4")
lathandle = filehandle.variables['lat']
lonhandle = filehandle.variables['lon']
timehandle = filehandle.variables['time']
datahandle = filehandle.variables['prate_anom_inches']

#get time data
time = timehandle[:]
time_index = len(time) - 1

latI, lonI = getIndex(target_lat, target_lon, lathandle, lonhandle, datahandle)


#get the actual climate data
data = []
for i in range(7):
	data.append(datahandle[lat_index, lon_index, i])
print(data)

#this function takes the target_lat, target_lon, lathandle and lonhandle
#and returns the nearest point with data to the lat lon passed in.
def getIndex(latTarget, lonTarget, lathandle, lonhandle, datahandle):
	#gets the list of possible lat long values.
	lat = lathandle[:]
	lon = lonhandle[:]
	#searches through the possible options and selects the closest option
	lat_index = np.searchsorted(lat, latTarget, side='right')
	lon_index = np.searchsorted(lon, lonTarget, side='right')
	
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
	
	#in this section we will peak at the data and make sure that we have data at indexes we've specified.
	#if we don't we will change them slightly and check again untill we have the nearest point that has data.
	check = datahandle[lat_index, lon_index, 0]
	if not math.isnan(check):
		return lat_index, lon_index
	return searchForData(lat_index, lon_index, lat, lon, datahandle)

#this function takes the lat index Lon index and the data handle and 
def searchForData(lat_index, lon_index, maxLat, maxLon, datahandle):
	










		
