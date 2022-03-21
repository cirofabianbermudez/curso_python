import pandas as pd
from itertools import product

# Boolean Equation
def f(C,B,A):
    return (A or B) and not C

# product() Producto cartesiano 
# list()	Convierte a lista 
def truth_table(f):
	values = [list(x) + [int(f(*x))] for x in product([0,1], repeat=f.__code__.co_argcount)]
	return  pd.DataFrame(values, columns=(list(f.__code__.co_varnames) + [f.__name__]) )

data = truth_table(f); print(data)

# Save in csv
data.to_csv('Truth_table.csv',sep=',')

