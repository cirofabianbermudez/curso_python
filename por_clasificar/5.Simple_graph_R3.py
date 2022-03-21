# Simple graph in 3D

# Librerias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Fuente de la grafica
plt.rc('font', family='serif')    # garamong, serif, arial

# Tamaño de letra de los ejes
plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)

# Parametros de vectores
inicio = -6
paso = 0.05
fin = 6 + paso

# Vectores para generar grafica
x = np.arange(inicio, fin, paso)
y = np.arange(inicio, fin, paso)
X,Y = np.meshgrid(x,y)
# Z = np.maximum(X,Y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

# Generar grafica
fig = plt.figure()
ax = fig.gca(projection='3d')

# graph = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')		# 'binary' 'viridis'
ax.set_title('Función máximo');
ax.set_xlabel('Valores de verdad X')
ax.set_ylabel('Valores de verdad Y')
ax.set_zlabel('Función evaluada')
ax.view_init(20, -45)

# Mostrar la grafica
plt.show()

# Guardar la grafica como eps, png
# plt.savefig('graph_name.png')

