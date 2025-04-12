from vehicle import Bus, Vehicle
from employee import Employee
from school import CIIT, UP, Principal
from vector import Vector
from book import Author, Book


def run_vehicle_test() -> None:
    print("===== Vehicle Test =====")
    school_bus = Bus("Toyota Bluebird", 30)
    school_bus.start_engine()
    print("Is school_bus an instance of Vehicle?", isinstance(school_bus, Vehicle))


def run_employee_test() -> None:
    print("\n===== Employee Test =====")
    emp1 = Employee("Maria", 1001)
    emp2 = Employee.from_string("Joseph-1002")
    emp3 = Employee.default_employee()
    emp1.display()
    emp2.display()
    emp3.display()


def run_school_test() -> None:
    print("\n===== School GPA Test with Aggregation =====")
    p1 = Principal("Mrs. Ramos")
    p2 = Principal("Mr. Suarez")
    s1 = CIIT("CIIT", [89, 76, 92], p1)
    s2 = UP("UP", [65, 70, 60], p2)
    s1.display_report()
    s2.display_report()


def run_vector_test() -> None:
    print("\n===== Vector Addition Test =====")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print("v1 + v2 =", v3)


def run_book_test() -> None:
    print("\n===== Book Composition with Nested Class =====")
    author = Author("George Perez")
    book = Book("1984", author)
    book.display()
    chapter = Book.Chapter("War is Peace", 1)
    chapter.display_chapter()


if __name__ == "__main__":
    run_vehicle_test()
    run_employee_test()
    run_school_test()
    run_vector_test()
    run_book_test()
