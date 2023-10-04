from classa import ClassA
from classb import ClassB
import importlib


class NodeAB:
    instance = None
    implementation = None
    module_name = None
    module = None
    implementation_class = None

    def __init__(self, implementation: str = "ClassA", **kwargs):
        self.implementation = implementation
        self.module_name = f"{implementation.lower()}"
        try:
            self.module = importlib.import_module(self.module_name)
        except ModuleNotFoundError:
            raise ValueError(f"Invalid implementation: {implementation}")
        self.implementation_class = getattr(self.module,
                                            f"{self.implementation}")
        self.instance = self.implementation_class(**kwargs)
        # self = self.instance

    # def __post_init__(self):
    #     # self.__class__.__name__ = self.implementation
    #     # self.__class__ = type(self.instance)
    #     # return self.instance
    #     super().__init__()
    #     # return self

    # def __repr__(self) -> str:
    #     return self.instance.__repr__()

    def __getattr__(self, name):
        # delegate attribute access to the implementation instance
        return getattr(self.instance, name)

    def start(self):
        return self.instance

    @classmethod
    def __class__(self) -> type:
        # FIXME this is not working
        # delegate type() to the implementation instance
        return self.instance.__class__

    @classmethod
    def __instancecheck__(self, instance) -> bool:
        # check if the instance is an instance of the implementation class
        # FIXME this is not working
        return isinstance(instance, self.instance.__class__)


# DYANMIC
# create a NodeAB instance with ClassA implementation
node_a = NodeAB(implementation="ClassA", info="hello", alpha=1.0)
node_a = node_a.start()
# print(type(a))
print(node_a)
# print(type(node_a.instance))  # prints "ClassA"
print(node_a.__class__)
print(type(node_a))  # prints "ClassA"
print(isinstance(node_a, (ClassA)))
print(node_a.info)  # prints "hello"
print(node_a.alpha)  # prints "1.0"
print(node_a.add(2.0))  # prints "3.0"
# print(dir(node_a))

# create a NodeAB instance with ClassB implementation
node_b = NodeAB(implementation="ClassB", info="world", beta=2)
node_b = node_b.start()
print(node_b)
# print(type(node_b.instance))  # prints "ClassB"
print(node_b.__class__)
print(type(node_b))  # prints "ClassB"
print(isinstance(node_b, (ClassB)))
print(node_b.info)  # prints "world"
print(node_b.beta)  # prints "2"
print(node_b.add(3))  # prints "5"
