import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('indicadores.csv', encoding = 'utf-16le', skiprows=4)
df.rename(columns={'583753': 'Inflacion'}, inplace=True)
df['Periodos'] = pd.to_datetime(df['Periodos'])


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#plt.figure(figsize = (6.8, 4.8))
plt.locator_params(axis='y', tight= True,nbins=10)
plt.plot( df['Periodos'], df['Inflacion'] ,'k', linewidth=1.0, label=r'1970/01 a 2022/02')
plt.title(r'Inflación de 1970/01 a 2022/02', size=12) 
plt.ylabel(r'Inflación')
plt.xlabel(r'Años')
plt.legend()
plt.axis([ df.loc[0,'Periodos'] , df.loc[625,'Periodos'] , 0, max( df['Inflacion']*1.05 ) ])

idx1 = df['Inflacion'].idxmax()
p1 = [df.loc[idx1,'Periodos_new'],df.loc[idx1,'Inflacion']]
text1 = str(df.loc[idx1,'Periodos']) + ', ' +  str(df.loc[idx1,'Inflacion']) 
plt.annotate(text1,xy=p1, arrowprops=dict(arrowstyle='->'), xytext=(df.loc[idx1-120,'Periodos_new'], p1[1]-1), fontsize=6 )

plt.grid(visible=True, which='major', axis='both', color='#dedede', linestyle='-', alpha=0.4)
plt.grid(visible=True, which='minor', axis='y', color='#c5c5c5', linestyle=':', alpha=0.2)
plt.minorticks_on()  

plt.savefig('inflacion2.pdf')

#plt.show()

#x = np.linspace(0,2*np.pi,100)
#y = np.sin(x)

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#plt.rc( {'text.usetex': True, 'font.family': 'serif'}  )

#plt.plot(x,y,'k', linewidth=1.0, label=r'$f(x) = \sin x$')

#plt.title(r'Función senoidal', size=12) 
#plt.ylabel(r'Inflación')
#plt.xlabel(r'Años')
#plt.legend()
#plt.axis([0, 2*np.pi, -1, 1])
#plt.axhline(y=0, color="black", linestyle="--", linewidth=1.0)

#plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.4)
#plt.grid(visible=True, which='minor', color='#999999', linestyle='--', alpha=0.2)
#plt.minorticks_on()  


#plt.savefig('test.pdf')

#plt.show()
#step = 0.02
#a = np.arange(0, 3+step, step)
