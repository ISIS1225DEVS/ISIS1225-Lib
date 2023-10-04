import importlib


class DynamicImporter(object):
    package: str = ""
    implementation: str = ""
    _module = None
    _class = None
    _instance = None

    def __init__(self, implementation: str, package: str, **kwargs):
        try:
            self.package = package   # __import__(package)
            self.implementation = implementation
            self._module = importlib.import_module(self.package)
            self._class = None
            self._instance = None
        except ModuleNotFoundError:
            err_msg = f"Invalid implementation: {self.implementation}"
            raise ValueError(err_msg)
        self._class = getattr(self._module,
                              self.implementation)
        self._instance = self._class(**kwargs)

    def __post_init__(self):
        self.__class__.__name__ = self.implementation

    def __repr__(self) -> str:
        return self._instance.__repr__()

    def __getattr__(self, name):
        # delegate attribute access to the implementation instance
        return getattr(self._instance, name)

    def start(self):
        # FIXME this is a hack!!!
        return self._instance

    @classmethod
    def __class__(self) -> type:
        # FIXME this is not working
        # delegate type() to the implementation instance
        return self._instance.__class__

    @classmethod
    def __instancecheck__(self, instance) -> bool:
        # check if the instance is an instance of the implementation class
        # FIXME this is not working
        return isinstance(instance, self._instance.__class__)
