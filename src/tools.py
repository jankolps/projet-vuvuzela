import matplotlib.pyplot as plt
import numpy as np

# Création et affichage d'un graphique
def affichage_graph(t, data, xlabel = "Temps [s]", ylabel = "Amplitude", xmin = None, xmax = None, title = "Echantillon sonore"):
    plt.plot(t, data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xmin, xmax)
    plt.title(title)
    plt.show()

# fonction d'isolation d'un son entre deux bornes de temps
def isolation_de_son(start_time, end_time, fs, data_normalized):
    start_index = int(start_time * fs)
    end_index = int(end_time * fs)

    # Extraire la portion du signal correspondant à cet intervalle
    section = data_normalized[start_index:end_index]

    # Calcul du temps pour la portion extraite
    t = np.arange(start_index, end_index) / fs

    return section, t
