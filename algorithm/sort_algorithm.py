

# --------------------------- 冒泡排序 （交换排序） ----------------------------
# 冒泡排序：冒泡排序是稳定的
# 实现思路：使用双重for循环，内层变量为i，外层为j，在内层循环中不断的比较相邻的两个值
#         （i，i+1）的大小，如果i+1的值大于i的值，两者交换位置。
# 思想：拿待排序位置的数与列表中每个数比较，小于就互换位置。即将数据较大的不断后移
def bubble_sort(arr):
    n = len(arr)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


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
        quick_sort_inplace(array, pivot+1, end)


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


a = [36, 65, 5, 12]
quick_sort_inplace(a, 0, len(a) - 1)


# ------------------------------- 插入排序 -----------------------------------
# 插入排序：插入排序是稳定的
# 实现思路：与前面的每一个数进行比较，如果前面的数更大则将对应位置的数不断后移，直到找到
#          一个数小于待排序数为止。
# 优点：对几乎已经排好序的数据操作时，效率高，既可以达到线性排序的效果
# 缺点：一般来说效率较低，因为每次只能将数据移动一位
def insert_sort(array):
    for i in range(1, len(array)):
        index = array[i]
        j = i - 1
        while j >= 0 and array[j] > index:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = index


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
                if array[j] < array[j-gap]:
                    array[j], array[j-gap] = array[j-gap], array[j]
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
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = i
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index]


# ------------------------------ 堆排序 ------------------------------------
# 堆排序：利用堆来进行排序（堆是一种完全二叉树），时间复杂度为O(nlogn)
# 堆的定义：N个元素的系列{K1,K2,K3...}当且仅当满足下列关系之一时称之为堆。
#          1、ki <= k2i 且ki <= k2i+1 （最小化堆或小顶堆）
# 　　      2、ki >= k2i 且ki >= k2i+1 （最大化堆或大顶堆）
#           其中i = 1,2,3,4..n/2向下取整
#          堆是一个完全二叉树。所有非终端结点的均值不大于（或不小于）其左右孩子结点的值。
#         堆顶元素（完全二叉树的根）必为系列中的最大或者最小值。
# 基本思想：1、将初始化待排序关键子序列(R1,R2....Rn)构建成大顶堆，此堆为初始化无序区。
#          2、将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,......
#             Rn-1)和新的有序区（Rn），且满足R[1,2...n-1]<=R[n]
#          3、由于交换后新的堆顶R[1]可能违反堆的性质，因此需要多当前无序区(R1,R2,......
#             Rn-1)调整为新堆，然后再次R[1]与无序区最后一个元素交换，得到新的无序区(R1,
#             R2....Rn-2)和新的有序区（Rn-1,Rn）。不断重复此过程直到有序区的元素个数为
#             n-1,则整个排序过程完成。
def fix_down(array, start, end):
    index = start
    while True:
        child = 2*index + 1
        if child > end:
            break
        if child+1 <= end and array[child] < array[child+1]:
            child += 1
        if array[index] < array[child]:
            array[index], array[child] = array[child], array[index]
            index = child
        else:
            break


def heap_sort(array):
    first = len(array)//2 - 1
    for start in range(first, -1, -1):
        fix_down(array, start, len(array)-1)

    for end in range(len(array) - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        fix_down(array, 0, end-1)
