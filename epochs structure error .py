#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:03:59 2018

@author: Carpetli
"""

import math as m
import csv
import mne
import os.path as op
from mne.datasets import sample
import numpy as np
from mne.viz import plot_alignment
from matplotlib import pyplot as plt


#mydata = mne.io.read_raw_brainvision('/Users/Carpetli/Desktop/demo_2.vhdr', montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)

mydata = mne.io.read_raw_brainvision('/Users/Carpetli/Desktop/demo_2.vhdr', montage=None,eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto', scale=1.0, preload=False, response_trig_shift=0, event_id=None, verbose=None)

data_path = op.join('/','Users','Carpetli','Desktop')

raw = mne.io.read_raw_brainvision(op.join(data_path, 'demo_2.vhdr'),preload=True)

# If your raw object has a stim channel, you can construct an event array
# easily
events = mne.find_events(raw, stim_channel='STI 014')

# Show the number of events (number of rows)
print('Number of events:', len(events))

# Show all unique event codes (3rd column)
print('Unique event codes:', np.unique(events[:, 2]))

# Specify event codes of interest with descriptive labels.
# This dataset also has visual left (3) and right (4) events, but
# to save time and memory we'll just look at the auditory conditions
# for now.

event_id = {'Auditory/Left': 897, 'Auditory/Right': 898}
#ValueError: No matching events found for Auditory/Left (event id 1)
print('我是分割线----------')
epochs = mne.Epochs(raw, events, event_id, tmin=-0.1, tmax=1,
                    baseline=(None, 0), preload=True)
print(epochs)

#epochs = mne.Epochs(raw, events, 898, tmin=-0.1, tmax=1,
                   # baseline=(None, 0), preload=True)
#print(epochs)

print(epochs.events[:3])
print(epochs.event_id)
print('我是分割线----------')

print(epochs[1:5])
print(epochs['Auditory/Right'])

# These will be epochs objects
for i in range(3):
    print(epochs[i])

# These will be arrays
for ep in epochs[:2]:
    print(ep)
    
print('-----------我是分割线----------')

ev_left = epochs['Auditory/Left'].average()
ev_right = epochs['Auditory/Right'].average()

f, axs = plt.subplots(1 2,figsize=(10, 5))
_ = f.suptitle('Left / Right auditory', fontsize=20)
_ = ev_left.plot(axes=axs[:, 0], show=False, time_unit='s')
_ = ev_right.plot(axes=axs[:, 1], show=False, time_unit='s')
plt.tight_layout()
