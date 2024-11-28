## 列表
## 列表(list)是一个抽象的数据结构概念，表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作；不用考虑容量限制的问题，列表可以基于数组或者链表实现；
## 链表天然可以看作一个列表，其支持元素增删改查，并且可以灵活扩容
## 数组也支持元素增删查改，但由于其长度不可变，只能看作一个具有长度限制的列表。
## 通过数组实现列表由于长度不可变会导致列表的实用性降低。可以通过动态数组来实现列表。

## 4.3.1列表常用操作
## 1、初始化列表：有初始值初始化和无初始值初始化两种初始化方法；
## 无初始值初始化
nums1: list[int] = []
## 有初始值初始化
nums: list[int] = [1, 2, 3, 4, 5]

## 2.访问元素
## 列表本质上是数组。因此可以在O(1)时间内访问和更新元素，效率高；
num: int = nums[1]
nums[1] = 0

## 3.插入与删除元素
## 相较于数组，列表可以自由地添加与删除元素。在列表尾部添加元素的时间复杂度为O(1),但插入和删除元素的效率仍与数组相同，时间复杂度为O(n)

# 清空列表
nums.clear()
# 在尾部添加元素
nums.append(1)
nums.append(10)
nums.append(2)
nums.append(20)
# 在指定索引位置插入元素
nums.insert(2, 100)
# 删除指定索引处元素
nums.pop(1)
# print(nums)
## 4.遍历列表
## 与数组一样，列表可以根据索引遍历，也可以直接遍历各元素

count = 0
for i in range(len(nums)):
    """通过索引位置遍历"""
    count += nums[i]
for i in nums:
    """直接遍历所有元素输出"""
    count = i

## 5.拼接列表
## 拼接两个列表
nums1: list[int] = [200, 400, 600]
nums += nums1  # 拼接nums1到nums后面
## 6.排序列表
## 完成列表排序后，我们便可以使用在数组类算法中常考题目“二分查找”和“双指针”算法。

nums.sort()
# print(nums)


## 列表设计主要包含以下三个重点：
## 1、初始容量：选取一个合理的数组初始容量
## 2、数量记录：声明一个变量size，用于记录列表当前元素数量。并伴随着元素插入和删除实时更新
## 3、扩容机制：若插入元素时列表容量已满，则需要进行扩容

class MyList:
    def __init__(self):
        """构造方法"""
        self._capacity: int = 10 #列表容量
        self._arr: list[int] = [0] * self._capacity #数组(存储列表元素)
        self._size: int = 0 #列表长度(当前元素数量)
        self._extend_ratio: int = 2 #每次列表扩容的倍数

    def size(self) -> int:
        """获取当前列表长度(当前元素数量)"""
        return self._size
    def capacity(self) ->int:
        """获取列表容量"""
        return self._capacity
    def get(self,index: int)->int:
        """访问元素"""
        #索引如果越界则抛出异常
        if index <0 or index >=self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    def set(self,num:int,index:int):
        """更新元素"""
        if index <0 or index >=self._size:
            raise IndexError("索引越界")
        self._arr[index] = num
    def add(self,num : int):
        """在尾部添加元素"""
        #元素超长时，触发扩容机制
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size +=1
    def insert(self,num: int, index: int):
        """在中间插入元素"""
        if index<0 or index >= self._size:
            raise IndexError("索引越界")
        # 元素数量超出容量时，触发扩容机制
        if self._size == self.capacity():
            self.extend_capacity()
        # 将索引 index 以及之后的元素都向后移动一位
        for j in range(self._size - 1,index -1,-1):
            self._arr[j+1] = self._arr[j]
        self._arr[index] = num

        #更新元素数量
        self._size +=1

    def remove(self,index: int):
        """删除某个元素"""
        if index <0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        # 将索引位之后的元素向前移动一位
        for j in range(index -1,self._size-1,1):
            self._arr[j] = self._arr[j+1]
            # 更新元素数量
        self._size +=1
        return num

    def extend_capacity(self):
        """列表扩容"""
        # 新建一个长度为原数组 _extend_ratio 倍的新数组，并将原数组复制到新数组
        self._arr = self._arr + [0]*self.capacity()*(self._extend_ratio -1)
        self._capacity = len(self._arr)

    def to_arr(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[:self._size]

a = MyList()
a.add(1)
print(a)

