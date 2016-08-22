#!/usr/bin/env python3

# =================================================
# Program by Norman deVaux Reynolds
# email normandevauxreynolds at yahoo dot co dot uk
# -------------------------------------------------
# Purpose: to scroll numbers, either input from the
#          command line or randomly generated,
#          across the Blinkt! leds. Why?
# -------------------------------------------------
# Because I wanted to have my little Pi Zero show
# me which Gaussian prime numbers it was finding
# on its walk to infinity in the plane of complex
# numbers. I have written a C program to perform
# such a walk to infinity as part of my main MSc
# dissertation project in pure mathematics at
# Birkbeck College, University of London, UK.
# This C program has been running on various Linux
# computers for over a year and it has reached
# approx. 100 billion units from the origin, at
# 97,912,135,379 + 97,912,162,926i, stepping on
# more than 23,312,400,000 Gaussian primes. I have
# recently amended it to perform a call to this
# Python program every time the C program finds a
# new prime number, passing the real and imaginary
# parts of the Gaussian prime as a single string.
# It does this by using a simple system( ... ) call
# from within the running C program. For more info
# on Gaussian integers and primes, see this page:
# https://en.wikipedia.org/wiki/Gaussian_moat
# =================================================

import sys    # for the argv input parameters
import time   # to time the pauses as we scroll
import random # to generate a random test integer
import string # to perform translations; see below

from blinkt import set_pixel, show # for our Pi Zero lights!

# =================================================
# Routine to display a single digit as a lit led.
# The led number is input, plus the digit as a
# single ASCII character and the brightness
# -------------------------------------------------
def lightNumber( led, char, b ):
	# char and led must be between 0 and 7
	# and b = brightness between 0.0 and 1.0
	if char   == '0' : # grey
		set_pixel( led, 128, 128, 128, b )
	elif char == '1' : # red
		set_pixel( led, 255, 0, 0, b )
	elif char == '2' : # green
		set_pixel( led, 0, 255, 0, b )
	elif char == '4' : # blue 
		set_pixel( led, 0, 0, 255, b )
	elif char == '3' : # red + green = yellow
		set_pixel( led, 255, 255, 0, b )
	elif char == '5' : # red + blue = magenta
		set_pixel( led, 255, 0, 255, b )
	elif char == '6' : # green + blue = cyan
		set_pixel( led, 0, 255, 255, b )
	elif char == '7' : # red + green + blue = white
		set_pixel( led, 255, 255, 255, b )
	elif char == '8' : # orange 
		set_pixel( led, 255, 165, 0, b )
	elif char == '9' : # brown
		set_pixel( led, 165, 42, 42, b )
	else             : # unknown = black, catch-all
		set_pixel( led, 0, 0, 0, b )
# =================================================

# =================================================
# If no parameter input, generate a random number
# (I use this for testing purposes), otherwise use
# the number input. Note that any string can be
# input, but only the digits 0 to 9 will actually
# cause the Blinkt! leds to light up.
# -------------------------------------------------
if len(sys.argv) < 2:
        my_str = str( random.randint( 0, 1000000000 ) )
else :
	my_str = sys.argv[ 1 ]

if len( my_str ) > 30:
        my_str = my_str[ :30 ] # the left-most digits
# =================================================


# =================================================
# limit input numbers to 30 digits...
# just an arbitrary cut-off length really
# -------------------1---------2-------------------
#          012345678901234567890123456789
dummy   = "------------------------------" # this can be any string thingy
in_tab  = "abcdefghijklmnopqrstuvwxyzABCD" # used as the translation string
if len( my_str ) < len( in_tab ):
        in_tab = in_tab[ :len( my_str ) ] # right-most chars
# maketrans demands that these two strings be the same length

# create a translation table: a -> 0th digit, b -> 1st digit, etc
# reading from left to right along the input number
table = dummy.maketrans( in_tab, my_str )
# =================================================

# =================================================
# Here's the neat trick: I create a matrix of
# characters to represent the number scrolling from
# right-to-left and the translation table converts
# 'a' to the first digit, 'b' to the second digit,
# and so on. E.g., if "33457" were input, then 
# in_tab is truncated to equal "abcde" and row 07
# below is translated from "-abcdefg" to "-33457g".
# When this row is processed below, the '-' and 'g'
# characters are ignored by the lightNumber( ... )
# function and just appear as 'off' leds while '3'
# lights up as yellow, '4' as blue, etc.
# -------------------------------------------------
list_of_strings = [] # must be instantiated as a list thingy
list_of_strings.append( "--------" ) #  0 = row of 'off' leds
list_of_strings.append( "-------a" ) #  1
list_of_strings.append( "------ab" ) #  2
list_of_strings.append( "-----abc" ) #  3
list_of_strings.append( "----abcd" ) #  4
list_of_strings.append( "---abcde" ) #  5
list_of_strings.append( "--abcdef" ) #  6
list_of_strings.append( "-abcdefg" ) #  7
list_of_strings.append( "abcdefgh" ) #  8
list_of_strings.append( "bcdefghi" ) #  9
list_of_strings.append( "cdefghij" ) # 10
list_of_strings.append( "defghijk" ) # 11
list_of_strings.append( "efghijkl" ) # 12
list_of_strings.append( "fghijklm" ) # 13
list_of_strings.append( "ghijklmn" ) # 14
list_of_strings.append( "hijklmno" ) # 15
list_of_strings.append( "ijklmnop" ) # 16
list_of_strings.append( "jklmnopq" ) # 17
list_of_strings.append( "klmnopqr" ) # 18
list_of_strings.append( "lmnopqrs" ) # 19
list_of_strings.append( "mnopqrst" ) # 20
list_of_strings.append( "nopqrstu" ) # 21
list_of_strings.append( "opqrstuv" ) # 22
list_of_strings.append( "pqrstuvw" ) # 23
list_of_strings.append( "qrstuvwx" ) # 24
list_of_strings.append( "rstuvwxy" ) # 25
list_of_strings.append( "stuvwxyz" ) # 26
list_of_strings.append( "tuvwxyzA" ) # 27
list_of_strings.append( "uvwxyzAB" ) # 28
list_of_strings.append( "vwxyzABC" ) # 29
list_of_strings.append( "wxyzABCD" ) # 30
list_of_strings.append( "xyzABCD-" ) # 31
list_of_strings.append( "yzABCD--" ) # 32
list_of_strings.append( "zABCD---" ) # 33
list_of_strings.append( "ABCD----" ) # 34
list_of_strings.append( "BCD-----" ) # 35
list_of_strings.append( "CD------" ) # 36
list_of_strings.append( "D-------" ) # 37
# =================================================

# =================================================
# Use the string translate method to do the string
# conversion as described above.
# -------------------------------------------------
i = 0
while i < len( list_of_strings ):
        list_of_strings[ i ] = list_of_strings[ i ].translate( table )
        i = i + 1
# =================================================

# =================================================
# Here we scroll the lights, right-to-left.
# Setting the max_len stops us using more blank
# rows than we need to at the end.
# The 8 is because there are 8 Blinkt! leds.
# -------------------------------------------------
brightness = 0.1 # this doesn't need to blind us
row = 0
max_len = min( [ len( my_str ) + 8, len( list_of_strings ) ] )
while row < max_len:
	col = 0
	while col < 8:
		lightNumber( col, list_of_strings[ row ][ 7 - col ], brightness )
		col = col + 1
	show()
	time.sleep( 0.5 )
	row = row + 1
# =================================================
