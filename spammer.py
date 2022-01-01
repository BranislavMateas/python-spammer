import pyautogui, time
time.sleep(2)
f = open("d:/Rýchly prístup/Desktop/Nový priečinok/vec.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")