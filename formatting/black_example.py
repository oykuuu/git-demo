import numpy as np
import pandas as pd
STATEMENT="This string is defined too close to imports."



SINGLE_QUOTE='Will be replaced by double quotes and moved up.'

LONG_STR = "This statement is a very long one. Therefore it has to be split into two lines and cannot be fixed in place."
class Dataset:
    name: str
    timestamp:int
    def __init__(self,path):

        self.path = path
        self._dataset =      None



def read_data( path :str)->pd.DataFrame:
    return pd.DataFrame(path)
def write_data( data,path) ->pd.DataFrame:
    data.to_csv(path)