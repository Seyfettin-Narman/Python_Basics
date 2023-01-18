import pyautogui
pyautogui.moveTo(799,466,duration=2,tween=pyautogui.easeInOutQuad)
pyautogui.click()
for k in range(1000):
    pyautogui.write("evet!",interval=0.001)
    pyautogui.press('enter')

