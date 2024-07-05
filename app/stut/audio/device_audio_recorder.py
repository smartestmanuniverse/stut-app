#coding: utf-8

import subprocess

import sounddevice as sd

# Make sure NumPy is loaded before it is used in the callback
# with a alias 'np' and a alias 'numpy'
import numpy as np, numpy
assert numpy  # avoid "imported but unused" message (W0611)

def list_devices():
	print(sd.query_devices())

def get_list_devices():
	return sd.query_devices()

def show_list_of_devices():
    subprocess.call(["clear"],shell=True)
    print("Devices:\n\n{0}".format(get_list_devices()))

def get_device_id(device_name):
	devices = list(sd.query_devices())
	for device in devices:
		if device_name in device['name']:
			return device['index']
	return None

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text
    
def raise_kb_int():
	raise KeyboardInterrupt

# ##############################

# Get the audio input device
def get_n_last_amplitudes(amplitudes, n):
    return amplitudes[-n:]

# Get the amplitude of the audio signal
def get_amplitude_audio_signal(indata_array):
    return np.abs(indata_array).mean() * 200

# Increase the gain of the audio signal
def increase_gain_audio_signal(indata_array, gain=1.0):
    return indata_array * gain

# Decrease the gain of the audio signal
def decrease_gain_audio_signal(indata_array, gain=1.0):
    return indata_array / gain

# Normalize the audio signal
def normalize_audio_signal(indata_array):
    return indata_array / np.max(np.abs(indata_array))

