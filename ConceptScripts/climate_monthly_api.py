#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Description: The script download NMME climate forecast data by given parameters 
# like latitude and longitude
# Download 7 Months of Downscaled NMME Forecast Data from current date.

# A template download URL looks like: http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?decimal-precision=2&lat=41&lon=-113&positive-east-longitude=False&data-path=/datastore/climate/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_CFSv2_forecast_1monthAverage.nc&variable=tmp2m&variable-name=tmp2m&data-path=/datastore/climate/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_CFSv2_forecast_1monthAverage.nc&variable=prate&variable-name=prate


import requests
import os
import shutil

class NMMEClimateData:
    template_url = '''http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?decimal-precision={precision}&lat={lat}&lon={lon}&positive-east-longitude=False&data-path=/datastore/climate/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_{mod}_forecast_1monthAverage.nc&variable=tmp2m&variable-name=tmp2m&data-path=/datastore/climate/bcsd-nmme/monthlyForecasts/bcsd_nmme_metdata_{mod}_forecast_1monthAverage.nc&variable=prate_anom_inches&variable-name=prate_anom_inches'''
    
    def __init__(self):
        ''' Default parameters (configuration) to call Downscaled NMME Forecast Data.
        '''
        self.precision=2
        self.lat = 44
        self.lon = -123
        self.mod = 'CFSv2'
        
        self.climate_data = []
        self.comments = ''
     
    def set_model(self, model_name):
        ''' Set model code. 
            Possible models including: 
            CMC1-CanCM3, 
            CMC2-CanCM4, 
            NCEP-CFSv2, 
            GFDL-CM2.1, 
            GFDL-FLOR,
            NASA GEOS5,
            NCAR-CXCSM4,
            Multi-Model Mean(AVGMODEL)
        '''
        self.mod = model_name
        
    def get_model(self):
        ''' Get model code.
        '''
        return self.mod
    
    def set_lat(self, latitude):
        ''' Set latitude of the point.
        '''
        self.lat = latitude
    def set_lon(self, longitude):
        ''' Set longitude of the point.
        '''
        self.lon = longitude
    def get_lat(self):
        ''' Set latitude of the point.
        '''
        return self.lat
        
    def get_lon(self):
        ''' Set longitude of the point.
        '''
        return self.lon
    
    def set_frequency(self):
        ''' Set frequency.
        '''
        pass
        
    def set_product(self):
        ''' Set product.
        '''
        pass
        
    def prepare_url(self):
        ''' Prepare the url to download climate data by format template url 
            with specified parameters.
        '''
        return NMMEClimateData.template_url.format(precision=self.precision, lat=self.lat, lon=self.lon, mod=self.mod)
    
    def download_climate(self):
        ''' Download climate data.
        '''
        url = self.prepare_url()
        r = requests.get(url)
        r.close()
        text = str(r.content)
        lines = text.replace("<br//>", "\n").replace("<br />", "\n").split("\n")
        for ln in lines:
            ln = ln.strip()
            if ln == '':
                continue
            if ln[0] == '#': # skip comment lines
                self.comments += ln + '\n'
            else:  # climate forecast data
                self.climate_data.append(ln.split(','))
        
    def save_climate_forecast_json(self, fname):
        ''' Save climate data as json file.
        '''
        pass
    
    def load_climate_forecast_json(self, fname):
        ''' Load climate forecast data from json file.
        '''
        pass
        
    def save_climate_forecast_txt(self, fname):
        ''' Save climate forecast data to text file.
        '''
        with open(fname, 'w') as f:
            f.write(self.comments)
            for items in self.climate_data:
                f.write(','.join(items)+'\n')
        
    
    def load_climate_forecast_txt(self, fname):
        ''' Read climate forecast data from text file.
        '''
        self.comments = ''
        self.climate_data = []
        with open(fname) as f:
            ln = f.readline()
            if ln[0] == '#': # skip comment lines
                self.comments += ln
            else:  # climate forecast data
                self.climate_data.append(ln.split(','))
    
    def __str__(self):
        ''' Return string representation of this climate forecast data.
        '''
        return self.comments + '\n'.join([','.join(items) for items in self.climate_data])


if __name__ == '__main__':
    climate = NMMEClimateData()
    climate.prepare_url()
    climate.download_climate()
    print (climate)
