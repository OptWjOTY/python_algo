class Storage:
    def __init__(self, capacity):
        self._capacity = capacity  # 受保护的属性，表示存储的容量
        self.items = []  # 公开的属性，表示存储的物品

    def add_item(self, item):
        if len(self.items) < self._capacity:
            self.items.append(item)
        else:
            print("Storage is full!")

    # 提供一个方法来获取容量，而不是直接暴露_capacity
    def get_capacity(self):
        return self._capacity

# 使用示例
# storage = Storage(5)
# storage.add_item("item1")
# print(storage.items)  # 可以直接访问公开的items属性
# print(storage.get_capacity())  # 通过方法访问受保护的_capacity属性
# print(storage._capacity)
# # print(storage._capacity)  # 虽然可以访问，但按照约定，不应该这样做
# yiled_stement ::= yiled_stement
