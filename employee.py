class Employee:
    """Class representing an employee with support for multiple constructors."""

    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.id = emp_id

    @classmethod
    def from_string(cls, emp_str: str) -> 'Employee':
        """Creates an Employee object from a dash-separated string."""
        name, id_str = emp_str.split("-")
        return cls(name, int(id_str))

    @classmethod
    def default_employee(cls) -> 'Employee':
        """Returns a default employee object."""
        return cls("Juan Sulit", 0)

    def display(self) -> None:
        print(f"Employee: {self.name}, ID: {self.id}")
