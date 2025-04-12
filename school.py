from typing import List

class Principal:
    """Represents a school principal."""

    def __init__(self, name: str):
        self.name = name

    def get_info(self) -> str:
        return f"Principal: {self.name}"


class SchoolBase:
    """Base class for schools containing shared logic for GPA calculations."""

    def __init__(self, name: str, grades: List[float], principal: Principal):
        self.name = name
        self.grades = grades
        self.principal = principal

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

    @staticmethod
    def calculate_gpa(average: float) -> float:
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        else:
            return 1.0

    def display_report(self) -> None:
        avg = self.average_grade()
        gpa = self.calculate_gpa(avg)
        print(f"{self.name} - {self.principal.get_info()} - Avg: {avg:.2f}, GPA: {gpa}")


class CIIT(SchoolBase):
    pass


class UP(SchoolBase):
    pass
