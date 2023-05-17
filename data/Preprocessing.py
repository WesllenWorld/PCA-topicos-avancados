import pandas as pd
import numpy as np

class Preprocessing:

    def __init__(self):
        pass

    def load_data(self, path):
        self.data = pd.read_csv(path, sep=',')

    def get_data(self):
        return self.data
    
        
        