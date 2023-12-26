import dataclasses


def slot_dataclass(cls):
    cls.__slots__ = [f.name for f in dataclasses.fields(cls)]
    return dataclasses.dataclass(cls)
