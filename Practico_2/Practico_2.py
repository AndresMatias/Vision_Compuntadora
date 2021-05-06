import cv2
img=cv2.imread('hojas.jpg',0)
umbral=155
for i,row in enumerate(img) :
	for j,col in enumerate(row):
		if col > umbral:
			img[i][j]=255
		else:
			img[i][j]=0	
cv2.imwrite('Resultado.jpg',img)

			