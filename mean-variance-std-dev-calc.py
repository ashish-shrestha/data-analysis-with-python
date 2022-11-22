import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    flat_array = np.array(list)
    twod_array = flat_array.reshape(3, 3)
    mean = [twod_array.mean(axis=0).tolist(), twod_array.mean(axis=1).tolist(), flat_array.mean().tolist()]
    var = [twod_array.var(axis=0).tolist(), twod_array.var(axis=1).tolist(), flat_array.var().tolist()]
    std_dev = [twod_array.std(axis=0).tolist(), twod_array.std(axis=1).tolist(), flat_array.std().tolist()]
    maximum = [twod_array.max(axis=0).tolist(), twod_array.max(axis=1).tolist(), flat_array.max().tolist()]
    minimum = [twod_array.min(axis=0).tolist(), twod_array.min(axis=1).tolist(), flat_array.min().tolist()]
    sumTotal = [twod_array.sum(axis=0).tolist(), twod_array.sum(axis=1).tolist(), flat_array.sum().tolist()]
    calculations = {'mean' : mean, 'variance' : var, 'standard deviation' : std_dev, 'max' : maximum, 'min' : minimum, 'sum' : sumTotal}

    return calculations

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(list))