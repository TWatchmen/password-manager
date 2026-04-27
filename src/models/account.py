from dataclasses import dataclass
from typing import Optional


@dataclass
class Account:
    id: Optional[int]
    plattform: str
    username: str
    email: str
    password: str
    notes: str = ""

    @staticmethod
    def from_db_row(row):
        return Account(
            id=row[0],
            plattform=row[1],
            username=row[2],
            email=row[3],
            password=row[4],
            notes=row[5],
        )