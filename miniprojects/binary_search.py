#Time comparison for regular and binary search
#Regular search - looping over the list to find the index of an element if it exists else -1
import random
import time

def normal_search(num_list, find_num):
    for index,num in enumerate(num_list):
        if num == find_num:
            return index
    return -1

#Binary search using divide and conquer. used when there is an ordered list, so we sort before calling the function

def binary_search(num_list, find_num,low = None,high = None):
    #initializations
    if low is None:
        low = 0
    if high is None:
        high = len(num_list)-1
    #if element not in list, we keep calling functions increasing high and low values,
    # at some point, right bound may become smaller as we do midpoint-1 - we stop at that point
    if high < low:
        return -1
    # use // so that we get a proper index for odd num of elements
    midpoint = (low+high)//2

    #base case
    if num_list[midpoint] == find_num:
        return midpoint

    elif num_list[midpoint] > find_num:       #left of the array
        return binary_search(num_list,find_num,low,midpoint-1)
    else:               #right of the array
        return binary_search(num_list,find_num,midpoint+1,high)

if __name__ == "__main__":
    # size = int(input ("Enter the size of the list: "))
    # num_list = []
    # for i in range(size):
    #     num_list.append(int(input("Enter the element: ")))
    # find_num = int(input("Enter the element to be found: "))
    # num_list = sorted(num_list)
    # print(normal_search(num_list,find_num))
    # print(binary_search(num_list,find_num))

    #build a larger size list and finf the time taken by both logics

    size = 10000
    num_list = set()
    while len(num_list) < size:
        num_list.add(random.randint(-3*size, 3*size))  #just say any range to pick numbers from
    num_list = sorted(list(num_list))

    #time computation to find every element in the list in both methods to show binary search is faster
    start = time.time()
    for find_num in num_list:
        normal_search(num_list, find_num)
    end = time.time()
    print("Normal search time: ",((end-start)/size)*10**6, "microsseconds")

    start = time.time()
    for find_num in num_list:
        binary_search(num_list, find_num)
    end = time.time()
    print("Binary search time: ", ((end - start) / size)*10**6, "microseconds")



