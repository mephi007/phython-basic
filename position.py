import  pyautogui , time


time.sleep(10)
pyautogui.click()
distance = 300
while  distance>0 :
    pyautogui.dragRel(distance, 0 , duration = 0.2)
    distance = distance-5
    pyautogui.dragRel(0, distance, duration= 0.25)
    pyautogui.dragRel(-distance, 0 , duration= 0.25)
    distance = distance - 5
    pyautogui.dragRel(0, - distance, duration= 0.25)

