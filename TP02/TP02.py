import pandas as pd

class CSVReader(fp):
    def __init__(self, fp):
        self.fp = fp
        self._data = None
        
    def read(self):
        self._data = pd.read_csv(fp)
        
    def preview(self, n = 5):
        print(self._data[:,  : n])