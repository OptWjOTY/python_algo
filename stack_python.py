from typing import Optional

## 5.1.2 栈的实现
## 栈遵循先入后出的原则，因此只能在栈顶添加或删除元素。然而，数组和链表都可以在任意位置添加和删除元素，因此栈可以视为一种受限制的数组或链表。
## 基于链表的实现
## 使用链表实现栈时，可以将链表的头节点视为栈顶，尾节点视为栈底；
## 对于入栈操作，将元素插入链表头部，这种插入方法称为“头插法”；
## 对于出栈操作，只需将头节点从链表中删除即可；

## 以下基于链表实现栈

class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.var: int = val  # 节点值
        self.next: Optional[ListNode] = None  # 模拟指针值
class LinkedListStack:
    """基于链表实现的栈"""

    def __init__(self):
        """构造方法"""
        self._peek: Optional[ListNode] = None
        self._size: int = 0

    def size(self) -> int:
        """获取栈长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断是否为空"""
        return self._size == 0

    def push(self, val: int):
        """入栈"""
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        """出栈"""
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    def to_list(self) -> list[int]:
        """转化为列表，用于打印"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


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

    print(LinkedListStack.to_list(stack))
