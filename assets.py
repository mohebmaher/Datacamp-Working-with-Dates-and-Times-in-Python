# Unpack florida_hurricane_dates
import pickle

with open("./data/florida_hurricane_dates.pkl", 'rb') as f:
    florida_hurricane_dates = pickle.load(f)
    
    
# Shuffle elements in florida_hurricane_dates
from random import shuffle, seed

seed(42)
dates_scrambled = florida_hurricane_dates.copy()
shuffle(dates_scrambled)