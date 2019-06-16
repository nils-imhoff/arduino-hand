import serial
import pyautogui

Arduino_Serial = serial.Serial('com12',9600)

while 1:
incoming_data = str (Arduino_Serial.readline())
print incoming_data


if 'next' in incoming_data:
pyautogui.press(left)

if 'previous' in incoming_data:
pyautogui.press(right)

if 'down' in incoming_data:
#pyautogui.press('down')
pyautogui.scroll(-100)

if 'up' in incoming_data:
#pyautogui.press('up')
pyautogui.scroll(100)

if 'change' in incoming_data:
pyautogui.typewrite(['space'],0.2)
incoming_data = "
