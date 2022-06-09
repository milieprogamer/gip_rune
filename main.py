import cv2
import pygame

pygame.init()

width, height = 700, 700

win = pygame.display.set_mode((width, height))

cam = cv2.VideoCapture(1)

color = (255, 0, 0)

def detect(frame, x, y, color):
    cv2.circle(frame, (x, y), 5, color, 3)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    d = hsv_frame[x, y]
    a = d[0]
    b = d[1]
    c = d[2]
    if b < 10 and c > 50:
        return 'D'
    elif a < 10:
        return 'R'
    elif a < 50:
        return 'L'
    elif a < 75:
        return 'U'
    elif a < 175:
        return 'B'
    elif a < 300:
        return 'F'
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
        return (0, 0, 255)
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
    r = pygame.draw.rect(win, convert(b11), b11r)
    r = pygame.draw.rect(win, convert(b11), b11r)
    r = pygame.draw.rect(win, convert(b11), b11r)
    r = pygame.draw.rect(win, convert(b11), b11r)
    r = pygame.draw.rect(win, convert(b32), b11r)
    r = pygame.draw.rect(win, convert(b13), b11r)
    r = pygame.draw.rect(win, convert(b23), b11r)
    r = pygame.draw.rect(win, convert(b33), b11r)
    pygame.display.update()

cv2.destroyAllWindows()
cam.release()