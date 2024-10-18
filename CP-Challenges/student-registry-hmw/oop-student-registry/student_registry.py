class Student:
    def __init__(self,name: str, age: int = 13, grade: str = "12th") -> None:
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, updated_name: str):
        if isinstance(updated_name,str) and len(updated_name) >= 3:
            self._name = updated_name

    @property
    def age(self: int):
        return self._age
    
    @age.setter
    def age(self, updated_age: int):
        if isinstance(updated_age, int) and updated_age > 11 and updated_age < 18:
            self._age = updated_age

    @property
    def grade(self: str):
        return self._grade
    
    @grade.setter
    def grade(self, updated_grade: str):
        if isinstance(updated_grade, str) and updated_grade[-2:] == "th":
            value = updated_grade[:-2]
            match value:
                case "9":
                    self._grade = updated_grade
                case "10":
                    self._grade = updated_grade
                case "11":
                    self._grade = updated_grade
                case "12":
                    self._grade = updated_grade
                # case _:
                #     raise ValueError("Invalid grade. Must be 9th, 10th, 11th, or 12th.")
    
# zeus = Student("jesus", 36, "11th")
# print(zeus.name)
# print(zeus.age)
# print(zeus.grade)
# print(zeus.name.upper())

    