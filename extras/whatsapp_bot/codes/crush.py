import pyautogui, webbrowser
from time import sleep

enable = True
possible_numbers = []

# generar numeros de telefono
for x in range(10):
    for y in range(10):
        possible_numbers.append("5123"+str(x)+"12"+str(y)+"04")

print("POSSIBLE NUMBERS")
for numbers in possible_numbers:
    print(numbers)

# Enviar mensajes de whatsapp
if enable:
    message = "Hola, tu eres la chica que encontre ayer en el bar?"
    for number in possible_numbers:
        webbrowser.open("https://web.whatsapp.com/send?phone=+52"+number)
        sleep(10)
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        sleep(10)



