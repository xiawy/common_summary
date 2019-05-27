

# -------------------------- 顺序查找 ---------------------------
# 描述：从第一个元素开始逐个与查找的元素进行比较，当元素相同时返回对应元素的下标，如果到
#      最后都没有找到，则返回-1
# 缺点：当N很大时，平均查找查找长度较大、效率低
# 优点：对表中数据元素的存储没有要求。对于线性链表，只能进行顺序查找
def sequential_search(array, key):
    length = len(array)
    for i in range(length):
        if array[i] == key:
            return i
        return False


# ------------------------- 二分查找(折半) ------------------------------
# 描述：一种在有序数组中查找某一特定元素的查找算法。查找过程从数组中间元素开始每次范围缩小一半
# 优点：查找速度较快，每次搜索区域减少一半，时间复杂度为O(logn)，
# 缺点：数组必须是有顺序的
def binary_search(array, key):
    low, high, time = 0, len(array) - 1, 0
    while low < high:
        mid = int((low + high) / 2)
        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid
    return False


# ------------------------ 插值查找 -------------------------------------
# 描述：基于二分查找算法，将查找点的选择改进为自适应选择，一定程度上提高查找效率
# 优点：对于数据较大，且分布均匀时插值查找算法的平均性能要优于折半查找，O(log log n) < 时间复杂度 <O(n)
# 缺点：插值查找也是有序查找
# 比较：差值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的查找方法，其核心就在于
#      插值的计算公示(key-a[low])/(a[high]-a[low])*(high-low)
def interpolation_search(array, key):
    low, high, time = 0, len(array) - 1, 0
    while low < high:
        mid = low + int((high-low) * (key-array[low])/(array[high]-array[low]))
        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid
    return False


# -------------------------- 斐波那契数列 -----------------------------------
# 描述：斐波那契查找就是在二分查找的基础上根据斐波那契数列进行分割
def fib_search(array, key):
    if key < array[0] or key > array[-1]:
        return -1

    def fib_func(n):
        prev, curr = 0, 1
        while n > 0:
            n -= 1
            yield curr
            prev, curr = curr, prev + curr
    fib_list = [i for i in fib_func(len(array))]

    # 获取array长度在fib_list中的位置
    k, n = 0, len(array)
    while n > fib_list[k]:
        k += 1

    # 数组长度不会刚好等于fib的数据，须填充
    for i in range(n, fib_list[k]):
        array.append(array[-1])

    low, high = 0, fib_list[k]
    while low <= high:
        mid = low + fib_list[k-1]  # fib_search[k] == array[-1]
        if key < array[mid]:
            high = mid - 1
            k -= 1
        elif key > array[mid]:
            low = mid + 1
            k -= 2
        else:
            return mid

    return -1
