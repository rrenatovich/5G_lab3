import numpy as np 
from scipy.linalg import solve


# функция для генерации линия внутри выбранной области со сторонами A
def gen_points_for_line():
  flag_for_second_point = False # определяем флаг для проверки лежит ли вторая точка вутри области

  angl = np.random.uniform(0, 2 * np.pi) # выбираем угол для линии прямой видимости
  x1, y1 = np.random.uniform(0, A), np.random.uniform(0, A) # генерируем координаты первой точки линии прямой видимости
  x2 = x1 + dist * np.cos(angl) # генерируем координаты второй точки линии прямой видимости
  y2 = y1 + dist * np.sin(angl)

  while flag_for_second_point == False: # пока вторая точка не лежит внутри области
    if x2 < A and y2 < A and x2 > 0 and y2 > 0: # проверяем если вторая точка лежит внутри области
      flag_for_second_point = True # меняем значение флага
    else: # если вторая точка не лежит внутри области, то генерируем заново
      angl = np.random.uniform(0, 2 * np.pi) # выбираем другой угол для линии прямой видимости
      x2 = x1 + dist * np.cos(angl) # генерируем новые координаты второй точки линии прямой видимости
      y2 = y1 + dist * np.sin(angl)

  return x1, y1, x2, y2

# функция для расчета расстояния между двумя точками
def dist_two_points(x1, y1, x2, y2):
  return np.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# функция для нахождения координаты высоты, опущенной из центра окружности на отрезок
def height_points(x0, y0, x1, y1, x2, y2):
  # решаем систему линейных уравнений для нахождения коэффициентов прямой k и b
  A = np.array([[x1, 1],
                [x2, 1],])

  b = np.array([y1, y2]).reshape((2, 1))
  result = solve(A, b)

  k = result[0][0]
  b = result[1][0]

  # находим угловой коэффициент k2 перпендикулярной прямой (высоты) и коэффициент b2
  k2 = -1 / k
  b2 = y0 - k2 * x0

  # решаем систему линейных уравнений для нахождения координатов высоты x и y
  A = np.array([[k, -1],
              [k2, -1],])

  c = np.array([-b, -b2]).reshape((2, 1))
  result = solve(A, c)

  return result[0][0], result[1][0]