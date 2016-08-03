from pandas import DataFrame, read_csv

import pandas as pd
import matplotlib.pyplot as plt


zipcode = pd.read_csv('20150710_busan_text.txt', 'cp949')

print(zipcode.head())