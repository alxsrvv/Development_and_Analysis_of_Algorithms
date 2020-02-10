import random
import os

class Sort:

    def bubble(self, array):
        #worst - n^2
        #best - 1
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def selection(self, array):
        #worst - n^2
        #best - n^2
        for i in range(len(array)):
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[min_idx] > array[j]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
        return array

    def insertion(self, array):
        #worst - n^2
        #best - n
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array
arr = []
file = open("input.txt")
for line in file.readlines():
    line = line.rsplit('\n')
    arr.append(int(line[0]))
print(arr)
s = Sort()
arr = s.insertion(arr)
print(arr)