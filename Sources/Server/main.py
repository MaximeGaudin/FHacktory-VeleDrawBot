#!/usr/bin/env python 

from serial import Serial
from time import sleep
from sys import argv

total_steps = 0

ON = [1]
OFF = [0]

addr = '/dev/tty.usbserial-A40131PF'

def connect():
  print 'Connecting...'
  arduino = Serial(addr, 9600)
  print 'Connection OK\n'

  return arduino

def step(arduino, stepperId, steps):
  print '[{0}] {1} steps...'.format(stepperId, steps)
  arduino.write([stepperId, steps])

def up(arduino):
  step(arduino, 0, 0)
  sleep(5)

def down(arduino):
  step(arduino, 0, 254)
  sleep(5)

def left(arduino):
  step(arduino, 1, 254)
  sleep(1)

def right(arduino):
  step(arduino, 1, 0)
  global total_steps 
  total_steps += 1
  sleep(1)

def pen_up(arduino):
  step(arduino, 2, 0)
  sleep(1)

def pen_down(arduino):
  step(arduino, 2, 40)
  sleep(1)


def next_letter(arduino):
  right(arduino)
  pen_down(arduino)

f = [ pen_down, pen_up, right, pen_down, pen_up, right, pen_down, right, pen_up, right, pen_down, pen_up, right ]
h = [ pen_down, pen_up, right, pen_down, pen_up, right, pen_down, pen_up, right, pen_down, pen_up, right ]
a = [ pen_down, pen_up, right, pen_down, right, pen_up, right ]
c = [ pen_down, right, pen_up, right, pen_down, pen_up, right, pen_down, right, pen_up, right, pen_down, pen_up, right ]
k = [ pen_down, right, pen_up, right, pen_down, pen_up, right, pen_down, right, pen_up, right ]
t = [ pen_down, right, pen_up, right ]
o = [ pen_down, right, pen_up, right, pen_down, right, pen_up, right, pen_down, right, pen_up, right ]
r = [ pen_down, pen_up, right, pen_down, right, pen_up, right, pen_down, pen_up, right ]
y = [ pen_down, right, pen_up, right, pen_down, pen_up, right, pen_down, right, pen_up, right, pen_down, right, pen_up, right ]

arduino = connect()

pen_up(arduino)
for arg in argv[1:]:
  { 
      'up': up, 
      'down': down, 
      'left': left, 
      'right': right,
      'pen_up': pen_up,
      'pen_down': pen_down,
  }[arg](arduino)

pen_up(arduino)
# [ left(arduino) for i in range(0, 32) ]

for l in [f, h, a, c, k, t, o, r, y]:
  for cmd in l:
    cmd(arduino)

