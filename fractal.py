import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            real = x * (x_max - x_min) / (width - 1) + x_min
            imag = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color

    return image

width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 1000

mandelbrot_image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

plt.imshow(mandelbrot_image, cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Ensemble de Mandelbrot")
plt.xlabel("Partie réelle")
plt.ylabel("Partie imaginaire")
plt.show()
