import numpy as np
arr = np.arange(1e7)

larr = arr.tolist()

def list_times(alist, scalar):
   for i, val in enumerate(alist):
      alist[i] = val * scalar
   return alist
