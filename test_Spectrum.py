#!/usr/bin/env python


from SDSSData import Spectrum as S
import glob
import os

def main():
	spectrum_list = glob.glob('/Users/paulb/Python_Files/SDSSData/Data/spec*.fits')
	print(spectrum_list)
	for spectrum in spectrum_list:
		s1 = S.Spectrum(spectrum)
		s1.plot_flux_wavelength()
		s1.close_file()



if __name__ == '__main__':
	main()