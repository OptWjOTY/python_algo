import random

# 4.1数组：数组是一种线性数据结构，将相同类型的元素存储在连续的内存空间中。将元素在数组中的位置称为该元素的索引。数组的长度是固定的。
# 4.4.1数组常用操作
## 1.初始化数组
## 可以根据需求选用数组的两种初始化方式：无初始值、给定初始值；在未指定初始值情况下，大多数编程语言会将数组元素
arr: list[int] = [1] * 5  # 声明数组，变量名称：类型 = 初始值
nums: list[int] = [1, 2, 3, 4, 5]


## 2.访问元素
## 数组元素被存储在连续的内存空间中，所以计算数组元素的内存地址非常容易。给定数组地址(首元素内存地址)和某个元素的索引
## 可以通过公式：元素内存地址 = 数组内存地址 + 元素长度*元素索引；元素索引本质上是内存地址的偏移量。
## 例如：   1  3  2  5  4
## 元素索引：0  1  2  3  4
## 内存地址：00 04 08 12 16
## 元素长度：4
### 数组中 5的内存地址为 012 = 000 + 4*3
# print(nums)
# for item in nums:
#     print("元素数据是：",item,",元素内存地址是：",id(item))
def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    # 在区间[0,len(nums)-1] 中随机抽取一个数字
    random_indx = random.randint(0, len(nums) - 1)
    return nums[random_indx]


## 3.插入元素
## 数组元素在内存中是“紧挨着的”，它们之间没有空间再存放任何数据。如果想在数组中间插入一个元素，则需要将该元素之后的所有元素都向后移动一位，之后再把元素赋值给该索引。
def insert_array(nums: list[int], num: int, index: int):
    """在数组的索引 index处插入 元素 num"""
    # 把索引 index以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num
    return nums


## 4.删除元素
## 如果想要删除索引i处的元素，则需要把索引i之后的所有元素都向前移动一位
def delete_array(nums: list[int], index: int):
    """删除索引index处的元素"""
    # 把索引 index以及之后的所有元素向后移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
    return nums


## 总的来看，数组的插入与删除操作有以下特点：
## 时间复杂度高：数组的插入和删除的平均时间复杂度为O(n),其中n为数组长度
## 丢失元素：由于数组的长度不可变，因此在插入元素后，超出数组长度的元素会丢失
## 内存浪费：可以初始化一个比较长的数组，只用前面一部分，在插入数据时，会丢失末尾的无意义数据，但是会造成空间浪费

## 5.遍历数组
## 可以通过索引遍历数组，也可以直接遍历获取数组中的每个元素：
def traverse(nums: list[int]):
    """遍历数组"""
    count = 0
    # 通过索引遍历数组 通过for循环遍历数组各个元素
    for i in range(0, len(nums) - 1, 1):
        count += nums[i]
    # 直接遍历数组元素
    for num in nums:
        count += num
    # 同时遍历数据索引和元素
    for i, num in enumerate(nums):
        count += nums[i]
        count += num

## 6.查找元素
## 因为在数组中查找指定元素需要遍历数组，每轮循环判断元素值是否匹配，匹配则输出对应索引
## 因为数组是线性结构，所以上述查找操作被称为“线性查找”

def find_arry(nums: list[int],idx: int):
    """查找某个元素是否在对应的数组中"""
    for i in range(len(nums)):
        if nums[i] == idx:
            return i,nums[i]
        # elif nums[i] != idx:
    return ("数据：{0}不在数组中".format(idx))

## 7.扩容数组
## 在大多数编程语言中 数组的长度都是不可改变的
## 如果要扩容数组，则需要重新建一个更大的数组，然后把原数组的各个元素依次复制到新数组。这是一个O(n)的操作，在数组很大的时候非常耗时

def move_array(nums: list[int],enlarge: int):
    """将现有的一个数组进行扩容，存入一个更大的数组"""
    count = 0
    enlarge = [0]*len(nums)+enlarge
    for i in range(len(nums)):
        enlarge[i] = nums[i]
        count += 1
    return enlarge

print(move_array(nums=[10, 20, 30, 40, 50],enlarge=5))
