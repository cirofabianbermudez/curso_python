import numpy as np
from scipy import signal
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
plt.rc('font', family='serif', size=8)

# Funcion de transferencia
alfa = 0.9
A = (1 - alfa)/(1 + alfa)
sys = signal.TransferFunction([A,1],[1,A])

w = np.logspace(-2,2,500)
w,mag,phase = signal.bode(sys,w)

# Transdormar a Hz o rad/s
freq = 'Hz'
if freq == 'Hz':
	w = w/(2*np.pi)
	xlabel = 'Frequency (Hz)'
else:
	xlabel = 'Frequency (rad/s)'


fig, axs = plt.subplots(2)
fig.subplots_adjust(hspace=0.5)

axs[0].semilogx(w, mag, label='Magnitud', linewidth=0.6)
axs[0].axis([w.min(), w.max(), mag.min(), mag.max()])
Config_graph(0, 'Bode Diagram', xlabel, 'Magnitud (dB)')

axs[1].semilogx(w, phase, label='Phase', linewidth=0.6)
axs[1].axis([w.min(), w.max(), phase.min(), phase.max()])
Config_graph(1, '', xlabel, 'Phase (deg)')

# Mostrar Grafica
plt.show()

# Guardar la grafica como eps, png, es necesario comentar plt.show()
# plt.savefig('graph_name.eps')

# Problema 1
# num = np.poly1d([200,0])
# p1 = np.poly1d([1,2])
# p2 = np.poly1d([1,10])
# den = p1*p2