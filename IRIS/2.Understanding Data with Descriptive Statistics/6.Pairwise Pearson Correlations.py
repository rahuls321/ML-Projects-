from pandas import read_csv
from pandas import set_option
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
set_option('precision', 3)
correlations = data.corr(method = 'pearson')
print(correlations)
