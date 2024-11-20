# 2.2.1迭代
### 迭代是一种重复执行某个任务的控制结构。会在满足一定的条件下重复执行某段代码，直到条件不再满足。
#### 1.for 循环 适合在预先知道迭代的次数时使用。
# 求 1 + 2 +...+n的和 思考：如何计算？ 给定一个n值，计算1-n的和，首先需要声明一个初始值 res 用于存储每一次的计算结果；
# 那么如何判断计算是否在n以内呢？需要指定另一个变量 i ，每一次做完加法后，对该变量+1，+1后的值用于判断是否在n以内。
def for_loop(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i  # 等同于 res = res + i
        # res = res + i
    return res

#### 2.while循环 while循环比for循环自由度更高
def while_loop(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1 # 这一步相当于声明间隔步骤
    return res

# 如果想计算 1- n之间偶数的和呢？
def while_loop_en(n: int) -> int:
    res = 0
    i = 0
    while i <= n:
        res += i
        i += 2
    return res

#### 3.嵌套循环 可以在循环内部再嵌套一个循环结构
def nested_for_loop(n : int) -> str:
    res = ""
    for i in range(1,n+1):
        for j in range(1,n+1):
            res += f"({i},{j}),"
            resa = i +j
    return res,resa

# 2.2.2递归
### 递归是一种方法策略，通过函数调用自身来解决问题，主要包含两个阶段
### 1：递（程序不断地调用自身，通常传入更小或更简化的参数，直到达到“终止条件”;
### 2：归（触发终止条件后，程序从最深层的递归函数开始逐层返回，汇聚每一层的结果）
### 递归通常包含三个要素：
#### 1、终止条件：用于决定什么时候由“递”转“归”；
#### 2、递归调用：对应“递”，函数调用自身，通常输入更小或更简化的参数
#### 3、返回结果：对应“归”，将当前递归层级的结果返回至上一层

def recur(n : int) ->int:
    if n==1:
        return 1
    res = recur(n - 1)
    return n+res
# print(recur(5))

#### 迭代：“自下而上”的解决问题。从最基础的步骤开始，不断重复或累加完成这些步骤，直到任务完成；
#### 递归：“自下而上”的解决问题。将原问题分为更小的子问题，子问题和原问题具有相同的形式。接下来将子问题继续分为更小的问题，直到基本情况时停止。
##### 1、调用栈 递归函数每次调用自身时，系统都会为新开启的函数分配内存，以存储局部变量、调用地址和其他信息，这将导致两方面结果：
######      ①函数的上下文数据都存储在称为“栈帧空间”的内存区域中，直至函数返回后才会被释放。因此，递归通常比迭代更耗费内存空间。
######      ②递归调用函数会产生额外的开销。因此递归通常比循环的时间效率更低。递归深度通常是有限的，过身的递归可能导致栈溢出错误；


#### 2、尾递归：如果函数在返回前的最后一步才进行递归调用，则该函数可以被编译器或者解释器优化，使其在空间效率上与迭代相当。称为尾迭代。
###### 普通递归：当函数返回到上一层级的函数后，需要继续执行代码，因此系统需要保存上一层调用的上下文。
###### 尾递归：递归调用是函数返回前的最后一个操作，这意味着函数返回到上一层级后，无须继续执行其他操作，因此系统无需保存上一层函数的上下文。

def tail_recur(n : int,res: int) -> (int,int):
    if n== 0:
        return res
    return tail_recur( n -1,res + n)
# print(tail_recur(2,5))

# 输入 2，5 ;当n等于2时，返回 函数tail_recur(2-1,5+2) -> tail_recur(1,7)
## 那么tail_recur(1,7)的值仍然需要递进原函数求值 当n等于1的时候，返回 tail_recur(0,8)
## 求tail_recur(0,8),当n等于0，res等于8的时候，返回res得到 8，最终返回8

### 3.递归树 当处理“分治”相关的算法问题时，递归往往比迭代的思路更加直观、代码更加易读。
#### 以“斐波那契”数列为例 给定一个斐波那契数列0,1,1,2,3,5,8,13...求该数列的第n个数字。
#### 设斐波那契的第n个数为f(n),易得到两个结论
##### ①数列的前两个数字f(1)=0,f(2)=1
##### ②数列中的每个数字是前两个数字的和，即f(n) = f(n-1) +f(n-2)
def leFibanacci(n: int) -> int:

    if n==1 or n==2:
        return n-1
    return  leFibanacci(n-1) + leFibanacci(n-2)


#### 递归适合处理链表、树和图相关问题，因为他们非常适合用分治思维进行分析


def for_loop_recur(n: int) -> int:
    """使用迭代模拟递归"""
    # 使用一个显式的栈来模拟系统调用栈
    stack = []
    res = 0
    # 递：递归调用
    for i in range(n, 0, -1):
        # 通过“入栈操作”模拟“递”
        stack.append(i)
    # 归：返回结果
    while stack:
        # 通过“出栈操作”模拟“归”
        res += stack.pop()
    # res = 1+2+3+...+n
    return res

# 2.3时间复杂度
## 运行时间可以直观且准确的反应算法的效率。可通过以下步骤预估代码运行时间
### ① 确定运行平台 、② 评估各种计算操作所需的运行时间、③ 统计代码中所有的操作。

## 2.3.1 统计时间增长趋势
### 时间复杂度分析统计的不是算法运行时间,而是算法运行时间随着数据量变大时的增长趋势
### 常数阶时间复杂度：算法运行时间不随着n增大而增大
### 线性阶时间复杂度：算法运行时间随着n增大而线性增长
### 常数阶时间复杂度：算法运行时间与输入n无关

def algorithm(n: int) -> int:
    a = 1
    a +=n
    for i in range(5*n + 1):
        print(0)
    for i in range(2*n):
        print(1)
## 2.3.2 函数渐近上界：将线性的时间复杂度记为O(n),这个数学符号称为大O记号，表示函数T(n)的渐近上界。
### 时间复杂度本质上是计算“操作数量T(n)”的渐近上界，具有明确的数学定义；
### 函数渐近上界：若存在正实数c和实数n0，使得对于所有的n>n0,均有 T(n)<=c*f(n),则可认为f(n)给出了T(n)的一个渐近上界，记为：T(n) = O(f(n))

## 2.3.3推算方法
### 根据定义,确定f(n)之后,便可以得到时间复杂度O(f(n))。如何确定f(n)?
### 分为两步：一、首先统计操作数量；二、判断渐近上界

#### 1、第一步：统计操作数量
##### 针对代码，逐行从上到下计算即可。然而，由于c*f(n)中的c可大可小，因此操作数量T(n)中的各种系数、常数项都可以忽略。由以下计算技巧：
##### 1.忽略T(n)中的常数项。因为它们都与n无关，对时间复杂度不产生影响。
##### 2.省略所有系数。例如：2n、4n+1，都可以简化记为n次，n前面的系数不产生影响
##### 3.循环嵌套时使用乘法。总操作数量等于外层循环和内层循环的操作数量之积，每一层循环依然可以套用第1、2点运算技巧

#### 2、第二步：判断渐近上界
##### 时间复杂度由T(n)中最高项来决定。

## 2.3.4常见类型
##### 设输入数据大小为n，常见时间复杂度为O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(2^n)<O(n!)
##### 1.常数阶O(1) 常数阶的操作数量与输入数据大小n无关，即不随着n的变化而变化
def constant(n: int) -> int:
    """常数阶"""
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count
##### 2.线性阶O(n) 线性阶的操作数量与相对于输入大小n以线性级别增长。线性阶通常出现在单层循环中
def linear(n : int) -> int:
    '''线性阶'''
    count = 0
    for _ in range(n):
        count += 1
    return count

def array_traversal(nums : list[int]) ->int:
    '''线性阶(遍历数组)'''
    count = 0
    for num in nums:
        count += 1
    return count

##### 3.平方阶O(n^2) 平方阶的操作数量相对于输入数据大小n以平方级别增长。平方阶通常出现在嵌套循环中，外层循环和内存循环的时间复杂度都为O(n),因此总体的时间复杂度为O(n^2)
def quardratic(n : int) ->int:
    '''平方阶'''
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

##### 以冒泡排序为例，外层循环执行n-1次，内层循环执行n-1,n-2,...,2,1次，平均为n/2次，因此时间复杂度为O((n-1)n/2)=O(n^2)
def bubble_sort(nums : list[int]) -> int:
    '''平方阶(冒泡排序)'''
    count = 0
    #外循环：未排序区间为[0,i]
    for i in range(len(nums) - 1,0,-1):
        #内循环：将未排序区间[0,i]中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j]>nums[j+1]:
                # 交换nums[j]和nums[j+1]
                tmp : int = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                count += 3
    return count
print(bubble_sort([2,8,64,85,0]))
##### 4.指数阶O(2^n)
def exponential(n:int) -> int:
    '''指数阶 (循环实现)'''
    count = 0
    base = 1
    for _ in range(n):
        for _ in range (base):
            count += 1
        base *= 2
    return count

##### 5.对数阶O(logn)
##### 与指数相反，对数阶反映了“每轮缩减到一半”的情况。设输入数据大小为n，由于每轮缩减到一半，因此循环次数是log2n,即2^n的反函数
def logarithmic(n:int) -> int:
    '''对数阶(循环实现)'''
    count = 0
    while n>1:
        n = n/2
        count += 1
    return count

def log_recur(n : int) -> int:
    '''对数阶(递归实现)'''
    if n<=1:
        return 0
    return log_recur(n / 2) + 1

##### 6.线性对数O(nlogn)
def linear_log_cur(n : int) -> int:
    '''线性对阶'''
    if n<=1:
        return 1
    # 一分为二，子问题的规模减少一半
    count = linear_log_cur(n // 2 ) + linear_log_cur(n // 2)
    # 当前子问题包含n个操作
    for _ in range(n):
        count += 1
    return count

##### 6.阶乘阶O(n!)
def factorial_recur(n : int) ->int:
    '''阶乘阶(递归实现)'''
    if n==0:
        return 1
    count = 0
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count

### 2.3.5最差、最佳、平均时间复杂度
#### 算法的时间往往是不固定的，而是与输入数据的分布有关。假设输入一个长度为n的数组 nums,
print(factorial_recur(4))

