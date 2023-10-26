import numpy as np

def poison_point_process(lmbd, a):
  s = np.random.poisson(lmbd * pow(a, 2))
  x = np.random.uniform(0, a, s)
  y = np.random.uniform(0, a, s)
  return x, y