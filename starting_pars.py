import kaggle
import numpy as np
import pandas as pd

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

file_content = api.datasets_download_file('abdulmalik1518', 'cars-datasets-2025.csv')
print(file_content)