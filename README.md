# Blinkt
Python code written for my little Blinkt!

this is my first 'original' Blinkt program

previous fluffings were just amended clones of the excellent Pimoroni supplied examples

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
