import numpy as np

def addition(array_1, array_2):
	if len(array_1) != len(array_2):
		raise ValueError("Array lengths must be the same")

	return array_1 + array_2

def subtraction(array_1, array_2):
	if len(array_1) != len(array_2):
		raise ValueError("Array lengths must be the same")

	return array_1 - array_2

arr_1 = np.ones([1, 4])
arr_2 = np.arange(4)
result = arr_1 + arr_2
