# Unpack florida_hurricane_dates dataset
import pickle

with open("./data/florida_hurricane_dates.pkl", 'rb') as f:
    florida_hurricane_dates = pickle.load(f)
    
    
# Shuffle elements in florida_hurricane_dates
from random import shuffle, seed

seed(42)
dates_scrambled = florida_hurricane_dates.copy()
shuffle(dates_scrambled)


# Unpack onebike_datetimes list
import pickle

with open("./data/onebike_datetimes.pkl", 'rb') as f:
    onebike_datetimes = pickle.load(f)