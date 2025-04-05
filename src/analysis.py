#!/usr/bin/env python3

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram
import tools


# ===== Chargement du son et normalisation de la valeur des échantillions =====

fs, data = wavfile.read("../wav/vuvuzela.wav")
t = np.arange(len(data))/fs
data_normalized = data/np.max(np.abs(data))

tools.affichage_graph(t, data_normalized, "Temps [s]", "Amplitude", None, None, "Enregistrement sonore complet")


# ===== Isolation du Son de Vuvuzela =====

start_time = 0
end_time = 3.8

start_index = int(start_time * fs)
end_index = int(end_time * fs)

vuvuzela_section = data_normalized[start_index:end_index]

data_vuvuzela_1, t_vuvuzela_1 = tools.isolation_de_son(start_time, end_time, fs, data_normalized)

tools.affichage_graph(t_vuvuzela_1, data_vuvuzela_1, "Temps [s]", "Amplitude", None, None, "Echantillon Vuvuzela")

# ===== Analyse Spectrale =====

# Calcul du périodogramme
frequencies, power_spectrum = periodogram(vuvuzela_section, fs)

# Affichage du spectre de fréquence
tools.affichage_graph(frequencies, power_spectrum, "Fréquence [Hz]", "Densité spectrale de puissance", 0, 2000,"Analyse spectrale du son de vuvuzela")

bands = [25, 51, 60, 64]
frequencies = [235, 710, 1181, 1402]
for idx in range (0, 4):
    m = bands[idx] / (2 * frequencies[idx])
    print("band : " + str(bands[idx]) + ", frequencies : " + str(frequencies[idx]) + ", m : " + str(m) + "\n")
