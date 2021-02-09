import pylab
import matplotlib.pyplot as plt


import PDI_Trabalho_3_Func as func
img = pylab.imread("guitarra.jpg")
img_gray = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]
print(img_gray.shape)

img_gray = func.contraste(1,img_gray,0.005) # 1 =LINEAR, 2 = EXPONENCIAL, 3 =LOGARÍTIMO
img_gray = func.filtro(1,img_gray) #1=MEDIANA, 2 = GAUSSIANO
img_gray = func.limiarizacao(2,img_gray) #1 =GLOBAL, 2 =LOCAL
img_gray = func.bordas(1,img_gray) #1=ROBERTS, 2 = PREWIT
print(img_gray.shape)
pylab.imshow(img_gray,pylab.cm.gray)
plt.show()
