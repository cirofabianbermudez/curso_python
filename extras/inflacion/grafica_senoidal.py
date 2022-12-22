import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#plt.rc( {'text.usetex': True, 'font.family': 'serif'}  )

plt.plot(x,y,'k', linewidth=1.0, label=r'$f(x) = \sin x$')

plt.title(r'Función senoidal', size=12) 
plt.ylabel(r'Inflación')
plt.xlabel(r'Años')
plt.legend()
plt.axis([0, 2*np.pi, -1, 1])
#plt.axhline(y=0, color="black", linestyle="--", linewidth=1.0)

plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.4)
plt.grid(visible=True, which='minor', color='#999999', linestyle='--', alpha=0.2)
plt.minorticks_on()  


plt.savefig('test.pdf')

#plt.show()
#step = 0.02
#a = np.arange(0, 3+step, step)
