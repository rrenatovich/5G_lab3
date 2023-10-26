from .src.test import points_visible, circle_line_segment_intersection
from .src.poison_point import poison_point_process
from .src.geometry import gen_points_for_line


import math

A = 100 # сторона квадратной области
lmbd = 0.01 # плотность точечного Пуассоновского процесса
radius = 2 # радиус окружности объекта, размещенного внутри квадратной области
dist = 20 # расстояние между двумя точками
alpha = 90 # угол области видимости точек

visible_counter = 0 # счетчик количества блокировок
unblock_counter = 0 # счетчик количества блокировок
exp_counter = 0 # счетчик количества экспериментов

while unblock_counter < 1000: # пока не достигнуто нужное количество блокировок
  x, y = poison_point_process(lmbd, A)
  x1, y1, x2, y2 = gen_points_for_line() # генерируем точки линии прямой видимости
  if points_visible(x1, y1, alpha) and points_visible(x2, y2, alpha): # проверяем на видимость
    visible_counter += 1 # если видят друг друга
    if circle_line_segment_intersection(x, y, radius, x1, y1, x2, y2) == False:
      unblock_counter += 1 # если блокировки нет
  exp_counter += 1 # подсчитываем количество экспериментов


print("Число случаев, когда оба источника видят друг друга:", visible_counter)
print("Число проведенных экспериментов:",exp_counter)
print("Эмпирическая вероятность видимости", round(visible_counter / exp_counter, 3))
print("Теоретическая вероятность видимости", round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3))
print("*******************************************************************************************************")
print("Число не блокировок и видимости друг друга:", unblock_counter)
print("Число проведенных экспериментов:",exp_counter)
print("Эмпирическая вероятность видимости и отсутсвия блокировки", round(unblock_counter / exp_counter, 3))
print("Теоретическая вероятность видимости и отсутсвия блокировки", round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3) * round(1 - math.exp(-lmbd * 2 * radius * (dist - 2 * radius)), 3))