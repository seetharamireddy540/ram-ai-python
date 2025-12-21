
student = {
    "name": "Ram",
    "age": 30,
    "grade": "A",
    "is_enrolled": True,
    "subjects": ["Math", "Science", "English"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "year": 2023
}

print(student["name"])
print(student.keys())

student.update({"year": 2024, "place": "Test"})
print(student["year"])
print(student["place"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
