
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        introduce = f'Name: {self.fullname}. Age: {str(self.age)}. Married: {self.is_married}.'
        return introduce


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def g_p_a(self):
        gpa = sum(self.marks.values()) / len(self.marks)
        return round(gpa, 1)


class Teacher(Person):
    base_salary = 20000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    # def finally_salary(self):
    #     if self.experience > 3:
    #         salary = self.base_salary + (self.base_salary * 0.05) * (self.experience - 3)
    #     else:
    #         salary = self.base_salary
    #     return f'Salary: {int(salary)} som.'
    def finally_salary(self):
        x = self.experience - 3
        if self.experience > 3:
            salary = self.base_salary * (1.05 ** x)
        else:
            salary = self.base_salary
        return f'Salary: {int(salary)} som.'


man = Person('Albert Einstein', 57, False)
print(man.introduce_myself())

math_teacher = Teacher('Mark Muller', 33, 'True', 8)
print(math_teacher.introduce_myself(),
      f'Experience: {math_teacher.experience} years.',
      math_teacher.finally_salary()
      )


def create_students(student_1, student_2, student_3):
    student_1 = Student(student_1, 20, False, {'Math': 4.7, 'Physics': 4.2,
                                               'Biology': 4.0, 'Chemistry': 4.1})
    student_2 = Student(student_2, 22, True, {'Math': 3.3, 'Physics': 4.0,
                                              'Biology': 3.8, 'Chemistry': 4.8})
    student_3 = Student(student_3, 19, False, {'Math': 4.1, 'Physics': 3.9,
                                               'Biology': 3.2, 'Chemistry': 3.5})
    student_list = [student_1, student_2, student_3]
    return student_list


students = create_students('Ralf', 'Kevin', 'Molly')

for student in students:
    print(student.introduce_myself(), f'GPA: {student.g_p_a()}')
