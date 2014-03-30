#!/usr/bin/env python 

from serial import Serial
from time import sleep
from sys import argv

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
  sleep(5)

def right(arduino):
  step(arduino, 1, 0)
  sleep(5)

def pen_up(arduino):
  step(arduino, 2, 0)
  sleep(1)

def pen_down(arduino):
  step(arduino, 2, 45)
  sleep(1)


def next_letter(arduino):
  right(arduino)
  pen_down(arduino)

def draw_a(arduino):
  commands = [ 
    pen_down, pen_up, right, pen_down, right, right, pen_up
  ]
  up(arduino)
  up(arduino)
  right(arduino)
  down(arduino)
  left(arduino)
  right(arduino)
  down(arduino)

  pen_up(arduino)
  next_letter(arduino)

def draw_f(arduino):
  up(arduino)
  right(arduino)
  left(arduino)
  up(arduino)
  right(arduino)

  pen_up(arduino)
  down(arduino)
  down(arduino)
  next_letter(arduino)

def draw_h(arduino):
  up(arduino)
  up(arduino)
  down(arduino)
  right(arduino)
  up(arduino)
  down(arduino)
  down(arduino)

  pen_up(arduino)
  next_letter(arduino)


def draw_letter(arduino, letter):
  {
    'a': draw_a(arduino),
  }[letter](arduino)

arduino = connect()
for arg in argv[1:]:
  { 
      'up': up, 
      'down': down, 
      'left': left, 
      'right': right,
      'pen_up': pen_up,
      'pen_down': pen_down,
  }[arg](arduino)

# draw_f(arduino)
#draw_h(arduino)
