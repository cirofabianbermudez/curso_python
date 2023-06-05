import pyautogui, webbrowser
from time import sleep

template = "5123*12*04"
enable = True
possible_numbers = ["2225871482", "2223694664"]


# Enviar mensajes de whatsapp
if enable:
    message = "Que onda"
    for number in possible_numbers:
        webbrowser.open("https://web.whatsapp.com/send?phone=+52"+number)
        sleep(10)
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        sleep(10)



