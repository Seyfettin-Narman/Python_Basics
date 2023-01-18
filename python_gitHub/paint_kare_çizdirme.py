import pyautogui
pyautogui.moveTo(100,200,duration=2,tween=pyautogui.easeInOutQuad)
mesafe=150
while mesafe>0:
    pyautogui.drag(mesafe,0,duration=0.5)
    mesafe-=5
    pyautogui.drag(0,mesafe,duration=0.5)
    pyautogui.drag(-mesafe,0,duration=0.5)
    mesafe-=5
    pyautogui.drag(0,-mesafe,duration=0.5)
