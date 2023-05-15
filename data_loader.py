import os
import pandas as pd

class DataLoader:
    def __init__(self):
        self.data_path = os.path.join(os.getcwd(), 'mockdata', 'MOCK_DATA.csv')
        self.loader = None

    def load_data(self):
        self.loader = pd.read_csv(self.data_path)
        return self.loader