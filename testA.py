import numpy as np
import matplotlib.pyplot as plt
# Nombre de valeurs simulees
n = 1000000
# Parametres
n_1 = 0.174
c = 5.00
V_E1mes = 10.7e-3
V_E2mes = 7.2e-3
# Incertitude
V_E1 = V_E1mes + 0.05*np.random.randn(n)
V_E2 = V_E2mes + 0.05*np.random.randn(n)
# Calcul de la quantite d'ester
n_ester = n_1-c*(V_E1 - V_E2)
# Trace de l'histogramme associe
plt.hist(n_ester, 100, label="Simulation de valeurs de quantite d'ester")
plt.xlabel("Quantite d'ester forme")
plt.ylabel("Nombre de mesures")
plt.title("Histogramme des mesures simulees")
plt.axvline(x=np.mean(n_ester)-np.sqrt(2)*c*0.05, color = 'red', label = 'Intervalle de confiance')
plt.axvline(x=np.mean(n_ester)+np.sqrt(2)*c*0.05, color = 'red', label = 'Intervalle de confiance')
plt.legend() 
plt.show()
