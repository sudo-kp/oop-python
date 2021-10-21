import operator
from numpy import mean


class Student:
    def __init__(self, name, surname, grades, rb_number):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError('Wrong name or surname.')
        if not isinstance(grades, dict):
            raise TypeError("Wrong grades format.")
        if not all(isinstance(marks, int) for marks in grades.values()):
            raise TypeError('Wrong type of marks.')
        if not all(isinstance(subjects, str) for subjects in grades.keys()):
            raise TypeError('Wrong type of subject name.')
        if not isinstance(rb_number, (str, int)):
            raise TypeError('Wrong record book number.')
        self.name = name
        self.surname = surname
        self.grades = grades
        self.rb_number = rb_number

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.surname == other.surname
        raise NotImplementedError("Can only compare objects of 'Student'.")

    def __hash__(self):
        return hash((self.name, self.surname))

    def __str__(self):
        return f'{self.name} {self.surname}'

    def average_score(self):
        return mean(list(self.grades.values()))


class Group:
    def __init__(self, students):
        if not isinstance(students, list):
            raise TypeError('Wrong type of students.')
        if not all(isinstance(student, Student)for student in students):
            raise TypeError('Wrong type of student.')
        if len(students) > 20:
            raise ValueError('Error: more than 20 students in the group.')
        if len(students) != len(set(students)):
            raise ValueError('Error: students with same name.')
        self.students = students

    def top5(self):
        topfive = sorted(self.students, key=operator.methodcaller('average_score'), reverse=True)
        return topfive[0:5]


try:
    grad = {'math': 12, 'eng': 10, 'bio': 11}
    grad2 = {'math': 6, 'eng': 7, 'bio': 8}
    grad3 = {'math': 13, 'eng': 14, 'bio': 15}
    stud1 = Student('Vasya', 'Pupkin', grad2, '1')
    stud2 = Student('Petya', 'Cheburekov', grad, '2')
    stud3 = Student('Vasya', 'Nepupkin', grad, '3')
    stud4 = Student('Yan', 'Go', grad2, '4')
    stud5 = Student('Maria', 'Petrenko', grad, '5')
    stud6 = Student('Anna', 'Honcharenko', grad3, '6')
    students = [stud1, stud2, stud3, stud4, stud5, stud6]
    group = Group(students)
    print(*group.top5())
except TypeError as message:
    print(message)
except ValueError as message:
    print(message)
except NotImplementedError as message:
    print(message)
except:
    print('error')



