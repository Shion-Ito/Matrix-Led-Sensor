# Matrix-Led-Sensor
#Summary:
The purpose of this project is to handle user input of a detector to influence the led matrix board
to match where the input is being sensored from. In other words, wherever our indicator built pen
is shown for the matrix the LEDs will match with the corresponding output of light displayed
that are adjacent to the pen or near.The phototransistor will be built off the 3mm TIL78 parts and
will be connected with the adafruit in order to actually map the location of if the x and y indexes
of the matrix to refresh the view of what the sensor wants to output.
#Expected Results:
The expected results for this matrix sensor detector is that we will be able to project an led screen
where the user can draw and write on. This will be done using the photo resistive pen that we
will use will allow us to interact with the led matrix screen. The pen and screen will be
connected together in an organized manner where only one wire will be directly connected from
the pen to the matrix screen. Furthermore, it will use adafruit to monitor the photoresistor value
and also measure how and where the pen is located.
Materials Needed:
● Raspberry Pi
● Breadboard
● 64x64 RGB LED matrix
● 5V 4A Power Adapter (from AdaFruit)
● Female DC Power Adapter 2.1mm jack to Screw Terminal block
● 3mm TIL78 phototransistor
● Jumper wires
