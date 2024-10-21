from typing import Iterable


class Columns:
    def __init__(self, columns: Iterable[str], round_until: int = 1):
        self.columns = columns
        self.round_until = round_until