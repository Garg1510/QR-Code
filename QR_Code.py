# importing the qrcode module  
# import pyqrcode
import qrcode
import cv2
import numpy as np
import qrcode
from PIL import Image
# creating a QRCode object  
obj_qr = qrcode.QRCode(  
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)  
# using the add_data() function  
obj_qr.add_data("https://www.javatpoint.com/python-tutorial")  
# using the make() function  
obj_qr.make(fit = True)  
# using the make_image() function  
img = obj_qr.make_image(fill_color="black", back_color="white").convert('RGB')
# saving the QR code image  
img.save("qr-img1.png")  
# importing the OpenCV library  

# reading the image 
# using the QRCodeDetector() function 
# using the detectAndDecode() function 
# qr_img = cv2.imread('qr-img1.png')  
 
# qr_det = cv2.QRCodeDetector()  
  
# val, pts, st_code = qr_det.detectAndDecode(qr_img)  

 

qr_im = cv2.imread("qr-img1.png")
qr_det = cv2.QRCodeDetector()
retval, points, straight_qrcode = qr_det.detectAndDecode(qr_im)
print("Information:", retval) 
# retval, decoded_info, points, straight_qrcode = qr_det.detectAndDecodeMulti(np.hstack([qr_im, qr_im]))
# print(decoded_info)