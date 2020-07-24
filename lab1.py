
import random
import math
import time
import random

def bSort(A):
    for j in range(1, len(A)):
        key = A[j]
        pos = BinSearch(A,0,j-1,key)
        A = A[:pos] + [key] + A[pos:j] + A[j+1:]
    return A



def insertionsort(A):
    for i in range(1, len(A)): 
        key = A[i] 
        j = i-1
        while j >=0 and key < A[j] : 
                A[j+1] = A[j] 
                j -= 1
        A[j+1] = key 
    return A


    

def BinSearch(A,p,q,x):
    if p > q:
            return p
    middle = (p+q)//2
    if x > A[middle]:
        return BinSearch(A,middle + 1,q,x)
    if x < A[middle]:
        return BinSearch(A,p,middle - 1,x)
    else:
        return middle

def imodmergesort(array,k):
    if len(array) > 1:
        if k < len(array):
            middle = math.floor(len(array)/2)
            return merge(imodmergesort(array[0:middle],k),imodmergesort(array[middle+1:],k))
        else:
            return insertionsort(array)
    else:
        return array



def bmodmergesort(array,k):
    if len(array) > 1:
        if k < len(array):
            middle = math.floor(len(array)/2)
            return merge(bmodmergesort(array[0:middle],k),bmodmergesort(array[middle+1:],k))
        else:
            return bSort(array)
    else:
        return array

    
    

def merge(left,right):
    result=[]
    x, y = 0, 0
    while x < len(left) and y < len(right):
        if left[x] <= right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1
    result += left[x:]
    result += right[y:]
    return result


def FULLTEST(A,n):
    if n <= 1: #FOR PRE-GENERATED ARRAYS
        print("Input array: ", A)
        start_time = time.perf_counter()
        bSortA = bSort(A)
        end_time = time.perf_counter()-start_time
        print("bSort: ", bSortA, " time: ", end_time)
        k = 0
        while k <= len(A):
            start_time = time.perf_counter()
            res = imodmergesort(A,k)
            end_time = time.perf_counter()-start_time
            print("Mergesort (INS): ", res, " k = ",k," time: ", time.perf_counter()-start_time)
            start_time = time.perf_counter()
            res = bmodmergesort(A,k)
            end_time = time.perf_counter()-start_time
            print("Mergesort (bSort): ", res, " k = ",k," time: ", time.perf_counter()-start_time)
            k += 1
    elif n > 1: #THIS IS FOR CUSTOM N SIZE GENERATED ARRAYS
        x = [0,2,6,12,20,25,50,90,150,350,600,1000]
        i=0
        while i < len(x):
            GenA = GENERATEARRAY(n,n)
            start_time = time.perf_counter()
            imodmergesort(GenA,x[i])
            end_time = time.perf_counter()-start_time
            print("Mergesort (INS): ", " k = ",x[i]," time: ", end_time)

            GenA = GENERATEARRAY(n,n)
            start_time = time.perf_counter()
            bmodmergesort(GenA,x[i])
            end_time = time.perf_counter()-start_time
            print("Mergesort (bSort): ", " k = ",x[i]," time: ", end_time)

            i += 1
        GenA = GENERATEARRAY(n,n)
        start_time = time.perf_counter()
        quickSort(GenA,0,len(GenA)-1)
        end_time = time.perf_counter()-start_time
        print("Quicksort :"," time: ", end_time)

    else:
        print("INVALID OPTION PARAMETER: x selects the use of existing arrays, x = 1. Or randomly generated big arrays, x = 2")

def GENERATEARRAY(length,max):
     A = []
     i = 0
     while i < length:
         A.append(random.randrange(0,max))
         i  += 1
     return A
    

def partition(arr,low,high): 
    i = ( low-1 ) 
    pivot = arr[high]
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 

            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 

        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    return

alreadysorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
almostsorted = [1,2,18,4,5,6,7,8,9,20,11,12,13,14,15,16,17,3,19,10]
randomarray = GENERATEARRAY(20,20)
print("\nTESTING ALREADY SORTED ARRAY: ")
FULLTEST(alreadysorted,1)
print("\nTESTING ALMOST SORTED ARRAY: ")
FULLTEST(almostsorted,1)
print("\nTESTING RANDOMLY GENERATED ARRAY: ")
FULLTEST(randomarray,1)
print("\nTESTING RANDOMLY GENERATED BIG ARRAY (n = 10000): ")
FULLTEST(0,10000)
print("\nTESTING ON GENERATED MASSIVE ARRAY (n = 1 000 000 might take a minute or two) : ")
FULLTEST(0,1000000)

print("\nOne last test of n = 1 000 000 and k = 27 bSort vs Quicksort: ")
GenA = GENERATEARRAY(1000000,1000000)
start_time = time.perf_counter()
bmodmergesort(GenA,27)
end_time = time.perf_counter()-start_time
print("Mergesort (bSort): ", " k = ",27," time: ", end_time)

GenA = GENERATEARRAY(1000000,1000000)
start_time = time.perf_counter()
quickSort(GenA,0,len(GenA)-1)
end_time = time.perf_counter()-start_time
print("Quicksort: "," time: ", end_time)
