import pylab
import numpy as np
import scipy
import scipy.signal
from skimage import filters

def contraste(P,vec,K):
    ####>>>AJUSTE DE CONTRASTE<<<####
    a, b = vec.shape
    limite1 = 100
    limite2 = 200
    if P == 1:
        ####LINEAR####
        for k in range(a):
            for i in range(b):
                if vec[k, i] < limite1:
                    vec[k, i] = vec[k, i] * 1
                else:
                    if vec[k, i] >= limite1 and vec[k, i] <= limite2:
                        vec[k, i] = vec[k, i] * 1.5
                    else:
                        vec[k, i] = vec[k, i] * 0.8
    ####EXPONENCIAL###
    else:
        if P == 2:
            for k in range(a):
                for i in range(b):
                    vec[k, i] = 255 * np.log2(K * vec[k, i] + 1) / (np.log2(K * (255) - 1))
        ####LOGARÍTIMO####
        else:
            if P == 3:
                for k in range(a):
                    for i in range(b):
                        vec[k, i] = 255 * ((2 ** (K * vec[k, i]) - 1) / (2 ** (K * (vec[k, i] - 1)) - 1))

    return vec



def filtro(P,vec):
    if P==1:
        filtromediana = scipy.ones((3, 3)) / 9
        filtromediana = scipy.signal.convolve2d(vec, filtromediana, mode='same')
        filtro = scipy.uint8(filtromediana)
    ####GAUSSIANO#####
    else:
        filtro = scipy.ndimage.gaussian_filter(vec, 2)
    return filtro




def limiarizacao(P,vec):
    a, b = vec.shape
    intervalos = 10 #quanto maior menor  a janela
    if P==1:
        media = np.mean(vec)
        for k in range(a):
            for i in range(b):
                if vec[k,i]<=media:
                    vec[k,i] = 0
                else:
                    vec[k,i] = 255
    else:

        for k in range(intervalos):
            for i in range(intervalos):
               media = np.mean(vec[k*int(a/intervalos):(k+1)*int(a/intervalos),i*int(b/intervalos):(i+1)*int(b/intervalos)])
               for p in range(int(a/intervalos)):
                   for c in range(int(b/intervalos)):
                       if vec[k*int(a/intervalos)+p,i*int(b/intervalos)+c] < media:
                           vec[k * int(a / intervalos) + p, i * int(b / intervalos) + c] = 0
                       else:
                           vec[k * int(a / intervalos) + p, i * int(b / intervalos) + c] = 255


    return vec

def bordas(P,vec):
    if P ==1:
        vec = filters.roberts(vec)
    else:
        vec = filters.prewitt(vec)
    return vec