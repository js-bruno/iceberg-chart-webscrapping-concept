from dataclasses import dataclass, asdict


@dataclass
class Iceberg:
    name: str
    url: str

    dict = asdict


@dataclass
class CategoryEntryDTO:
    name: str
    icebergs: list[Iceberg]

    dict = asdict
