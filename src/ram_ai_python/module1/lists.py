
from dataclasses import dataclass
from dataclasses import replace
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Dict, Any, Union, Optional


class Address(BaseModel):
    street: str
    city: str | None = None
    email: EmailStr = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")  # Email format validation
    state: str
    zip_code: str = Field(..., pattern=r"^\d{5}$")  # US zip code format
    model_config = ConfigDict(
        extra="forbid",
    )

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    gender: str


person = Person("John", 30, "male")
print(person.name)
update_person = replace(person, name="Ram")
print(update_person.name)
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        print("I love bananas!")

repeated = "ha" * 3
print(repeated)
results = 10 + 5
results = 10 - 5
results = 10 * 5
results = 10 / 5  # Division always returns a float
results = 10 // 5  # Floor deivision discards the fractional part
results = 10 % 3  # The % operator returns the remainder of the division
results = 10 ** 2  # 10 raised to the power of 2
results = 10 ** 3  # 10 raised to the power of 3
print(results)
results = 10 + 5 * 2
print(results)

if __name__ == "__main__":
    print("Hello World")

