from typing import Optional

from linkList_study import ListNode

## 5.1栈 栈是一种遵循先入后出逻辑的线性数据结构。
## 堆叠元素的顶部称为“栈顶”，底部称为“栈底”。将元素添加到栈顶的操作叫做“入栈”，删除栈顶元素的操作叫做“出栈”
## 5.1.1 栈的常用操作 ： 元素入栈(添加至栈顶)、栈顶元素出栈、访问栈顶元素
## 在python中可将list当作栈来使用

stack: list[int] = []
# 元素入栈
stack.append(1)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(8)

# 访问栈顶元素
peek: int = stack[-1]

# 元素出栈
pop: int = stack.pop()  # 默认删除最后一个数，并返回最后一个数

# 获取栈的长度
size: int = len(stack)

# 判断是否为空
is_empty: bool = len(stack) == 0

if __name__ == "__main__":
    # 初始化栈
    stack = []

    # 元素入栈
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(10)
    print("栈是：", stack)

    # 访问栈顶元素
    peek = stack[-1]
    print("栈顶元素是：", peek)

    # 元素出栈
    pop = stack.pop()
    """
    Remove and return item at index (default last).

    Raises IndexError if list is empty or index is out of range.
    """
    print("出栈元素是：", pop)
    print("元素出栈后栈是：", stack)

    # 获取栈的长度
    size = len(stack)
    print("栈长度是：", size)

    # 判断是否为空
    is_empty = len(stack) == 0
    print("栈是否为空：", is_empty)
