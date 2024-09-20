import numpy as np
x = np.array([1,2,3],dtype=np.float32)
# print(x)

# we show how to compute the elementwise
#  sine using Numpy
# print(np.sin(np.array([1,2,3],dtype=np.float32) ))

# Otherwise, we would have to do looping explicitly as in the following
from math import sin
# print([sin(i) for i in [1,2,3]])


# two-dimensional 2x3 array constructed from two conforming Python lists.
x=np.array([ [1,2,3],[4,5,6] ])
# print(x.shape)

# Numpy
# arrays follow the usual Python slicing rules in multiple dimensions as shown below
# where the : colon character selects all elements along a particular axis
def slice():   
    x=np.array([ [1,2,3],[4,5,6] ])
    print("1 is ",x[:,0]) 
    print("2 is ",x[:,1]) #[2,5]
    print("3 is ",x[0,:])
    print("4 is ",x[1,:])
    print("5 is ",x[:,:]) #[456] -  >>[[23][56]]  - 
    print("6 is ",x[:, : : 2]) # range(4,10,-1) =[9,8,7,6,5,4]
    print("7 is ",x[:,::-1])
# slice()
# --------------
def arraysCalls():
    # Numpy Array and Memory
    # Numpy uses pass-by-reference
    # x = np.ones((3,3))
    x=np.array( [[1,2,3],
    [4,5,6],
    [7,8,9]])
    y=x[:2,[0,1]] #x[:,0:3]
    print(f' the y is {y}')
    # the variable y has 
    # its own memory because the relevant parts of x were copied. 
    # x[0,0]=999
    # print(x, y)
    # x = np.ones((3,3))
    y = x[:2,:2]
    x[0,0] = 999
    # print(x,y)
# arraysCalls()
# ----------------------------
def forceCopy():
    # Note that if you want to explicitly force a copy without 
    # any indexing tricks, you can do y=x.copy(). 
    # The code below works through another example of advanced
    # indexing versus slicing.
    x = np.arange(5)
    y=x[[0,1,2]] # index by integer list to force copy
    z=x[:3]     # slice creates view
    print(x,y,z,"\n")
    x[0]=999
    print(x,y,z)

# --------------------------
# Numpy Matrice

#  how to create two matrices and multiply them
A=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
x=np.matrix([[1],[0],[0]])
# print(A*x)

# Another Way by array
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.array([[1],[0],[0]])
# print(A.dot(x))



# -------------------------
# Numpy broadcasting
# It is a powerful feature in the Numpy library of Python that allows 
# you to perform operations on arrays of different shapes and sizes, without having 
# to explicitly reshape or duplicate the arrays.
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
# Broadcasting: Adding a 1-dimensional array to a 2-dimensional array
result = a + b
# print(result)

# ------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def MeshGridD():
    # Meshgrid+++ is used to create a grid of coordinates from two one-dimensional arrays. 
    # This is commonly used when you want to evaluate a function on a grid of points.

    # This function takes multiple one-dimensional arrays as input and returns a meshgrid. 
    # A meshgrid is a 2D array where each element is a pair of coordinates representing
    # a point on a grid.

    # x,y=np.meshgrid(np.arange(3),np.arange(2))
    # # print(x,y)

    x = np.array([1, 2]) #x axis
    y = np.array([10, 20,30]) #y axis    (1,1o) (1,20) (1,30 ) (2,1o) (2,20) (2,30 )
    X, Y = np.meshgrid(x, y)
    print(X , "\n") 
    print(Y)

def MeshGridEXM():
    # EXAMPLE

    x_vals = np.linspace(-5, 5, 100)
    y_vals = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x_vals, y_vals)
    # print ('xvalues i', x_vals,'x', x)
    # print ('yvalues',y_vals ,'y',y)
    # Calculate the values of the function at each point in the grid
    z = np.sin(np.sqrt(x*2 + y*2))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    
    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot of f(x, y) = sin(sqrt(x^2 + y^2))')
    plt.show()
MeshGridEXM()
# MeshGridEXM()
# TASK [0]
# Problem: Analyzing Temperature Distribution Across a Wall

# You have a wall made of a metallic material inside a room. 
# The temperature distribution across this wall 
# is influenced by various factors, including its thermal conductivity, 
# thickness, and heat generation.

# The wall is represented as a two-dimensional matrix, where each cell corresponds to a specific location on the wall. Your task is to create a Python program that visualizes the temperature distribution across the wall based on the following parameters:
# The thermal conductivity of the wall material is represented by 
# the coefficient K.
# The thickness of the wall is represented by L.
# The heat generation rate within the wall is denoted by G.
# The heat at both surfaces of the wall is represented by Tw.

# to calculate the temperature in each poin by the following

# Use Python to create a graphical representation 
# that shows the temperature distribution across the wall by 3D view

# ----------------------pandas-----------------------------------
# ======================pandas===================================
# ++++++++++++++++++++++pandas+++++++++++++++++++++++++++++++++++

#1-Series: There are two primary data structures in Pandas. 
# The first is the Series object which combines an index 
# and corresponding data values
import pandas as pd
x=pd.Series(index = range(5),data=[1,3,9,11,12])
# print(x)

# The main thing to keep in mind with Pandas is that these data 
# structures were originally designed to work with time-series data. 
# In that case, the index in the data
# structures corresponds to a sequence of ordered time stamps. 
# In the general case, the
# index must be a sort-able array-like entity. For example,
x=pd.Series(index = ['a','b','d','z','z'],data=[1,3,9,11,12])
# Note the duplicated z entries in the index. We can get at the entries 
# in the Series in a number of ways. First, we can used the dot 
# notation to select as in the following:
x.a
x.z
# We can also use the indexed position of the entries with 
# iloc as in the following:
x.iloc[:3]
# which uses the same slicing syntax as Numpy arrays. 
# You can also slice across the index, even if it is not numeric 
# with loc as in the following
x.loc['a':'d']
x['a':'d']

# the main power of Pandas comes from its power to aggregate and
# group data
x = pd.Series(range(5),[1,2,11,9,10])
grp=x.groupby(lambda i:i%2) # odd or even
grp.get_group(0) # even group
grp.get_group(1) # odd group
# 2-Dataframe
# The Pandas DataFrame is an encapsulation of the Series that extends 
# to two dimensions. One way to create a DataFrame is with 
# dictionaries as in the following
df = pd.DataFrame({'col1': [1,3,11,2], 'col2': [9,23,0,2]})
# Note that the keys in the input dictionary are now the column 
# headings (labels) of the DataFrame
# We can extract elements from each column using the iloc method
df.iloc[:2,:2]# get section
# or by directly slicing or by using the dot notation as shown below
df['col1'] # indexing
df.col1 # use dot notation
# Subsequent operations on the DataFrame preserve its column-wise structure as in
# the following:
df.sum()
# Grouping and aggregating with the dataframe is
# even more powerful than with Series
df = pd.DataFrame({'col1': [1,1,0,0], 'col2': [1,2,3,4]})
grp=df.groupby('col1')
grp.get_group(0)
grp.get_group(1)
grp.sum()
# The Dataframe can compute new columns based on existing columns using the
# eval method as shown below
df['sum_col']=df.eval('col1+col2')


# ----------------------Sympy-----------------------------------
# ======================Sympy===================================
# ++++++++++++++++++++++Sympy+++++++++++++++++++++++++++++++++++

# Sympy [5] is the main computer algebra module in Python. 
# It is a pure-Python package with no platform dependencies
import sympy as sym
from sympy import expand

# x = sym.Rational(1, 2)
# print(x)

# evalf evaluates the expression to a floating-point number
# print(sym.pi.evalf())

#  class representing mathematical infinity, called oo:
# print(sym.oo > 999999999)
# print(sym.oo + 1)

# In contrast to other Computer Algebra Systems, in SymPy you have to declare symbolic 
# variables explicitly:
x=5
# print(x)
# x = sym.symbols('x')
# print(x)
# p=sum(x**i for i in range(3)) # 2nd order polynomial
# print(p)

# x = sym.Symbol('x')
# y=sym.Symbol('y')
# print(x + y + x - y)
# print((x + y) ** 2)

# ---------
# SymPy is capable of performing powerful algebraic manipulations. 
# We'll take a look into some of the most frequently used: 
# expand and simplify.

# print (sym.expand((x+y)**3))
# print (sym.expand(sym.cos(x + y), trig=True))
# print(sym.trigsimp(sym.sin(x)*2 + sym.cos(x)*2))

# Use simplify if you would like to transform an expression into a simpler form:
# print(sym.simplify((x + x * y) / x))

# Limits are easy to use in SymPy, they follow the syntax limit(function, variable, point), so to compute the limit of f(x) as x 
# \rightarrow 0, you would issue limit(f, x, 0):
# print(sym.limit(x, x, sym.oo))
# print(sym.limit(sym.sin(x) / x, x, 0))
# print(sym.limit(1 / x, x, sym.oo))

# # You can differentiate any SymPy expression using diff(func, var):
# print (sym.diff(sym.sin(x), x))
# print(sym.diff(sym.sin(2 * x), x))
# print(sym.diff(x**2,x))

# print(sym.diff(x**3,x,1))
# print(sym.diff(x**3,x,2))
# print(sym.diff(x**3,x,3))

# SymPy has support for indefinite and definite integration of transcendental elementary 
# and special functions via integrate() facility

# print (sym.integrate(6 * x ** 5, x))
# ----------------------------------

# def calculate_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# result = calculate_sum(1000000)
# print(result)