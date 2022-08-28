import cv2

a = cv2.VideoCapture(0)

while True:
    cv2.imshow('cube', a)