#!/usr/bin/env python
#-----------------------------------------------------------------------------
# ex2_qwiic_oled_display.py
#
# Simple Example for the Qwiic OLED Display
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2021
#
# This python library supports the SparkFun Electroncis qwiic
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers.
#
# More information on qwiic is at https:# www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#==================================================================================
# Example 2 - Simple example to display "hello world" on the Qwiic OLED Display board.
#

from __future__ import print_function
import qwiic_oled_base
import sys

def runExample():

    #  These three lines of code are all you need to initialize the
    #  OLED and print the splash screen.

    #  Before you can start using the OLED, call begin() to init
    #  all of the pins and configure the OLED.


    print("\nSparkFun OLED Display - Hello Example\n")

    #  Create instance with parameters for Qwiic OLED Display
    myOLED = qwiic_oled_base.QwiicOledBase(0x3C, 128, 32)

    if not myOLED.connected:
        print("The Qwiic OLED Display isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    myOLED.begin()

    #  clear(ALL) will clear out the OLED's graphic memory.
    myOLED.clear(myOLED.ALL) #  Clear the display's memory (gets rid of artifacts)
    
    #  Display buffer contents
    myOLED.display()
    time.sleep(3)

    #  clear(PAGE) will clear the Arduino's display buffer.
    myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
    
    #  Display buffer contents
    myOLED.display()
    time.sleep(3)

    #  Print "Hello World"
    #  ---------------------------------------------------------------------------
    #  Add text
    myOLED.print("Hello World")

    #  To actually draw anything on the display, you must call the display() function.
    myOLED.display()

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding OLED Hello Example")
        sys.exit(0)
