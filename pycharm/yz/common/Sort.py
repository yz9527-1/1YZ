##coding=utf-8



class Sort():
    """各种排序方法"""


    def bubble_sort(list1):
        """冒泡排序"""
        # 第一层for表示循环的遍数
        for i in range(len(list1)-1):

        # 第二层for表示具体比较哪两个元素
            for j in range(len(list1)-1-i):

        # 如果前面的大于后面的，则交换这两个元素的位置
                if list1[j] > list1[j+1]:
                    list1[j],list1[j+1]=list1[j+1],list1[j]

        return  list1

    def insertion_sort(list1):
        """插入排序"""
        # 第一层for表示循环插入的遍数
        for i in range(1, len(list1)):
            # 设置当前需要插入的元素
            current = list1[i]
            # 与当前元素比较的比较元素
            pre_index = i - 1
            while pre_index >= 0 and list1[pre_index] > current:
                # 当比较元素大于当前元素则把比较元素后移
                list1[pre_index + 1] = list1[pre_index]
                # 往前选择下一个比较元素
                pre_index -= 1
            # 当比较元素小于当前元素，则将当前元素插入在 其后面
            list1[pre_index + 1] = current

        return list1

    def quick_sort(arr):
        """快速排序"""
        if len(arr) < 2:
            return arr
        # 选取基准，随便选哪个都可以，选中间的便于理解
        mid = arr[len(arr) // 2]
        # 定义基准值左右两个数列
        left, right = [], []
        # 从原始数组中移除基准值
        arr.remove(mid)
        for item in arr:
            # 大于基准值放右边
            if item > mid:
                right.append(item)
            else:
                # 小于基准值放左边
                left.append(item)
        # 使用迭代进行比较
        return Sort.quick_sort(left) + [mid] + Sort.quick_sort(right)