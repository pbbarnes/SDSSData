#!/usr/bin/env python


from astropy.io import fits
import math
import numpy as np
import matplotlib.pyplot as mpp
import glob
import os


class Spectrum(object):

	def __init__(self, filename):
		self.dir = r'/Users/paulb/Python_Files/SDSSData/Data/'
		self.filename = filename
		self.filepath = os.path.join(self.dir, self.filename)
		
		try:
			self.data= fits.open(self.filepath)
		except OSError:
			print("The input file specified was the incorrect format")
		except FileNotFoundError:
			print("The file was not found in working directory")

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
		
			
	def get_info(self, spectrum_list):
		'''Returns structure of the fits file with number of HDUs, types, dimensions '''
		for spectrum in spectrum_list:
			print(spectrum.info())

    	
	def plot_all(self):
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
    		
    		
s1 = Spectrum('spec-4055-55359-0001.fits')

s1.plot_all()

s1.close_file()

s2 = Spectrum('spec-10000-57346-0003.fits')

s2.plot_all()

s2.close_file()



