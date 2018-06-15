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

	def plot(self):
		print("ppplot")

	def filt(self):
		channels=[10,15]
		print("worinidie")
		# plotter.figure()
		covolve_input = signal.firwin(400,[0.002,0.01],pass_zero=False)
		# for channel in channels:
		# 	print(self.data[channel,:].shape)
		new_signal = [signal.convolve(covolve_input,self.data[channel,:]) for channel in channels]

		print("new signals length", len(new_signal[0]))
		print("new signals length", len(new_signal[1]))		
		return new_signal
		# signals = self.raw.readsomething[]
		# signals = signal.firwin2(n, freq, gain, nyq=nyq)
		# for i in 

		# for i in signals:
		# 	processed_signals = 


path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"
my_filter = Filter(path)
new = my_filter.filt()
# print(len(shape))
print(my_filter.times.shape)

# print("haimeikaishi")
# plt.figure()
# print("kaishi show")
# plt.plot(my_filter.times,new[0])
# print("show buwan le nimabi")
# plt.show()
# plotter.close()