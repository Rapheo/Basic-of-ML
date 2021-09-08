import numpy as np
# from operator import itemgetter

data = np.genfromtxt('input.txt', delimiter=';',skip_header=1,filling_values=0,dtype='float')
data = np.append(data,[[10,12,13,14]],axis=0)
data = np.append(data,[[10],[12],[13],[14],[15]],axis=1)
print(data)
print(data.shape,data.size,data.ndim)
data = data[::-1,::-1]
print(data)
index = np.where(data > 10)
print(index[0],index[1])
newArray = data[:4,1:5]
print(newArray)

newArray = (newArray - newArray.min()/(newArray.max()-newArray.min()))
print(newArray)
mean_colmn = np.array([])
for i in range(len(newArray)):
    mean_colmn = np.append(mean_colmn,newArray[i].mean())

print(mean_colmn)
newArray = np.append(newArray,[mean_colmn],axis=0)
print(newArray)
newArray = sorted(newArray,key = lambda x: x[1])
print(newArray)


# newArray = newArray.tolist()
# print(newArray)
# print(newArray.sort(key = lambda x: x[1]))





# # a = np.zeros((2,2))   # Create an array of all zeros
# # print(a)              # Prints "[[ 0.  0.]
# #                       #          [ 0.  0.]]"

# # b = np.ones((4,2))    # Create an array of all ones
# # print(b)              # Prints "[[ 1.  1.]]"
# # b = np.linspace(0,10,10)
# # print(b)  

# c = np.array([[1,3,2],[4,5,6]])
# newArray = np.append(c,[[50,60,40]],axis = 0)
# newArray = newArray[::-1,::-1]
# # print(np.savetxt("a.csv",newArray))
# print(np.arange(10,0,-1))
# print(np.random.seed(100))
