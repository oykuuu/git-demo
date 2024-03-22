"""Example file for pydocstyle exercise.

**Tip:** You can use `Markdown` here in case we use Sphinx.
"""

import numpy as np
import pandas as pd


class Calculations:
    """Class for simple calculations."""

    def __init__(self, constant: int):
        """Initialize Calculations class that resolve simple maths operations.

        Args:
            constant (int): Constant value to use in calculations.
        """
        self.constant = constant

    def add(self, array_list: List[np.Array]) -> np.Array:
        """Add a list of numpy arrays of same length.

        Args:
            array_list (List[np.Array]): List of numpy arrays to sum

        Returns:
            np.Array: Resulting sum
        """
        summation = array_list[0]
        for array in array_list[1]:
            self.__check_array_lenghts(summation, array)
            summation += array

        return summation

    def __check_array_lenghts(self, arr_1: np.Array, arr_2: np.Array):
        if len(arr_1) != len(arr_2):
            raise ValueError("Differing lengths")


def read_data(path: str) -> pd.DataFrame:
    """Sometime one liner docstrings are enough."""
    return pd.DataFrame(path)


def write_data(data: pd.DataFrame, path: str):
    """Notice that function string has no return indicator as nothing is returned."""
    data.to_csv(path)
