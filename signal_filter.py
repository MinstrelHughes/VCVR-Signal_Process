import math as m
import csv
import mne
import os.path as op
from mne.datasets import sample
import numpy as np
from mne.viz import plot_alignment

from matplotlib import pyplot as plt
from scipy import signal, fftpack
from mne.viz import plot_filter, plot_ideal_filter
from mne.time_frequency.tfr import morlet

class Filter():
	def __init__(self,path,transformer):
		self.path = path
		self.signal_data = mne.io.read_raw_brainvision(path, montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)
		self.raw = mne.io.read_raw_brainvision(path,preload=True)

	def plot():

	def filt():
		signals = self.raw.readsomething[]
		# signals = signal.firwin2(n, freq, gain, nyq=nyq)
		wavelet = signal.firwin(400,[0.002,0.01],pass_zero=False)
		for i in 

		for i in signals:
			processed_signals = 


path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"
my_filter = Filter(path)