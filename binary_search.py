def binary_search(list, number):
    low = 0
    high = len(list) - 1
    step = 0
    
    while low <= high:
        step += 1
        mid = (low + high) // 2
        guess = list[mid]

        if guess == number:
            return mid, step
        elif guess < number:
            low = mid + 1
        else: 
            high = mid - 1
        
    return None, step

import time


my_list = [i for i in range(1, 1_000_001)]
print(binary_search(my_list, 1000_000))