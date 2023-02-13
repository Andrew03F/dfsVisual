from PIL import Image
import random
import two
# makes a matrix then


black = (255, 255, 255)
white = (0,0,0)
size = (658,482)


# create matrix
matrix = two.initialize(size[0], size[1], 59)
two.remove_islands(matrix)



#initialize image

image = Image.new('RGB', size, color=black)
for p in range(size[0]):
    for q in range (size[1]):
        if (matrix[p][q] == 1):
            image.putpixel((p,q), white)
        else:
            image.putpixel((p,q),black)
image.save('black_pixel2.png')
image.show()