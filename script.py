import time

def quickSort(ml):
    if len(ml) < 2:
        return ml
    pivot = ml[0]
    less = [i for i in ml if i < pivot]
    greater = [i for i in ml if i > pivot]
    
    return quickSort(less) + [pivot] + quickSort(greater)

def bubbleSort(ml):
    if len(ml) < 2:
        return ml
    for i in range(len(ml)):
        for j in range(len(ml) - 1 - i):
            if ml[j] > ml[j + 1]:
                ml[j], ml[j + 1] = ml[j + 1], ml[j]
    return ml

def read_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def main():
    filename = 'data.txt'
    data = read_from_file(filename)
    ml = list(data)

    start = time.time()
    bubble_sorted = bubbleSort(ml)
    end = time.time()
    print("Bubble sort:", bubble_sorted)
    print("Duration of bubble sort:", end - start)

    start = time.time()
    quick_sorted = quickSort(ml)
    end = time.time()
    print("Quick sort:", quick_sorted)
    print("Duration of quick sort:", end - start)

if __name__ == "__main__":
    main()

