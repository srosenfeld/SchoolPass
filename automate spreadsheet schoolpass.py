import pyautogui as pg
from time import sleep
import os



hello = os.startfile("C:\\Users\\srosenfeld\\Desktop\\Untitled.xlsx")

sleep(5)

pg.hotkey('Ctrl','g')

## Type "H:AZ"
sleep(3)
pg.typewrite('H:AZ')
sleep(1)
pg.hotkey('enter')

## Press Ctrl + G
pg.hotkey('Ctrl','g')
sleep(1)

## Press Alt + S
pg.hotkey('alt','s')
sleep(2)

## Press Alt + k
pg.hotkey('alt','k')
sleep(2)
pg.hotkey('enter')
sleep(2)

## Press Ctrl + -
pg.hotkey('ctrl','-')
sleep(2)

## Press Alt + L, then enter
pg.hotkey('alt','L')
sleep(2)
pg.hotkey('enter')
sleep(2)


