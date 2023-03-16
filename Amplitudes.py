# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math
v1 = [[[-2,-1]],[[0,-2]],[[0,1]],[[2,0]]]
# Probabilidad de observación
# 1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
def probabilidad (v1,a):
    resultado = ((lc.modulo(v1[a][0]))**2 )/(vc.normaVector(v1)**2)
    return resultado

# 2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
v2 = [[[-3,-1]],[[0,-2]],[[0,1]],[[2,0]]]
def probabilidad_transicion(v1,v2):
    # normalizar los vectores
    resultado = vc.productoEscalar_Vector(v1,(1/vc.normaVector(v1),0))
    #vn1 = vc.productoEscalar_Vector(1/vc.normaVector(v1),v1)
     #vn2 = v2/vc.normaVector(v2)
    #resultado = vc.productoInterno_Vector(vc.adjunta_Matriz_Vector(vn1),vn2)
    return resultado

if __name__ == '__main__':
    #print(probabilidad(v1,2))
    print(probabilidad_transicion(v1,v2))