import cv2
import numpy as np

def count_objects():
    image = cv2.imread('d:/Maria_iti/day 10/2.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    num_obj = len([cnt for cnt in contours if cv2.contourArea(cnt) > 95])
    
    return num_obj

print(f"Number of objects: {count_objects()}")
