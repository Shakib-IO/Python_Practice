# https://youtu.be/yatgY4NpZXE?list=LL
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
@dataclass
class Customer:
    name: str
    phone: str

@dataclass
class CustomerCard(Customer):
    cc_number: str
    cc_exp_month: str
    cc_exp_year: str
    cc_valid: bool = False

class CardInfo(Protocol):
    @property
    def number(self) -> str:
        ...
    @property
    def exp_month(self) -> int:
        ...
    @property
    def exp_year(self) -> int:
        ...

def luhn_checksum(card_number: str) -> bool:
    def digits_of(number:str) -> list[int]:
        return [int(d) for d in number]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0 

def validate_card(*, number:str, exp_month:int, exp_year:int) -> bool:
    return (
        luhn_checksum(number)
        and datetime(exp_year, exp_month, 1) > datetime.now()
    )

def main() -> None:
    alice = CustomerCard(
        name="Alice",
        phone="2341",
        cc_number="1249190007575069",
        cc_exp_month=1,
        cc_exp_year=2024,
    )
    alice.cc_valid = validate_card(number = alice.cc_number, exp_month = alice.cc_exp_month, exp_year=alice.cc_exp_year)
    print(f"Is Alice's card valid? { alice.cc_valid}")
    print(alice)


if __name__ == "__main__":
    main()
