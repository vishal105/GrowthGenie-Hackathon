# data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_excel(self.file_path)
        # Additional data validation if needed
        return data
