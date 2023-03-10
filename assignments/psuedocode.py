'''
N^2
def bubbleSort(list)
    for i = 0 to list.length - 1
        for j = 0 to list.length - i - 1
            if list[j] > list[j + 1]
                swap(list[j], list[j + 1])



N log N
def quickSort(list, left, right)
    if left < right
        pivotIndex = partition(list, left, right)
        quickSort(list, left, pivotIndex)
        quickSort(list, pivotIndex + 1, right)

procedure partition(list, left, right)
    pivot = list[right]
    i = left - 1
    for j = left to right - 1
        if list[j] <= pivot
            i = i + 1
            swap(list[i], list[j])
    swap(list[i + 1], list[right])
    return i + 1




N+K
def countingSort(list)
    max = findMax(list)
    count = new array of size max + 1
    for i = 0 to list.length - 1
        count[list[i]] = count[list[i]] + 1
    for i = 1 to max
        count[i] = count[i] + count[i - 1]
    output = new array of size list.length
    for i = list.length - 1 to 0
        output[count[list[i]] - 1] = list[i]
        count[list[i]] = count[list[i]] - 1
    return output




Bogosort
def bogosort(list)
    while not is_sorted(list)
        list = shuffle(list)
    return list

'''
##Search
'''
def hash_table_search(hash_table,key):
  return hash_table[key]


def linear_search(arr,key):
  n = len(n)
  for i in range(n):
    if arr[i]==key:
      return i
  return -1

def binary_search(arr,key):
  low=0
  high=len(arr)-1
  while high-low>1:
    mid=(high + low)//2
    if arr[mid]<key:
      low = mid+1
    else:
      high = mid 
    if arr[low]==key:
      return low
    elif arr[high]==key:
      return high
    else:
      return -1


'''

