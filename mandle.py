from PIL import Image

# Image size
width, height = 800, 600

# Create a blank image with a white background
img = Image.new("RGB", (width, height), "white")
pixels = img.load()

# Parameters for the Mandelbrot set
min_x, max_x = -2, 1
min_y, max_y = -1, 1
max_iter = 256

# Generate the Mandelbrot set
for x in range(width):
    real = min_x + (max_x - min_x) * x / width
    for y in range(height):
        imag = min_y + (max_y - min_y) * y / height
        c = complex(real, imag)
        z = 0
        for i in range(max_iter):
            if abs(z) > 2:
                # Color the pixel based on the number of iterations
                color = (i % 8 * 32, i % 32 * 8, i % 64 * 4)
                pixels[x, y] = color
                break
            z = z * z + c

# Save the image
img.save("mandelbrot.png")
