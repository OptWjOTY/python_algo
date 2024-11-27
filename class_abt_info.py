## 关于类：用于创建对象的模板或蓝图。类定义了对象的属性和方法(函数)。通过类，可以创建具有相同属性和方法的多个对象(实例)；
## 类的其他特性
## 类属性：类属性是属于类本身的属性，而不是某个特定的实例。可以通过类名来访问类属性，也可以通过实例来访问。
## 继承：继承是面向对象编程的一个重要特性，允许你创建一个新的类(子类),这个类继承了一个或多个已存在的类(父类)的属性和方法。
## 多态：多态允许你将子类对象视为父类对象来使用，意味着可以使用父类类型的引用来调用子类中重写的方法
## 封装：封装是将数据(属性),和操作数据的方法(函数),结合在一个单独的单元中(类),并尽可能隐藏对象的内部细节。
class student:
    # 每个方法第一个参数就是self，位于所有形参前面。调用init方法时，会自动传入self参数，self实参是一个指向实例本身的引用，让实例能够访问实例中的属性和方法

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def student_info(self) -> str:
        return f"该学生姓名是：{self.name},年纪是：{self.age}"


class cls1(student):
    def __init__(self, name, age, major: str, graduation_year: int):
        """初始化父类属性、继承"""
        super().__init__(name, age)
        self.major = major
        self.graduation_year = graduation_year
    def graInfo(self)->str:
        return f"该学生姓名是：{self.name},今年{self.age}岁,学习专业是{self.major},毕业时间是：{self.graduation_year}"


student_return = cls1(name="张三", age=20,major="电子信息工程",graduation_year=2021)
print(student_return.graInfo())
