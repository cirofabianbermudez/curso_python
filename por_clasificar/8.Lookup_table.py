
# Lookup table
import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd 

# Latex 
# plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=8)

# Parametros de vectores
inicio = -3; paso = 6/256; fin = 3
m = 3; n = 1; a = 1.6; b = 1.4

# Vectores para generar grafica
Vin = np.arange(inicio, fin, paso)
Vout = np.sinc(Vin)

# Guardar como en EXCEL CSV
Vout.tofile('Lookup_T.csv', sep='\n', format='%2.6f')
# pd.DataFrame(Vout).to_csv('Lookup_T.csv',header=None, index=None, float_format='%2.6f')
# np.savetxt("Lookup_T.csv", Vout, delimiter=",", fmt='%2.6f')

# Grafica
plt.plot(Vin, Vout, linewidth=0.6)

# Configuraciones de Grid
plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.4)
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.2)

# Configuraciones de Ejes
plt.axis([Vin.min(), Vin.max(), Vout.min(), Vout.max()])
plt.show()
# plt.savefig('Lookup_T.eps')

