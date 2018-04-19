%Author: Thomas Noelcke
%Description: This script uses OPeNDAP to dowload specific sub set of the nmme data
%requirements: R

UNDER CONSTRUCTION

%===========================
%  SET TARGET DATA -modify only the paramaters in this section
%===========================
% geographical region
%
lat_target = [45.0 45.2];
lon_target = [-103.0 -103.5] + 360;

%Variables, Models
var_targer = [1 2 3 4 5 6 7]
model_target[1:20]
exp_target = [1:2]

outputFileName = 'maca_subset.mat'

%===================================
% SET OPENDAP PATH DIR
%===================================
pathDir='http://thredds.northwestknowledge.net:8080/thredds/dodsC/NWCSC_INTEGRATED_SCENARIOS_ALL_CLIMATE/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_NCAR_forcast_1monthAverage.nc';

pathName = pathDir;
loninfo = ncinfo(pathname, 'lon');
lonSize = loninfo.Size;
latinfo = ncinfo(pathname, 'lat');
latSize = latinfo.Size;

lat = ncread(pathname, 'lat');
lon = ncread(pathname, 'lon');

%indicies of lat/lon subset
lat_index = lat(lat_index);
lon_index = lon(lon_index);

%============================
% Paramaters
%============================

EXP_Name= {};
VAR_NAME = {'tmp2m', 'tmp2m_anom', 'prate', 'prate_anom'};


