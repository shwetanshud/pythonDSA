import array

my_array = array.array('i')
print(my_array)

my_array1 = array.array('i', [1,2,3,4])
print(my_array1)

#array using numpy
import numpy as np
np_array = np.array([], dtype=int)
print (np_array)

np_array1 = np.array([1,2,3,4])
print (np_array1)

#insertion to array
my_array.insert(0,6)
print (my_array)

#traversal operation

from array import *
arr1 = array('i', [1,2,3,4,5,6])

def traverseArray(array):
    for i in array:
        print (i)

traverseArray(arr1)

#array traversal
def accessElement(array, index):
    if index >= len(array):
        print('there is not an element in this index')
    else:
        print(array[index])

accessElement(arr1, 3)
accessElement(arr1, 6)

#linear search in array

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return-1

print(linear_search(arr1, 3))

#deleting element in array

my_array1.remove(2)
print(my_array1)

