from filters import RLC_Notch, TwinT_Notch, ActiveTwinT_Notch
import numpy as np

# Paramètres globaux
Global_frequencies = [235, 710, 1181, 1402]  # Fréquences en Hz
Global_T0 = 1  # Gain
Global_m = [0.053, 0.035, 0.025, 0.023]  # Facteur d'amortissement

def Test_RLC_Notch(frequencies, T0, m):
    # Initialisation de la classe
    filter = RLC_Notch()

    # Résultats pour chaque fréquence
    print("\n\033[1mFiltre RLC Notch\033[0m\n")
    for idx in range(0, 4):
        w0 = 2 * np.pi * frequencies[idx]  # Convertir la fréquence en pulsation
        R, L, C = filter.set_components(T0, w0, m[idx])
        print(f"Pour la fréquence \033[1m{frequencies[idx]}\033[0m Hz :")
        print(f"  R = {R:.2f} Ω")
        print(f"  L = {L:.2e} H")
        print(f"  C = {C:.2e} F")
        print()

def Test_TwinT_Notch(frequencies, T0, m):
    # Initialisation de la classe
    filter = TwinT_Notch()

    # Résultats pour chaque fréquence
    print("\n\033[1mFiltre TwinT Notch\033[0m\n")
    for idx in range(0, 4):
        w0 = 2 * np.pi * frequencies[idx]  # Convertir la fréquence en pulsation
        R, C = filter.set_components(T0, w0, m[idx])
        print(f"Pour la fréquence \033[1m{frequencies[idx]}\033[0m Hz :")
        print(f"  R = {R:.2f} Ω")
        print(f"  C = {C:.2e} F")
        print()

def Test_ActiveTwinT_Notch (frequencies, T0, m):
    # Initialisation de la classe
    filter = ActiveTwinT_Notch()

    # Résultats pour chaque fréquence
    print("\n\033[1mFiltre ActiveTwinT Notch\033[0m\n")
    for idx in range(0, 4):
        w0 = 2 * np.pi * frequencies[idx]  # Convertir la fréquence en pulsation
        R, C, R1, R2 = filter.set_components(T0, w0, m[idx])
        print(f"Pour la fréquence \033[1m{frequencies[idx]}\033[0m Hz :")
        print(f"  R = {R:.2f} Ω")
        print(f"  C = {C:.2e} F")
        print(f"  R1 = {R1:.2f} Ω")
        print(f"  R2 = {R2:.2f} Ω")
        print()

def main():
    Test_RLC_Notch(Global_frequencies, Global_T0, Global_m)
    Test_TwinT_Notch(Global_frequencies, Global_T0, Global_m)
    Test_ActiveTwinT_Notch(Global_frequencies, Global_T0, Global_m)


if __name__ == "__main__":
    main()
