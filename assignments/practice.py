
def bogo_sort(a):
    n = len(a)
    while not is_sorted(a):
        shuffle(a)


def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False

    return True


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]




def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2

##non comparison 
def count_sort(arr):
    n = len(arr)
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(n)]
    for i in range(n):
        count_arr[arr[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(n - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(n):
        arr[i] = output_arr[i]



def bucket_sort(arr):
    n = len(arr)
    num_buckets = 10
    temp = []
    for i in range(num_buckets):
        temp.append([])
    for j in arr:
        index_b = int(j * num_buckets / n)
        temp[index_b].append(j)
    for i in range(num_buckets):
        insertion_sort(temp[i])
    k = 0
    for i in range(num_buckets):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingsort_for_radixsort(arr, exp)
        exp *= 10


def countingsort_for_radixsort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


##
def stooge_sort(arr, low, high):
    if low >= high:
        return
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if high - low + 1 > 2:
        third = int((high - low + 1) / 3)
        stooge_sort(arr, low, high - third)
        stooge_sort(arr, low + third, high)
        stooge_sort(arr, low, high - third)


def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

