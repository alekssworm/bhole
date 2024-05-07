import numpy as np
import matplotlib.pyplot as plt

# Константы
G = 6.67430e-11  # Гравитационная постоянная
c = 299792458  # Скорость света в м/с
M = 10 * 1.9885e30  # Масса черной дыры в кг (10 масс Солнца)

# Параметры сетки
size = 100  # Размер сетки
grid = np.zeros((size, size))  # Сетка для хранения значений

# Начальные условия
grid[size // 2, size // 2] = M  # Помещаем массу в центр

# Функция для вычисления гравитационного потенциала в точке (x, y)
def calculate_potential(x, y):
    r = np.sqrt((x - size // 2) ** 2 + (y - size // 2) ** 2)
    if r == 0:
        return 0
    else:
        return -G * M / r

# Обновление сетки на каждом временном шаге
def update_grid():
    new_grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            new_grid[i, j] = calculate_potential(i, j)
    return new_grid

# Визуализация симуляции
def visualize():
    plt.imshow(grid, cmap='jet')
    plt.colorbar(label='Gravitational Potential (J)')
    plt.title('Black Hole Simulation')
    plt.show()

# Запуск симуляции
for _ in range(100):
    grid = update_grid()

visualize()

