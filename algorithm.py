

# --------------------------- 冒泡排序 （交换排序） ----------------------------
# 冒泡排序：冒泡排序是稳定的
# 实现思路：使用双重for循环，内层变量为i，外层为j，在内层循环中不断的比较相邻的两个值
#         （i，i+1）的大小，如果i+1的值大于i的值，两者交换位置。
# 思想：拿待排序位置的数与列表中每个数比较，小于就互换位置。即将数据较大的不断后移
def bubble_sort(arr):
    n = len(arr)
    for j in range(0, n-1):
        for i in range(0, n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


bubble_sort([5, 10, 45, 6, 0, 2])

# 第一次循环后：[5, 10, 6, 0, 2, 45]
# 第二次循环后：[5, 6, 0, 2, 10, 45]
# .....


# ------------------------------- 快速排序 （交换排序） ------------------------
# 快速排序
# 实现思路：快排是排序速度最快的算法，采用的是分而治之的策略，把数组递归成只有单个元素的数组
#          之后再不断两两进行合并，最后得到一个有序数组。

# 方法一：
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()
    less = [i for i in array if i <= pivot]
    greater = [i for i in array if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


# 方法二：
# 修改：1、不再使用额外的存储空间，实现原地排序
#      2、修改每次都遍历两个数组，改为每次只遍历一个数组。
def quick_sort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quick_sort_inplace(array, beg, pivot)
        quick_sort_inplace(array, pivot + 1, end)


def partition(array, beg, end):
    pivot_index = beg
    pivot, left, right = array[pivot_index], pivot_index + 1, end - 1
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


# ------------------------------- 插入排序 -----------------------------------
# 插入排序：插入排序是稳定的
# 实现思路：与前面的每一个数进行比较，如果前面的数更大则将对应位置的数不断后移，直到找到
#          一个数小于待排序数为止。
# 优点：对几乎已经排好序的数据操作时，效率高，既可以达到线性排序的效果
# 缺点：一般来说效率较低，因为每次只能将数据移动一位
def insert_sort(a):
    for i in range(1, len(a)):
        index = a[i]
        j = i - 1
        while j >= 0 and a[j] > index:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = index


# ------------------------------- 希尔排序 ------------------------------
# 希尔排序：非稳定排序算法
# 算法思路：将待排序的数组元素按下标的一定增量分组，分成多个子序列，然后对各个子序列进行直接
#          插入排序算法排序；然后依次缩减增量再进行排序，直到增量为1时，进行最后一次直接插
#          入排序。
def shell_sort(array):
    n = len(array)
    gap = n >> 1
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]
                else:
                    break
        gap >>= 1          # 相当于 gap = gap >> 1


# ------------------------------- 选择排序 -------------------------------
# 选择排序：最直观的一种排序方式
# 排序思路：首先在未排序中找到最小元素，存放在排序序列的起始位置，然后，再从剩余未排序元素中
#          找到最小元素放在一排序的末尾
def select_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = i
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index]


i = 100
while i > 0:
    print(i)
    i >>= 1