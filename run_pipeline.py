# Test whether data is fetched properly

from data.data_loader import load_dataset;

df = load_dataset()
print(df.head(2))
