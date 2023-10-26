import math
import logging
import time 
import random
from src.test import points_visible, circle_line_segment_intersection
from src.poison_point import poison_point_process
from src.geometry import gen_points_for_line
from src.foundation.log_controller import LogController

named_tuple = time.localtime() # получить struct_time
time_string = time.strftime("%m_%d_%Y_%H_%M_%S", named_tuple)
log = logging.getLogger()
logger_controller = LogController()
output_path = 'logs'
logger_controller.initialize(output_path, 'output'+ time_string +  '.log', logging.INFO)

A = 50 # сторона квадратной области
lmbd = 0.01 # плотность точечного Пуассоновского процесса
radius = 2 # радиус окружности объекта, размещенного внутри квадратной области
dist = 20 # расстояние между двумя точками
alpha = 30 # угол области видимости точек

visible_counter = 0 # счетчик количества блокировок
unblock_counter = 0 # счетчик количества блокировок
exp_counter = 0 # счетчик количества экспериментов

while unblock_counter < 1000: # пока не достигнуто нужное количество блокировок
  x, y = poison_point_process(lmbd, A)
  x1, y1, x2, y2 = gen_points_for_line(A, dist) # генерируем точки линии прямой видимости
  if points_visible(x1, y1, alpha) and points_visible(x2, y2, alpha): # проверяем на видимость
    visible_counter += 1 # если видят друг друга
    if circle_line_segment_intersection(x, y, radius, x1, y1, x2, y2) == False:
      unblock_counter += 1 # если блокировки нет
  exp_counter += 1 # подсчитываем количество экспериментов

log.info(f'A = {A}, Lambda = {lmbd}, Radius = {radius}, distance = {dist}, alpha = {alpha}')
log.info(f"The number of cases when both sources see each other: {visible_counter}")
log.info(f"Number of experiments conducted: {exp_counter}")
log.info(f"Empirical probability of visibility: {round(visible_counter / exp_counter, 3)}")
log.info(f"Theoretical probability of visibility: {round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3)} ")
log.info(f"The number of non-locks and visibility of each other: {unblock_counter}")
log.info(f"Empirical probability of visibility and absence of blocking: {round(unblock_counter / exp_counter, 3)}")
log.info(f"Theoretical probability of visibility and absence of blocking: {round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3) * round(1 - math.exp(-lmbd * 2 * radius * (dist - 2 * radius)), 3)}" )
log.info(' ')

for j in range (3):
  A = random.randint(50,200) # сторона квадратной области

  for k in range (3):
    log.info(f'A = {A}, Lambda = {lmbd}, Radius = {radius}, distance = {dist}, alpha = {alpha}')

    lmbd = 0.01 # плотность точечного Пуассоновского процесса
    radius = 2 # радиус окружности объекта, размещенного внутри квадратной области
    dist = 20 # расстояние между двумя точками
    alpha = random.randint(1,180) # угол области видимости точек

    visible_counter = 0 # счетчики количества блокировок
    unblock_counter = 0 
    exp_counter = 0 # счетчик количества экспериментов
    while unblock_counter < 1000: # пока не достигнуто нужное количество блокировок
      try:
        x, y = poison_point_process(lmbd, A)
        x1, y1, x2, y2 = gen_points_for_line(A, dist) # генерируем точки линии прямой видимости
        if points_visible(x1-x2, y1-y2, alpha) and points_visible(x2-x1, y2-y1, alpha): # проверяем на видимость
          visible_counter += 1 # если видят друг друга
        if circle_line_segment_intersection(x, y, radius, x1, y1, x2, y2) == False:
          unblock_counter += 1 # если блокировки нет
        exp_counter += 1 # подсчитываем количество экспериментов
      except Exception as e: 
        log.error('Error occurred: %s', e)
        raise e 
    
    
    log.info(f"The number of cases when both sources see each other: {visible_counter}")
    log.info(f"Number of experiments conducted: {exp_counter}")
    log.info(f"Empirical probability of visibility: {round(visible_counter / exp_counter, 3)}")
    log.info(f"Theoretical probability of visibility: {round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3)} ")
    log.info(f"The number of non-locks and visibility of each other: {unblock_counter}")
    log.info(f"Empirical probability of visibility and absence of blocking: {round(unblock_counter / exp_counter, 3)}")
    log.info(f"Theoretical probability of visibility and absence of blocking: {round((pow(alpha / 180 * math.pi, 2)) / (4 * pow(math.pi, 2)), 3) * round(1 - math.exp(-lmbd * 2 * radius * (dist - 2 * radius)), 3)}" )
    log.info(' ')