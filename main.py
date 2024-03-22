import numpy as np
import matplotlib.pyplot as plt
import random
import math

a = 0
b = 1
d = 1
r = 1

x_list = np.linspace( 0, 1, 10000 )
y_list = [ math.sqrt( r**2 - ( x/10000 )**2 ) for x in range( 10000 ) ]

plt.figure( figsize = ( 10, 15 ) )

for i, j in enumerate( [ 10, 100, 1000, 10000 ], 1 ):
    plt.subplot( 1, 4, i )
    plt.plot( x_list, y_list )
    plt.title( f'N = {j}' )
    plt.xlabel( 'x' )
    plt.ylabel( 'y' )
    plt.xlim( 0, 1 )
    plt.ylim( 0, 1 )
    plt.gca().set_aspect( 'equal' )
    plt.grid( True )

    k = 0
    n = 0
    for _ in range(j):
        n += 1
        x = random.uniform( 0, r )
        y = random.uniform( 0, r )
        if y > np.sqrt( r**2 - x**2 ):
            plt.scatter( x, y, color = 'red' )
        else:
            k += 1
            plt.scatter( x, y, color = 'green' )

    pi = k / n * (b - a) * d * 4
    print( f"Wartość π dla N = {j}: {pi:.5f}" )

plt.figure( figsize = ( 10, 5 ) )

for j in [ 10000, 10000, 10000, 10000, 10000 ]:
    k = 0
    n = 0
    pi_estimations = []

    for _ in range( j ):
        n += 1
        x = random.uniform( 0, r )
        y = random.uniform( 0, r )
        if y <= np.sqrt( r**2 - x**2 ):
            k += 1

        pi = k / n * ( b - a ) * d * 4
        pi_estimations.append( pi )

    plt.plot( pi_estimations, label = f'N = {j}' )

plt.title( 'Estymacja wartości liczby π' )
plt.xlabel( 'Liczba próbek' )
plt.ylabel( 'Estymacja π' )
plt.grid( True )
plt.legend()
plt.tight_layout()
plt.show()
