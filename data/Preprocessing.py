import pandas as pd
import numpy as np

class Preprocessing:

    def __init__(self):
        pass

    def load_data(self, path):
        labNome = ['Sexo']
        labNum = ['Comprimento','Diametro','Altura','Peso total','Peso sem casca','Peso das visceras','Peso da casca']
        labTarget = ['Aneis']

        self.data.columns = labNome + labNum


    def get_data(self):
        return self.data


        