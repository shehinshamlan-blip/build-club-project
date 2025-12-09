import os.path
import cv2

path=input("enter image path :").strip()#input image path here(wowo.jpg)

img = cv2.imread(path)  #give path of image here

if img is None: #in case user didn't give any image
    print("error image not found!!!!")
    exit()

img_name=os.path.splitext(os.path.basename(path))[0]#to get the name of image without extension

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert to gray

smooth_image = cv2.medianBlur(gray, 7) #Smooth the image

#Detect edges
edges = cv2.adaptiveThreshold(   smooth_image, 255,  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9, 9)

# cartoon-style color
pre_image= cv2.bilateralFilter(img, d=9, sigmaColor=200, sigmaSpace=200)

#  Combine color image with edges
cartoon = cv2.bitwise_and(pre_image,pre_image, mask=edges)

# Show result
cartoon_img_name=("cartoon_"+path+".jpg")
cv2.imshow("Original", img)
cv2.imshow(cartoon_img_name, cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result
cv2.imwrite(cartoon_img_name, cartoon)


