import numpy as np
import pandas as pd


class Calculations:
    def __init__(self, constant):
        self.constant = constant

    def add(self, array_list):
        summation = array_list[0]
        for array in array_list[1]:
            self.__check_array_lenghts(summation, array)
            summation += array

        return summation

    def __check_array_lenghts(self, arr_1, arr_2):
        if len(arr_1) != len(arr_2):
            raise ValueError("Differing lengths")


def read_data(path):
    return pd.DataFrame(path)


def write_data(data, path):
    data.to_csv(path)
