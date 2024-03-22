import numpy as np
import pandas as pd

STATEMENT = "This string is defined too close to imports."


SINGLE_QUOTE = "Will be replaced by double quotes and moved up."


class Dataset:
    name: str
    timestamp: int

    def __init__(self, path):

        self.path = path
        self._dataset = None


def read_data(path: str) -> pd.DataFrame:
    return pd.DataFrame(path)


def write_data(data, path) -> pd.DataFrame:
    data.to_csv(path)


def function_with_many_arguments(*args, **kwargs):
    return len(args), len(kwargs)


len_args, len_kwargs = function_with_many_arguments(
    0,
    1,
    None,
    "abc",
    first_key_argument=1,
    second_key_argument="2",
    third_key_argument=True,
)

df = pd.DataFrame(np.array([[12, 13, 14], [15, 16, 17], [22, 23, 24], [26, 26, 26], [12, 13, 14], [15, 16, 17], [22, 23, 24], [26, 26, 26]]), columns=['column_1', 'column_2', 'column_3'])