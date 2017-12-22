from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from pandas import read_csv
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
array = data.values
#Seperate array into input and output components
X = array[:,0:5]
Y = array[:,5]
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)
#Summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])
