import numpy as np
from scipy.io import wavfile
from scipy.signal import lti
from filters import RLC_Notch, TwinT_Notch, ActiveTwinT_Notch

# Paramètres globaux
frequencies = [235, 710, 1181, 1402]  # Fréquences en Hz
T0 = 1  # Gain
m = [0.053, 0.035, 0.025, 0.023]  # Facteur d'amortissement
filters_type = {"RLC" : RLC_Notch(), "TwinT_Notch" : TwinT_Notch(), "Active_TwinT_Notch" : ActiveTwinT_Notch()}

class Cascaded_Filter():

    def __init__(self, filter_list):
        self.filter_list = filter_list

    def lti(self):
        total_zeros = []
        total_poles = []
        total_gain = 1.0
        
        for filter in self.filter_list:
            H = filter.lti()
            total_zeros.extend(H.zeros)
            total_poles.extend(H.poles)
            total_gain *= filter.T

        return lti(total_zeros, total_poles, total_gain)

    def wav_output(self, filename_in, name="-post"):

        try :
            # reading input file
            print("reading input file...")
            fs, data = wavfile.read(filename_in)
            t = np.arange(len(data))/fs

            # normalizing data
            print("normalizing data...")
            data_normalized = data/np.max(np.abs(data))

            print(f"applying '{name}' filter...")
            _, data_out, _ = self.lti().output(data_normalized, t)

            # writing output file
            print("writing output file...")
            filename_out = filename_in.replace(".wav", f"_{name}_processed.wav")
            amp = np.iinfo(np.int16).max
            data_out_normalized = amp * data_out
            wavfile.write(filename_out, fs, data_out_normalized.astype(np.int16))

            print(f"Filtered file successfully saved under '{filename_out}'.\n")

        except Exception as e:
            # Affichage du message d'erreur
            print(f"An error occurred during the process : {e}\n")


def create_filter_list(filter, gain, frequencies, m):
    filter_list = []
    for idx in range (0, 4):
        filter.set_components(gain, 2*np.pi*frequencies[idx], m[idx])
        filter_list.append(filter)
    return filter_list

for i in filters_type:
    total_filter = Cascaded_Filter(create_filter_list(filters_type[i], T0, frequencies, m))
    total_filter.wav_output('../wav/vuvuzela.wav', i)
