# Load CSV using Pandas
from pandas import read_csv
import numpy as np
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
#Dimensions of data
shapes = data.shape
print(shapes)
