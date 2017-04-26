from turtle import *
from time import sleep

shape()

# http://www.softist.com/programming/hilbert/hilbert.htm

debug = 1
dist = 20

# 始点を揃える
def begin(k):
  if debug == 1:
    print("begin({})".format(k))

  deg_a = heading() - k
  deg_b = 360 - abs(deg_a)

  if heading() > k:
    right( heading() - k )
  elif heading() < k:
    left( k - heading() )

def line(rad):
  begin(rad)
  forward(dist)
  return

# 関数群
def ldr(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - ldr({})".format(n))

  # handle
  dlu(n-1)

  line(180)

  ldr(n-1)

  line(270)

  ldr(n-1)

  line(0)

  urd(n-1)


def urd(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - urd({})".format(n))

  # handle
  rul(n-1)

  line(90)
  right(90)

  urd(n-1)

  line(0)
  right(90)

  urd(n-1)

  line(270)

  ldr(n-1)


def rul(n):
  if n == 0:
    return
  
  if debug == 1:
    print("- - - rul({})".format(n))

  # handle
  urd(n-1)

  line(0)
  left(90)

  rul(n-1)
  
  line(90)
  left(90)

  rul(n-1)

  line(180)

  dlu(n-1)


def dlu(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - dlu({})".format(n))

  # handle
  ldr(n-1)

  line(270)
  right(90)

  dlu(n-1)

  line(180)
  right(90)

  dlu(n-1)

  line(90)

  rul(n-1)

###############

left(11)
begin(0)

#ldr(3)
penup()
setposition(window_width()/2-dist,window_height()/2-dist)
pendown()
ldr(5)

done()
