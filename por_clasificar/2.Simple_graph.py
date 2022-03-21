# Simple graph

# Librerias
import numpy as np
import matplotlib.pyplot as plt

# Fuente de la grafica
plt.rc('font', family='serif')    # garamong, serif, arial

# Tamaño de letra de los ejes
plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)

# Parametros de vectores
inicio = 0
paso = 0.1
fin = 2 * np.pi + paso

# Vectores para generar grafica
x = np.arange(inicio, fin, paso)
y = np.sin(x)
plt.plot(x, y, label=r'sin x', linewidth=0.6)

# Nombres de ejes y legenda
plt.xlabel(r'Time (s)', size=10)
plt.ylabel(r'Voltage (V)', size=10)
plt.legend(shadow=True, loc='upper right', fontsize='small')

# Configuraciones de Grid
plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.4)
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.2)

# Cambiar los limites de los ejes
plt.axis([x.min(), x.max(), y.min(), y.max()])

# Titulo de la grafica
plt.title(r'f(x) = sin(x)', size=10)      # Add an r Raw String Literal

# Mostrar la grafica
plt.show()

# Guardar la grafica como eps, png, es necesario comentar show()
# plt.savefig('graph_name.eps')

# Tipos de letra extras 
# garamong, serif, arial

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