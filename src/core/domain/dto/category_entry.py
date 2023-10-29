from dataclasses import dataclass


@dataclass
class Iceberg:
    name: str
    url: str


@dataclass
class CategoryEntryDTO:
    name: str
    icebergs: list[Iceberg]
