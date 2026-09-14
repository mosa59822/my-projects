from turtle import *
from colorsys import *
rgb_to_hls(9)
bgcolor("blue")
h = 0
for i in range(1000):
    h+=0.0002
    color(hsv_to_rgb(h,1,1))
    if i % 5 == 0:
        right(3)
    forward(200)
    right(360/5)
    hideturtle()
done()