## this is my first lesson on NumPy refresher
## lets learn about the numpy array and somethings we can do with it
import numpy as np

normal_array = [1,2,3,4,5]
normal_array = np.array(normal_array)

print(normal_array)
## easy to perform operations on these such types of arrays
print(normal_array + normal_array)



## learning about type casting through numpy
## this is done through the astype("type switch")
numbers = np.array([1,2,3,4,5])
print(numbers.dtype)
numbers = numbers.astype('float64')
print(numbers.dtype)

## vectorization is the process where you are able to perform scalar operations on numpy array
adding = np.array([[1,2,3], [4,5,6]])
print(adding)
print("...")
print(adding + adding)
print("...")
print(adding * adding)
print("...")

## arrays with more dimenstions in numpy library
## lets create a 2 x 2 x 3 array
multi_d = np.array([[[1,2,3], [5,9,11]], [[10, 9, 7], [17, 20, 18]]])
## if I were to do multi_d[0].... it would output a 2 x 3 array

print(multi_d)
print('...')
print(multi_d[0]) ## doing this would create a 2 x 3 array
print("...")
print(multi_d[:1, 1:, 1]) ## this is an interesting way of indexing for very specific items in within such arrays


## boolean indexing is a concept where we try to use boolean values as a way to be able to index through a list
## this is a powerful concept because we are able to pull data based on some information that we need to test
## allows for programmers to be able to take out key parts of information when analyzing a data-set
names = np.array(['Aryan', 'Arya', 'Aryan', 'Jack', 'Ryan'])
data = np.random.randn(5,4) ## this will create random numbers for a 7x4 array
print(data)
print("...")
print(data[names == 'Aryan'])

## lets go over fancy indexing
arr = np.arange(32).reshape((8,4))
print(arr)
print('...')
print(arr[[1,3,5],[2,0,1]] )
print("...")
print(arr[[1,2,5, 3]][:, [1,3,0,2]])
print("...")

## transpose of an array
## this is done through the t function
arr = np.arange(32).reshape((8,4))
arr_t = arr.T
x = np.dot(arr_t, arr)
arr = np.arange(32).reshape(2,4,4)

print(arr)
print('...')

## using a tuple like this on the numpy arrays will restructure the arrays such that the first and second dimesnsion switched
print(arr.transpose(1,0,2))


## whenever wanting to do any data-processing numpy is a great tool as it will save alot of time compared to python
## vectorization allows you to perform a task on every value in an array

print("lets look at some data processing")
point = np.arange(-5, 5, .01)
print(point)
print("...")

## meshgrid is used to create coordinate systems for various mathematical computation
xs, ys = np.meshgrid(point, point)
print(xs)
print("....")



## we can do conditional statements in python through the where function
randomm = np.random.randn(4,4)
print(randomm)
## we can use the where function to replace all positive value with positive 2
new = np.where(randomm > 0, 2, -2)
print(new)

## difference between the any and all fucntion
bools = np.array([True, False, True, True, False, False])
print(bools.any) # this will check if any of the bools are true
print("...")
print(bools.all) # this will check if any of the bools are false



