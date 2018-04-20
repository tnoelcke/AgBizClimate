#OPeNDAP Eample Script: Simple R version
#Purpose: This script pulls one 7 month period from the threads server.



#laod the libray
library(ncdf4)

#Define the URL
urltotal<-"http://thredds.northwestknowledge.net:8080/thredds/dodsC/NWCSC_INTEGRATED_SCENARIOS_ALL_CLIMATE/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_CMC1_forecast_1monthAverage.nc"

## open file
ncin <- nc_open(urltotal)

ncin

v3 <- ncin$var[[1]]

timesize <- v3$varsize[1]

print("Time size")
timesize

lonsize <- v3$varsize[2]

print("lon size")
lonsize


latsize <- v3$varsize[3]

print("lat size")
latsize


## define our point of interest
## note make sure to check weather your source starts counting at 0 or 1
## e.g. ncdf4 Pcakge starts counting at 1 but OPeNDap Dataset access starts at 0

lon = 1081
lat  = 444

##define our variable name

var="tmp2m"

data <- ncvar_get(ncin, var, start=c(1, 500, 500), count=c(1, 1, 1))

print("data")

data

nc_close(ncin)

#show the data




