<a id="class-0x00---solution"></a>
## Класс 0x00: решение

1. Напишите простой класс с двумя атрибутами и двумя методами. Один атрибут должен иметь значение по умолчанию.

```python
from typing import Optional
""" Student Module

    """


class Student:
    def __init__(self, name: str, department: Optional[str] = None) -> None:
        """ Instance Initialization function

        Args:
            name (str): Name of student
            department (Optional[str], optional): Department. Defaults to None.
        """
        self.name = name
        self.department = department

    def getdetails(self) -> str:
        """ Gets the students details

        Returns:
            str: A formatted string
        """
        return f"Name is {self.name}, I'm in department {self.department}"

    def change_department(self, new_deparment: str) -> None:
        """Changes the department of the student object

        Args:
            new_deparment (str): Assigns the new department value to dept attr
        """
        self.department = new_deparment

# student1 instantiation
student1 = Student("Ayobami", "Statistics")

print(student1.getdetails())

# Calling the change_department function to change the department of student
student1.change_department("CS")

print(student1.department)
```

Вывод:

```
Name is Ayobami, I'm in department Statistics
CS
```
