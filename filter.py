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

# Read data from my computer 
path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"

mydata = mne.io.read_raw_brainvision(path, montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)

# data_path = op.join('/','Users','Carpetli','Desktop')
raw = mne.io.read_raw_brainvision(path,preload=True)

# Input some basic factor 
sfreq = 512
dev_head_t = 3

# 50 Hz trasbandwidth, 100-50 = 0, f_s - f_p = 50 
trans_bandwidth = 50

# ass_zero : bool, optional . 
#If True, the gain at the frequency 0 (i.e. the “DC gain”) is 1. Otherwise the DC gain is 0.
pass_zero = 0

#Band-pass
f_s = 100
f_p = 50

# the Nyquist frequency is half our sample rate
nyq = sfreq / 2 

#The length of the filter would be 400 sec
filter_dur = 400.

# plot 
flim = (1., sfreq / 2.)  # limits for plotting
third_height = np.array(plt.rcParams['figure.figsize']) * [1, 1. / 3.]
freq = [0., f_p, f_s, nyq]
gain = [1., 1., 0., 0.]
ax = plt.subplots(1, figsize=third_height)[1]
title = '%s Hz lowpass with a %s Hz transition' % (f_p, trans_bandwidth)
plot_ideal_filter(freq, gain, ax, title=title, flim=flim)

#plot of the filter - - 400s, 400/trasband = 8, which is 8 cycle, 8/ 50 hz =  0.16
n = int(round(sfreq * 0.16)) + 1
h = signal.firwin2(n, freq, gain, nyq=nyq)
plot_filter(h, sfreq, freq, gain, 'Windowed 50-Hz transition (400 sec)',flim=flim)
