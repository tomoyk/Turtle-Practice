from turtle import *
from time import sleep

shape()

# http://www.softist.com/programming/hilbert/hilbert.htm

debug = 1
dist = 20

# 始点を揃える
def begin(k):
  print("begin({})".format(k))
  
  if heading() > k:
    right( heading() -k )
  elif heading() < k:
    left( k - heading() )

# 関数群
def ldr(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - ldr({})".format(n))

  # handle
  begin(180)

  dlu(n-1)

  begin(180) 
  forward(dist)

  ldr(n-1)

  begin(270)
  forward(dist)

  ldr(n-1)

  begin(0)
  forward(dist)

  urd(n-1)


def urd(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - urd({})".format(n))

  # handle
  rul(n-1)

  begin(90)
  forward(dist)
  right(90)

  urd(n-1)

  begin(0)
  forward(dist)
  right(90)

  urd(n-1)

  begin(270)
  forward(dist)

  ldr(n-1)


def rul(n):
  if n == 0:
    return
  
  if debug == 1:
    print("- - - rul({})".format(n))

  # handle
  urd(n-1)

  begin(0)
  forward(dist)
  left(90)

  rul(n-1)
  
  begin(90)
  forward(dist)
  left(90)

  rul(n-1)

  begin(180)
  forward(dist)

  dlu(n-1)


def dlu(n):
  if n == 0:
    return

  if debug == 1:
    print("- - - dlu({})".format(n))

  # handle
  ldr(n-1)

  begin(270)
  forward(dist)
  right(90)

  dlu(n-1)

  begin(180)
  forward(dist)
  right(90)

  dlu(n-1)

  begin(90)
  forward(dist)

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
