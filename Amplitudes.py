# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math

# Probabilidad de observación
def probabilidad (v1,a):
    resultado = ((lc.modulo(v1[a][0]))**2 )/(vc.normaVector(v1)**2)
    return resultado

