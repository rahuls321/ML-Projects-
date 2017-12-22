#Standardize data (0 mean , 1 stdev)
#By GAussian Distribution
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler
array = data.values
#Seperate array into input and output components
X = array[:,0:5]
Y = array[:,5]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
set_printoptions(precision=3)
print(rescaledX[0:5,:])
