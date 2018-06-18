import math as m
import csv
import mne
import os.path as op
from mne.datasets import sample
import numpy as np
from mne.viz import plot_alignment
from matplotlib import pylab as plotter 
from matplotlib import pyplot as plt
from scipy import signal, fftpack
from mne.viz import plot_filter, plot_ideal_filter
from mne.time_frequency.tfr import morlet

class Filter():
	def __init__(self,path,transformer=None):
		self.path = path
		self.signal_data = mne.io.read_raw_brainvision(path, montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)
		self.raw = mne.io.read_raw_brainvision(path,preload=True)
		self.data, self.times = self.raw[:,:]
		self.filted = None		

	def plot(self):
		print("ppplot")

	def filter(self):
		channels=[10,15]
		covolve_input = signal.firwin(400,[0.002,0.01],pass_zero=False)
		for channel in channels:
			print(channel)

		new_signal = [signal.convolve(covolve_input,self.data[channel,:]) for channel in channels]

		self.filted = new_signal	
		return new_signal

	def h_function(self,x):
		if x>0:
			return 1
		elif x<=0:
			return 0
	def bff(self,x,lower_bound,upper_bound):
		return self.h_function(x-lower_bound)-self.h_function(x-upper_bound)
	def band_filter_function(self,lower_bound,upper_bound,len):
		bff_x = np.arange(len)
		bff_y = [self.bff(i,lower_bound,upper_bound) for i in bff_x]
		return fftpack.fft(bff_y)
	def filter_custom(self,lower_bound,upper_bound):
		channels=[10,15]
		covolve_input = band_filter_function(i,4,14)
		for channel in channels:
			print(channel)

		new_signal = [signal.convolve(covolve_input,self.data[channel,:]) for channel in channels]

		self.filted = new_signal	
		return new_signal


# path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"
# my_filter = Filter(path)
# new = my_filter.filt()
# print(my_filter.times.shape)
# print(my_filter.times)
# plt.figure()
# plt.plot(np.array(range(len(new[0]))),new[0])
# # plt.plot(np.array(my_filter.times),np.array(my_filter.data[10]).T)
# plt.show()
# plotter.close()