from turtle import *
from time import sleep

length = 30

def draw(k):
  if k==0:
    return
  forward(length)
  draw(k-1)
  left(60)
  draw(k-1)
  forward(length)
  right(120)
  draw(k-1)
  forward(length)
  left(60)
  forward(length)
  draw(k-1)

draw(2)

done()
