from dataclasses import dataclass, asdict
from pprint import pprint
@dataclass
class Investor:
    name: str
    age: int
    cash: float


S1 = Investor("Islem", 23, 10000)
S2 = Investor("Islem", 23, 10000)
print(S1)
print(S1 == S2)
Dict = asdict(S1)
pprint(Dict)
