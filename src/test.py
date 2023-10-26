import numpy as np
import math

from .geometry import height_points
def circle_line_segment_intersection(circle_center_x,
                                     circle_center_y,
                                     circle_radius,
                                     first_line_point_x,
                                     first_line_point_y,
                                     second_line_point_x,
                                     second_line_point_y):

  block_flag = False # флаг для отслеживания блокировки

  for i in range(len(circle_center_x)):
    (x1, y1), (x2, y2), (x0, y0) = (first_line_point_x, first_line_point_y), (second_line_point_x, second_line_point_y), (circle_center_x[i], circle_center_y[i])

    if abs((y2 - y1) * x0 + (x1 - x2) * y0 + y1 * x2 - x1 * y2) / math.sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2)) <= circle_radius:  # если есть пересечения объекта с прямой,
                                                                                                                                  # проверяем пересечение отрезка, заданного координатами и объекта

      if pow(x1 - x0, 2) + pow(y1 - y0, 2) <= pow(circle_radius, 2): # если первая точка линии прямой видимости находится внутри объекта, блокировка
        block_flag = True
        break

      elif pow(x2 - x0, 2) + pow(y2 - y0, 2) <= pow(circle_radius, 2): # если вторая точка линии прямой видимости находится внутри объекта, блокировка
        block_flag = True
        break

      else: # если координаты высоты, опущенной из центра на прямую, принадлежат заданному отрезку, блокировка
        height_x, height_y = height_points(x0, y0, x1, y1, x2, y2)
        if min(x1, x2) < height_x < max(x1, x2) and min(y1, y2)< height_y < max(y1, y2):
          block_flag = True
          break

  return block_flag

# фкнция для проверки того, что одна точка попадает в область видимости второй
def points_visible(x, y, alpha):
  # gamma_angle - угол направления диаграммы направленности
  # alpha - угол области видимости точек диаграммы направленности
  gamma_angle = np.random.uniform(0, 2 * np.pi)
  gamma_x, gamma_y = np.cos(gamma_angle), np.sin(gamma_angle) # координаты вектора направленности

  gamma_cos = (x * gamma_x + y * gamma_y) / (math.sqrt(pow(x, 2) + pow(y, 2)) * math.sqrt(pow(gamma_x, 2) + pow(gamma_y, 2))) # угол между линией прямой видимости и вектором направленности

  if np.arccos(gamma_cos) * 180 / math.pi < alpha / 2: # если косинус найденного угла меньше, чем alpha/2, одна точка видит другую
    return True
  else:
    return False
  