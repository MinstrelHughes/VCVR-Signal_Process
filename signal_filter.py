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
	path = None

	def __init__(self,path):
		self.path = path
		self.signal_data = mne.io.read_raw_brainvision(path, montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)
		self.raw = mne.io.read_raw_brainvision(path,preload=True)

	def 

my_filter = Filter(path)