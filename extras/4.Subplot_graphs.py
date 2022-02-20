# Subplot graphs

import numpy as np
import matplotlib.pyplot as plt

# Funciones
def Config_graph(n, title, xlabel, ylabel):
		axs[n].grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.4)
		axs[n].minorticks_on()
		axs[n].grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.2)
		axs[n].legend(shadow=True, loc='upper right', fontsize='small')# Mostrar la grafica
		axs[n].set_title(title)
		axs[n].set_xlabel(xlabel)
		axs[n].set_ylabel(ylabel)

# Fuente de la grafica
plt.rc('font', family='serif', size=8)    # garamong, serif, arial

# Parametros de vectores
inicio = 0
paso = 0.1
fin = 2 * np.pi + paso

# Vectores para generar grafica
x = np.arange(inicio, fin, paso)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2)
fig.subplots_adjust(hspace=0.5)

axs[0].plot(x, y1, label=r'sin x', linewidth=0.6)
axs[0].axis([x.min(), x.max(), y1.min(), y1.max()])
Config_graph(0, 'Gráfica 1', 'Tiempo (s)', 'Voltaje (V)')

axs[1].plot(x, y2, label=r'cos x', linewidth=0.6)
axs[1].axis([x.min(), x.max(), y2.min(), y2.max()])
Config_graph(1, 'Gráfica 2', 'Tiempo (s)', 'Voltaje (V)')

# Mostrar la grafica
plt.show()

# Guardar la grafica como eps, png, es necesario comentar plt.show()
# plt.savefig('graph_name.png')

# Tipos de letra extras 
# garamong, serif, arial

# Titulo de la grafica
# plt.title(r'f(x) = sin(x)')      # Add an r Raw String Literal

# Para agregar texto en algun lugar de la grafica
# plt.text(3, 0.5, 'Notas', size=6)

# Parametros extra de grafica
# color='#444444', linestyle='--', marker='.', linewidth=2, markersize=5

# Tamanios de letra
# fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}

# Estilos de grafica
# Line Styles
# character   description
# '-'   solid line style
# '--'  dashed line style
# '-.'  dash-dot line style
# ':'   dotted line style
