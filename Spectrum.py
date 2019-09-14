#!/usr/bin/env python


from astropy.io import fits
import math
import numpy as np
import matplotlib.pyplot as mpp
import glob
import os
import errno


class Spectrum(object):

	def __init__(self, filepath):
		#self.dir = r'/Users/paulb/Python_Files/SDSSData/Data/'
		#self.filename = filename
		self.filepath = filepath #os.path.join(self.dir, self.filename)
		
		try:
			self.data= fits.open(self.filepath)
		except OSError:
			raise OSError('Input file format incorrect. Header missing END card.')
			#print("The input file specified was the incorrect format")
		except FileNotFoundError:
			raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
			#print("The file was not found in working directory")

	@property
	def wavelength(self):
		"""Wavelength binning, linear bins."""
		if getattr(self,'_wavelength',None) is None:
			# "loglam" is log10(wavelength [Å])
			self._wavelength = 10**self.data[1].data['loglam']
		return self._wavelength
	@property
	def flux(self):
		"""Flux binning, linear bins(columns)"""
		return self.data[1].data['flux']
		
	@property
	def boresight_ra(self):
		return self.data[0].header['RA']
	
	@property
	def boresight_dec(self):
		return self.data[0].header['DEC']
		
	@property
	def pointing_ra(self):
		return self.data[0].header['RADEG']
	
	@property
	def pointing_dec(self):
		return self.data[0].header['DECDEG']
		
	@property
	def object_ra(self):
		return self.data[0].header['PLUG_RA']
	
	@property
	def object_dec(self):
		return self.data[0].header['PLUG_DEC']
		
			
	def print_info(self, spectrum_list):
		'''Returns structure of the fits file with number of HDUs, types, dimensions '''
		for spectrum in spectrum_list:
			print(spectrum.info())

	def custom_plot(self, x, y, label, x_axis, y_axis):
		mpp.plot(x, y)
		mpp.title(label)
		mpp.xlabel(x_axis)
		mpp.ylabel(y_axis)
		mpp.show()
    	
	def plot_flux_wavelength(self):
		'''Plot function using matplotlib to show a plot of wavelength vs flux'''
		x = self.wavelength
		y = self.flux
		mpp.plot(x, y)
		mpp.title('SDSS')
		mpp.xlabel('Wavelength(Angstroms)')
		mpp.ylabel('Flux')
		mpp.show()
		
    	
    	
	def header_information(self):
		hdu = self.data[0]
		for key, value in hdu.header.items():
			print("{0} = {1}".format(key, value))
    
	def close_file(self):
		self.data.close()
    		
    		



