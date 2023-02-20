from dataclasses import dataclass
from typing import Optional

@dataclass
class Transaction:
    description: str
    price_kzt: int
    quantity: int
    amount: int
    price_usd: int
    date: str
    id: Optional[int] = None
