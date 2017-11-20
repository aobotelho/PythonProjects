'''
Based on:
'''
import RPi.GPIO as GPIO
from RPi.GPIO import HIGH as HIGH
from RPi.GPIO import LOW as LOW
import time
from random import randint
import I2C_LCD_driver

class CapacitiveTouchKeyboard():
    def __init__(self,SCLPin = 21,SDOPin = 20):
        GPIO.setmode(GPIO.BCM)
        self.SCLPin = SCLPin
        self.SDOPin = SDOPin

        self.HALF_BIT_TIME = .001
        self.CHARACTER_DELAY = 5*self.HALF_BIT_TIME
        self.NUM_BITS = 16

        GPIO.setup(self.SCLPin,GPIO.OUT)
        GPIO.setup(self.SDOPin,GPIO.IN)

        GPIO.output(self.SCLPin,HIGH)

    def checkButton(self):
        button=0
        while button < 16:
            GPIO.output(self.SCLPin,LOW)
            time.sleep(self.HALF_BIT_TIME)

            keyPressed = GPIO.input(self.SDOPin)
            if not keyPressed:
                return button + 1

            button += 1
            GPIO.output(self.SCLPin,HIGH)
            time.sleep(self.HALF_BIT_TIME)

        return None

if __name__ == '__main__':
    print('Hello!')
    buttonPressed = False
    btnPrsd = CapacitiveTouchKeyboard()
    phrasesUpper = ['Seja bem vindo!','Botelhos House']
    phrasesLower = ['16 para deletar','Insira senha','13 para confirmar']
    lcd = I2C_LCD_driver.lcd()

    enteringCode = False
    delayTime = 2
    codes = []
    
    longWait = 2
    shortWait = 0.05
    lastLen = 0
    while True:
        pressedButtons = btnPrsd.checkButton()

        if pressedButtons is not None and buttonPressed == False:
            buttonPressed = True
            if pressedButtons == 13:
                if enteringCode == False:
                    print('Entering code now')
                    delayTime = shortWait
                    enteringCode = True
                    lcd.lcd_clear()
                    lcd.lcd_display_string('Password:',1,1)
                else:
                    print('Code entered')
                    lcd.lcd_display_string('Code entered',1,1)
                    enteringCode = False
                    codes = []
                    delayTime = longWait
            elif pressedButtons == 16 and enteringCode == True:
                print('16....button pressed? {}'.format(buttonPressed))
                if len(codes) > 0 and enteringCode == True and lastLen == len(codes):
                    codes = codes[:-1]
                    print('Codes after deletion: {}'.format(codes))
                    lcd.lcd_display_string('                ',2,1)
                    strToPut = str(codes[0])
                    for index in range (len(codes)):
                        if index > 0:
                            strToPut += '-{}'.format(codes[index])
                    lcd.lcd_display_string(strToPut,2,1)
                    lastLen = len(codes)
            elif enteringCode == True and pressedButtons != 14 and pressedButtons != 15 and pressedButtons != 16 and len(codes)<5:
                codes.append(pressedButtons)
                print('Codes: {}'.format(codes))
            else:
                print('Pressed {} but it will not be used to anything'.format(pressedButtons))
        elif pressedButtons is not None and buttonPressed == True:
            #print('Waiting for user to release')
            buttonPressed == True
            delayTime = shortWait
        elif enteringCode == False:
            delayTime = longWait
            buttonPressed = False
            lcd.lcd_clear()
            str1 = phrasesUpper[randint(0,1)]
            str2 = phrasesLower[randint(0,1)]
            #print('Str1: '  + str1)
            #print('Str2: ' + str2)
            lcd.lcd_display_string(str1,1,1)
            lcd.lcd_display_string(str2,2,1)
        else:
            #print('Way down here')
            #print(len(codes))
            #print(lastLen)
            buttonPressed = False
            if len(codes) > 0 and lastLen != len(codes):
                lastLen = len(codes)
                lcd.lcd_display_string('                ',2,1)
                strToPut = str(codes[0])
                for index in range (len(codes)):
                    if index > 0:
                        strToPut += '-{}'.format(codes[index])
                lcd.lcd_display_string(strToPut,2,1)

        time.sleep(delayTime)
