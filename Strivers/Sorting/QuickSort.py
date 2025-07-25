def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i >= j: 
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[low], arr[j] = arr[j], arr[low]
    return j    
    
def quicksort(arr, low, high): 
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
    
    return arr

def main():
    arr = [7, 4, 1, 5, 3]
    sorted_arr = quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()