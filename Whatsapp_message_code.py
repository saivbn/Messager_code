import pyautogui
import time
import webbrowser
import pyperclip

x = 10
phone_number = "+919876543251"
message = "Hello Git"
webbrowser.open(f"https://web.whatsapp.com/send?phone={+919876543251}")
count = x
time.sleep(1)

for i in range (count):
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(0)

print("message sent succesfullly")
