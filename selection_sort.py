from tqdm import tqdm

def find_smalletst(arr):
    smallest = None
    smallest_index = None
    
    for i in range(len(arr)):
        if smallest is None or arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index


def selection_sort(arr):
    sorted_list = []
    
    for i in tqdm(range(len(arr))):
        s_index = find_smalletst(arr)
        sorted_list.append(arr.pop(s_index))
    
    return sorted_list

a = [i for i in range(10**4, 1, -1)]


b = selection_sort(a)
print(len(b), b[0], b[-1])