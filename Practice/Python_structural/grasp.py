# https://youtu.be/fGNF6wuD-fg
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ProductDescription:
    price: int
    description: str

@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int

@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory = list)
    time: datetime = field(default_factory = datetime.now)


def main() -> None:
    headset = ProductDescription(price = 500, description = "Nice earplug")
    keyboard = ProductDescription(price = 100, description = "Mechanincal Keyboard")
    
    row1 = SaleLineItem(product=headset, quantity=2)
    row2 = SaleLineItem(product=keyboard, quantity=3)

    sale = Sale([row1, row2])
    print(sold)

if __name__ == "__main__":
    main()


############################ Creator ############################
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ProductDescription:
    price: int
    description: str

@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int

@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory = list)
    time: datetime = field(default_factory = datetime.now)

    def add_line_item(self, product: ProductDescription, quantity:int):
        self.items.append([product, quantity])


def main() -> None:
    headset = ProductDescription(price = 500, description = "Nice earplug")
    keyboard = ProductDescription(price = 100, description = "Mechanincal Keyboard")

    sold = Sale()
    sold.add_line_item(headset, 3)
    sold.add_line_item(keyboard,4)
    print(sold)

if __name__ == "__main__":
    main()
