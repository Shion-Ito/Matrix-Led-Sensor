#!/usr/bin/env python
from samplebase import SampleBase

# Shion Ito and Aarish Brohi
import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import matplotlib.pyplot as plt
# Software SPI configuration:
CLK = 11
MISO = 9
MOSI = 10
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
voltage = []
voltage2 = []
pastTime = []
timeStamps = []
startTime = time.time()
passedTime = 0.0
currentTime =[]



import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

GPIO.setwarnings(False)

class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        signalRecieved = False
        while True:
            continuum = 0
            VoltageChannel = mcp.read_adc(0)
            VoltageChannel2 = mcp.read_adc(1)
            if VoltageChannel > 300:
                signalRecieved = True
                for x in range(0, self.matrix.width):
                    offset_canvas.SetPixel(x, x, 255, 255, 255)
                    offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

                for x in range(0, offset_canvas.width):
                    offset_canvas.SetPixel(x, 0, 255, 0, 0)
                    offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

                for y in range(0, offset_canvas.height):
                    offset_canvas.SetPixel(0, y, 0, 0, 255)
                    offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
                
                top = 0
                left = 0
                bottom = self.matrix.width
                right = self.matrix.height
                half = int(right / 2)
                half2 = int(right / 2)
                for i in range(top , bottom):
                    for j in range(half, half2):
                        offset_canvas.SetPixel(j, i, 124,12,124)
                    half -= 1
                    half2 += 1
                    if(half == left or half2 == right):
                        break

                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                print("printing on led board")
                
                
            if VoltageChannel2 > 300:
                signalRecieved = True
                index = 0
                index2 = 0
                index3 = 0
                colUp = 0
                rowLeft = 0
                colBottom = offset_canvas.width
                rowRight = offset_canvas.height
                while(rowLeft < rowRight and colUp < colBottom):
                    # Start from upleft corner of current loop, go right
                    for i in range(rowLeft, rowRight):
                        if(index < 255):
                            offset_canvas.SetPixel(colUp,i, index, 0, 0)
                            index += 2
                        elif(index2 <= 255):
                            offset_canvas.SetPixel(colUp,i, 0, index2, 0)
                            index2 += 2
                        else: 
                            offset_canvas.SetPixel(colUp,i, 0, 0, index3)
                            index3 += 2

                    # from righttop go down
                    for i in range(colUp + 1, colBottom):
                        if(index < 255):
                            offset_canvas.SetPixel(i,rowRight - 1, index, 0, 0)
                            index += 2
                        elif(index2 <= 255):
                            offset_canvas.SetPixel(i,rowRight - 1, 0, index2, 0)
                            index2 += 2
                        else: 
                            offset_canvas.SetPixel(i,rowRight - 1, 0, 0, index3)
                            index3 += 2

                    # Check if no need to go back, i.e. one row/col left for this loop
                    if (rowLeft + 1 == rowRight or colUp + 1 == colBottom):
                        break

                    # Go to leftbottom corner
                    for i in list(range(rowLeft, rowRight - 1))[::-1]:
                        if(index < 255):
                            offset_canvas.SetPixel(colBottom - 1,i, index, 0, 0)
                            index += 2
                        elif(index2 <= 255):
                            offset_canvas.SetPixel(colBottom - 1,i, 0, index2, 0)
                            index2 += 2
                        else: 
                            offset_canvas.SetPixel(colBottom - 1,i, 0, 0, index3)
                            index3 += 2

                    # Go back before the start point
                    for i in list(range(colUp + 1, colBottom - 1))[::-1]:
                        if(index < 255):
                            offset_canvas.SetPixel(i,rowLeft, index, 0, 0)
                            index += 2
                        elif(index2 <= 255):
                            offset_canvas.SetPixel(i,rowLeft, 0, index2, 0)
                            index2 += 2
                        else: 
                            offset_canvas.SetPixel(i,rowLeft, 0, 0, index3)
                            index3 += 2
                    
                    # Update boundary value, start a new loop
                    rowLeft += 2
                    rowRight -= 1
                    colUp += 2
                    colBottom -= 1

                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                print("printing on second led board")
                
            else:
                print("Led board is off")
                signalRecieved = False
                for x in range (0,offset_canvas.width):
                    for y in range (0, offset_canvas.height):
                        offset_canvas.SetPixel(x,y,0,0,0)
                    
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)



# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    
    if (not simple_square.process()):
        simple_square.print_help()
