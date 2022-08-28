import cv2
import pygame

pygame.init()

width, height = 700, 700

win = pygame.display.set_mode((width, height))

cam = cv2.VideoCapture(0)



color = (255, 0, 0)

def detect(frame, x, y, color):
    cv2.circle(frame, (x, y), 5, color, 3)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    d = hsv_frame[x, y]
    a = d[0] #h
    b = d[1] #s
    c = d[2] #v

    #geel vanboven en groen vooraan

    if b < 0 and b > 46 and c < 176 and c > 98:
        return 'D' #wit

    elif a < 5 and a > 0 and b < 212 and b > 111 and c < 255 and c > 153:
        return 'R' #orangje

    elif a < 179 and a > 155 and b < 211 and b > 150 and c < 255 and c > 70:
        return 'L' #red

    elif a < 75 and a > 56 and b < 255 and b > 151 and c < 255 and c > 68:
        return 'U' #geel

    elif a < 37 and a > 24 and b < 196 and b > 96 and c < 255 and c > 119:
        return 'B' #blue

    elif a < 111 and a > 102 and b < 255 and b > 185 and c < 255 and c > 119:
        return 'F' #groen

    else:
        return 'R'

b11r = pygame.rect.Rect(200, 200, 100, 100)
b21r = pygame.rect.Rect(400, 200, 100, 100)
b31r = pygame.rect.Rect(600, 200, 100, 100)
b12r = pygame.rect.Rect(200, 400, 100, 100)
centerr = pygame.rect.Rect(400, 400, 100, 100)
b32r = pygame.rect.Rect(600, 400, 100, 100)
b13r = pygame.rect.Rect(200, 600, 100, 100)
b23r = pygame.rect.Rect(400, 600, 100, 100)
b33r = pygame.rect.Rect(600, 600, 100, 100)

def convert(v):
    if v == 'D':
        return (255, 255, 255)
    elif v == 'R':
        return (255, 0, 0)
    elif v == 'L':
        return (255, 145, 0)
    elif v == 'U':
        return (255, 255, 0)
    elif v == 'B':
        return (0, 255, 0)
    elif v == 'F':
        return (0, 0, 255)



while True:
    _, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    b11 = detect(frame, 150, 100, color)
    b21 = detect(frame, 300, 100, color)
    b31 = detect(frame, 450, 100, color)

    b12 = detect(frame, 150, 250, color)
    b32 = detect(frame, 450, 250, color)

    b13 = detect(frame, 150, 400, color)
    b23 = detect(frame, 300, 400, color)
    b33 = detect(frame, 450, 400, color)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

    r = pygame.draw.rect(win, convert(b11), b11r)
    r = pygame.draw.rect(win, convert(b11), b21r)
    r = pygame.draw.rect(win, convert(b11), b31r)
    r = pygame.draw.rect(win, convert(b11), b12r)
    r = pygame.draw.rect(win, convert(b11), centerr)
    r = pygame.draw.rect(win, convert(b32), b32r)
    r = pygame.draw.rect(win, convert(b13), b13r)
    r = pygame.draw.rect(win, convert(b23), b23r)
    r = pygame.draw.rect(win, convert(b33), b33r)
    pygame.display.update()

cv2.destroyAllWindows()
cam.release()