import numpy as np
import matplotlib.pyplot as plt

# ���������
G = 6.67430e-11  # �������������� ����������
c = 299792458  # �������� ����� � �/�
M = 10 * 1.9885e30  # ����� ������ ���� � �� (10 ���� ������)

# ��������� �����
size = 100  # ������ �����
grid = np.zeros((size, size))  # ����� ��� �������� ��������

# ��������� �������
grid[size // 2, size // 2] = M  # �������� ����� � �����

# ������� ��� ���������� ��������������� ���������� � ����� (x, y)
def calculate_potential(x, y):
    r = np.sqrt((x - size // 2) ** 2 + (y - size // 2) ** 2)
    if r == 0:
        return 0
    else:
        return -G * M / r

# ���������� ����� �� ������ ��������� ����
def update_grid():
    new_grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            new_grid[i, j] = calculate_potential(i, j)
    return new_grid

# ������������ ���������
def visualize():
    plt.imshow(grid, cmap='jet')
    plt.colorbar(label='Gravitational Potential (J)')
    plt.title('Black Hole Simulation')
    plt.show()

# ������ ���������
for _ in range(100):
    grid = update_grid()

visualize()

