import cv2
import numpy as np

#içe aktar
img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)

width = 400
height = 500

pts1 = np.float32([[230,1], [1,472],[540,150], [338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
"""cv2.getPerspectiveTransform() fonksiyonu, perspektif dönüşüm matrisini hesaplar. 
Bu matris, orijinal görüntüdeki dört köşe noktasını dönüştürülmüş görüntüdeki hedef köşe noktalarına eşleştirir. 
Matris, perspektif dönüşümü temsil eder ve bu işlemi gerçekleştirmek için kullanılır."""
print(matrix)

#nihai dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Yeni", imgOutput)
"""" cv2.warpPerspective() fonksiyonu, perspektif dönüşümü uygular. 
Orijinal görüntü (img), önceden hesaplanan dönüşüm matrisi (matrix) ve hedef boyut (width ve height) kullanılarak dönüştürülmüş bir görüntü (imgOutput) elde edilir. 
Bu dönüştürülmüş görüntü, "Yeni" adında bir pencerede görüntülenir."""