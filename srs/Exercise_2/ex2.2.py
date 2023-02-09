'''Exercise 2.2: testing the quicksort algorithim'''


import json
import requests
import timeit
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data into a Python object
    data = json.loads(response.text)
else:
    print("Failed to load JSON data.")


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high




time_list = []
len_list = []

for index in range(10):
    upper = len(data[index])-1
    len_list.append(upper + 1)

    temp = timeit.timeit(lambda: func1(data[index], 0, upper), number = 1)
    time_list.append(temp)

plt.plot(len_list, time_list)
plt.xlabel("Lenght of array/list (n)")
plt.ylabel("Time (s)")
plt.title("funct1, lenght of array V.S. time")
plt.show()