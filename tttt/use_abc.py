import abc

class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def greet(self):
        pass

class B(A):
    def greet(self):
        pass

class C(A):
    pass

if __name__ == "__main__":
    b = B()  # 正常实例化
    c = C()  # 解释器抛错
    # TypeError: Can't instantiate abstract class C with abstract methods greet
