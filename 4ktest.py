from PIL import Image

width = 3840
height = 2160
color1 = (0,0,0)
color2 = (255,255,255)

img1 = Image.new(mode = "RGB", size = (width, height), color = color1)
px1=img1.load()
for x in range(width):
    for y in range(height):
        if y % 2 == 0:
            px1[x,y] = color2
img1.save("out1.png")

img2 = Image.new(mode = "RGB", size = (width, height), color = color1)
px2=img2.load()
for x in range(width):
    for y in range(height):
        if x % 2 == 0:
            px2[x,y] = color2
img2.save("out2.png")

img3 = Image.new(mode = "RGB", size = (width, height), color = color1)
px3=img3.load()
for x in range(width):
    for y in range(height):
        if (x + y) % 2 == 0:
            px3[x,y] = color2
img3.save("out3.png")
