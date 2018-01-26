#!/usr/bin/evn python2.7

#Author: Thomas Noelcke
#purpose: The pourpose of this script is to prove that we can get data from the Thredds database using 
#OPENDAP getting a netcdf4 file for a specific lat long. We will then take the file and turn it in to
#JSON file and output the result to a file.


from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt


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

#get the data lat long data.
lat = lathandle[:]
lon = lonhandle[:]

#find the indices of the target lat/lat/lon/day
#lat_index = (np.abs(lat - lat_array)).argmin()
#lon_index = (np.abs(lon - lon_array)).argmin()
lat_index = np.searchsorted(lat, latTarget, side='right')
lon_index = np.searchsorted(lon, lonTarget, side='right')


#check to make sure we are with in bounds.
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
lat = lat[lat_index]
lon = lon[lon_index]

print(lat_index, lon_index)

#get the actual climate data
data = []
for i in range(7):
	data.append(datahandle[lat_index, lon_index, 0])

print(data)
