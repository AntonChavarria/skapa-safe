import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(24, GPIO.OUT)#BUZZER
GPIO.setup(22, GPIO.IN)#BOTON
GPIO.setup(26, GPIO.OUT)#LED

GPIO.output(26, False)

flag = True
con = 0



try:
    while flag:
        input_state = GPIO.input(22) #estado del boton
        
        if input_state == True: #Boton presionado
            GPIO.output(26, True)
            print('Boton presionado')
            cont = 0
            while cont <= 6:
                GPIO.output(24, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(24, GPIO.LOW)
                time.sleep(0.5)
                cont = cont + 1
            
            GPIO.output(26, False)
            
        if con >=2:
            flag = False
            
except KeyboardInterrupt:
    GPIO.cleanup()

 
GPIO.output(24, GPIO.LOW)
GPIO.cleanup()
