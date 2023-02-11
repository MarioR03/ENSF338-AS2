import random
import json
import requests
import timeit
import sys
import matplotlib.pyplot as plt
import json
sys.setrecursionlimit(20000)

url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
# Load the JSON data into a Python object
    data = json.loads(response.text)
else:
    print("Failed to load JSON data.")


def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[int(end - start)]
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

# Example usage

data = [shuffle_list(x) for x in data]

time_list = []
len_list = []

for index in range(10):
    upper = len(data[index])-1
    len_list.append(upper + 1)
    print(upper+1)
    temp = timeit.timeit(lambda: func1(data[index], 0, upper), number = 1)
    time_list.append(temp)

with open('ex2.5.json', 'w') as file:
    json.dump(data, file)

plt.plot(len_list, time_list)
plt.xlabel("Lenght of array/list (n)")
plt.ylabel("Time (s)")
plt.title("funct1, lenght of array V.S. time- RANDOM")
plt.show()