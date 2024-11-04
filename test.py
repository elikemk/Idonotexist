import cv2 #make sure you have opencv installed 


print(cv2.__version__)

img = cv2.imread('00001.png', 1) #shows the image in black and white

print(img) 
cv2.imshow('image', img) 
cv2.waitKey(5000) #wait of x amount of seconds
cv2.destroyAllWindows() #delete the window after 
