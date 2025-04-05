import numpy as np
from scipy.signal import lti

class RLC_Notch:
    """
    RLC_Notch Filter
    """
    def __init__(self, R=None, L=None, C=None, T=1):
        self.R = R
        self.L = L
        self.C = C
        self.T = T

    def lti(self):
        #Coefficients Numerateur (s^2 + 1/LC)
        num = [1, 0, 1 / (self.L * self.C)]
        #Coefficients Denominateur (s^2 + R/L * s + 1/LC)
        den = [1, self.R / self.L, 1 / (self.L * self.C)]
        return lti(num, den)
    
    def get_params(self):
        #Parametres en fonction des composants
        w0 = 1 / np.sqrt(self.L * self.C)  #Resonance
        m = self.R / (2 * np.sqrt(self.L / self.C))  #facteyr d'amortissement
        delta_w = 2 * m * w0  #largeure bande rejeter
        return self.T, w0, m, delta_w
    
    def set_components(self, T, w0, m):
        #composant en fonction des parametres
        if self.C is None:
            self.C = 1.1e-6  # Exemple : 1 µF

        self.L = 1 / (w0 ** 2 * self.C) 
        self.R = 2 * m * np.sqrt(self.L / self.C)
        return self.R, self.L, self.C
    
class TwinT_Notch:
    """
    Twin-T Notch Filter
    """
    def __init__(self, R=None, C=None, T=1):
        self.R = R
        self.C = C
        self.T = T

    def lti(self):
        #Coefficients Numerateur (s^2 + 1/RC * s + 1/(R^2 * C^2))
        num = [1, 1 / (self.R * self.C), 1 / (self.R ** 2 * self.C ** 2)]
        #Coefficients Denominateur (s^2 + 3/(2*RC) * s + 1/(R^2 * C^2))
        den = [1, 3 / (2 * self.R * self.C), 1 / (self.R ** 2 * self.C ** 2)]
        return lti(num, den)
    
    def get_params(self):
        #Parametres en fonction des composants
        w0 = 1 / (self.R * self.C)  #Resonance
        m = 3 / 2  #facteyr d'amortissement
        delta_w = 2 * m * w0  #largeure bande rejeter
        return self.T, w0, m, delta_w
    
    def set_components(self, T, w0, m):
        # Set le condensateur
        if self.C is None:
            self.C = 1.1e-6  # Exemple : 1 µF

        self.R = 1 / (w0 * self.C)  # Resolution en fonction de w0 et C
        return self.R, self.C
    
class ActiveTwinT_Notch:
    """
    Active Twin-T Notch Filter
    """
    def __init__(self, R=None, C=None, R1=None, R2=None, T=1):
        self.R = R
        self.C = C
        self.R1 = R1
        self.R2 = R2
        self.T = T

    def lti(self):
        #Coefficients Numerateur ((RC) ** 2 * s^2 + 1)
        num = [(self.R ** 2 * self.C ** 2), 0, 1]
        #Coefficients Denominateur ((RC) ** 2 * s^2 + (RC / (1 + (R5/R4))) * s + 1)
        den = [(self.R ** 2 * self.C ** 2), self.R * self.C / (1 + (self.R2 / self.R1)), 1]
        return lti(num, den)
    
    def get_params(self):
        #Parametres en fonction des composants
        w0 = 1 / (self.R * self.C)  #Resonance
        m = (1 / 2) * (1 / (1 + (self.R2 / self.R1)))  # Facteur d'ammortissement
        delta_w = 2 * m * w0  #largeure bande rejeter
        return self.T, w0, m, delta_w
    
    def set_components(self, T, w0, m):
        # Si C n'est pas déjà défini, fixer une valeur par défaut
        if self.C is None:
            self.C = 1.1e-6  # Exemple : 1 µF

        self.R = 1 / (w0 * self.C)  # Calculer R en fonction de w0 et C
        self.R1 = 10e3  # Exemple : R1 = 10 kΩ
        self.R2 = self.R1 * ((1 / (2 * m)) - 1)  # Calculer R2
        return self.R, self.C, self.R1, self.R2
