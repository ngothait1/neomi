from project_person_cls import Person
from project_valid_cls import Validator


class Student(Person):
    def __init__(self, ID: str, name: str, age: str):
        super().__init__(ID, name, age)

        grades_str = Validator.input_until_valid(
            "Enter grades separated by commas: ", Validator.is_valid_grades, "grades"
        )
        self.grades = Validator.parse_grades(grades_str)

        self.field_of_study = input("Enter field of study: ").strip()

        self.year_of_study = Validator.input_until_valid(
            "Enter year of study: ", Validator.is_valid_year_of_study, "year"
        )

        self.average_score = self.get_average_score()

    def add_grades(self, new_grades) -> None:
        self.grades.extend(new_grades)

    def get_average_score(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, Type=Student, "
            f"Field={self.field_of_study}, Year={self.year_of_study}, "
            f"Grades={self.grades}, Average Score={self.get_average_score():.2f}"
        )

    def to_dict(self):
        base = super().to_dict()
        base.update(
            {
                "Field": self.field_of_study,
                "Year": self.year_of_study,
                "Grades": ", ".join(map(str, self.grades)),
                "Average": self.get_average_score(),
            }
        )
        return base

    def my_func(self):
        print(f"I'm a student and my name is {self.name}.")
