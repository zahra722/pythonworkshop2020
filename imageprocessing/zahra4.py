import cv2

img = cv2.imread("galaxy.jpg",0)
img1 =["galaxy1.jpeg","galaxy2.jpeg","galaxy3.jpeg","galaxy4.jpeg","galaxy5.jpeg","galaxy6.jpeg","galaxy7.jpeg","galaxy8.jpeg","galaxy9.jpeg","galaxy10.jpeg",1]


print(img)
print(type(img))
print(img.shape)
print(img1.shape)
print(img.ndim)
print(img1.ndim)

cv2.imshow("ANTARISHQ",img1)
cv2.waitKey(2000)
cv2.destroyALLWindows

resize_img = cv2.resize(img,(590,350))
cv2.imshow("newIMAGE",resize_img)
cv2.waitKey(2000)
for i in img1:
    i =cv2.imread(i,1) 
    r_img = cv2.resize(i,(int(i.shape[1]/2),int(i.shape[0]/2)))
    cv2.imshow("nm",r_img)
    cv2.waitKey(2000)

    cv2.imwrite("nm_resize.jpeg",r_img)
