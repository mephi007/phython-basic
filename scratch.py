import  pyautogui, time

time.sleep(5)

print ("enter CTRL + C to interrupt")

try :
    x, y = pyautogui.position()
    pos =  'X : ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4)
    print (pos , end= ' ')



except KeyboardInterrupt:
    print ("\n done")