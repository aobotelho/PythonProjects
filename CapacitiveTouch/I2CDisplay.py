import I2C_LCD_driver
from time import sleep

lcdi2c = I2C_LCD_driver.lcd()

lcdi2c.lcd_display_string('This is a test',1,1)

counter = 0
while counter < 20:
    lcdi2c.lcd_display_string('Loop: {}'.format(str(counter)),2,1)
    sleep(1)
    counter += 1