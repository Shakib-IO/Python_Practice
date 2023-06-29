# https://docs.pydantic.dev/latest/
# https://youtu.be/Vj-iU-8_xLs
import json
import pydantic
from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional, Callable

class ISBN10FormatError(Exception):
    # A error will ocurred if the isbn is not valid
    def __init__(self, value, message:str) -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)

class PriceError(Exception):
    # A error will occured if any book price is negative
    def __int__(self, check_book_price, message:str) -> None:
        self.check_book_price = check_book_price
        self.message = message
        super().__init__(self.message)

class ISBN10ORISBN13Error(Exception):
    def __init__(self, title, message:str) -> None:
        self.title = title
        self.message = message
        super().__init__(self.message)

class AuthorError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        super().__init__(self.message)

class Book(BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def isbn10_or_isbn12(cls, values) -> None:
        # Make sure that there is at least one ISBN number
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBN10ORISBN13Error(title=values["title"], message = "This book '{}' doesn't have any ISBN number.".format(values["title"]))
        return values

    @validator('isbn_10')
    @classmethod
    def isbn_10_valid(cls, val) -> None:
        chars = [c for c in val if c.isdigit()]
        if len(chars) != 10:
            raise ISBN10FormatError(value = val, message = "This {} ISBN number must be 10 digits".format(val))

        def char_to_int(char:str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        weighted_sum = sum((10 - i) * char_to_int(c) for i, c in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(value = val, message = "This {} ISBN number is not valid".format(val))
        return val
    
    @validator('price')
    @classmethod
    def check_price(cls, book_price) -> None:
        if book_price < 0:
            raise PriceError(book_price,  "The price {} of the book can't be negative".format(book_price))
        return book_price

    @validator('author')
    @classmethod
    def check_author(cls, author) -> None:
        if author == "":
            raise AuthorError("The author of this book '{}' can't be empty")
        return author

def read_from_file(path: str) -> None:
    with open(path, 'r') as f:
        data = json.load(f)
    books: List[Book] = [Book(**item) for item in data]
    print("Data Loaded Successfully")

if __name__ == '__main__':
    read_from_file('data.json')
