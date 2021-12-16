import json
import os.path
import re
from abc import ABC, abstractmethod


teachers = {}
id_teacher = 0


class ICourse(ABC):
    """Interface for class Course"""
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, program):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Course(ICourse):
    """Class fpr realization of courses in software academy"""
    def __str__(self):
        return f'{self.name} by {self.teacher}'

    def __init__(self, name, teacher, program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong name of the course.")
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Wrong teacher.")
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not all(isinstance(topic, str) for topic in program):
            raise TypeError("Wrong program.")
        self.__program = program


class ITeacher(ABC):
    """Interface for class Teacher"""
    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @courses.setter
    @abstractmethod
    def courses(self, courses):
        pass

    @abstractmethod
    def add_course(self, course):
        pass


class Teacher(ITeacher):
    """Class which is representation of Teacher in software academy, contains name and courses."""
    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Wrong course to add")
        self.courses.append(course)

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
        teachers[id_teacher+1] = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong name type")
        if not re.compile('[a-zA-Z ]+').match(name):
            raise ValueError("Wrong name")
        self.__name = name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        if not all(isinstance(course, Course) for course in courses):
            raise TypeError("Wrong courses")
        self.__courses = courses

    def __str__(self):
        return f"{self.name}" + '\n'.join(map(str, self.courses))


class ILocalCourse(ABC):
    """Interface for class LocalCourse"""
    @abstractmethod
    def __str__(self):
        pass
    
    @property
    @abstractmethod
    def lab(self):
        pass
    
    @lab.setter
    @abstractmethod
    def lab(self, lab):
        pass
    
    
class LocalCourse(Course, ILocalCourse):
    """Class for realization of Local courses in academy, inherits Courses. """
    def __str__(self):
        return Course.__str__(self) + f' in {self.lab} lab'
    
    @property
    def lab(self):
        return self.__lab
    
    @lab.setter
    def lab(self, lab):
        if not isinstance(lab, str):
            raise TypeError("Wrong lab type")
        self.__lab = lab
        
    def __init__(self, name, teacher, program, lab):
        super().__init__(name, teacher, program)
        self.lab = lab


class IOffsiteCourse(ABC):
    """Interface for OffsiteCourse class"""
    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def town(self):
        pass

    @town.setter
    @abstractmethod
    def town(self, town):
        pass


class OffsiteCourse(IOffsiteCourse, Course):
    """Class for realization of Offsite courses in academy, inherits Courses. """
    def __init__(self, name, teacher, program, town):
        super().__init__(name, teacher, program)
        self.town = town

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, town):
        if not isinstance(town, str):
            raise TypeError("Wrong town")
        self.__town = town

    def __str__(self):
        return Course.__str__(self) + f' in {self.town}'


class ICourseFactory(ABC):
    """Interface for factory class of courses."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def course_factory(self, is_local):
        pass

    @property
    @abstractmethod
    def data(self):
        pass

    @data.setter
    @abstractmethod
    def data(self, data):
        pass


class CourseFactory(ICourseFactory):
    """Factory class to create instances of different courses"""
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError("No such file")
        with open(path, 'r') as file:
            self.data = json.load(file)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, dict):
            raise TypeError("Wrong json data")
        data["teacher"] = teachers[data["teacher"]]
        self.__data = data

    def course_factory(self, is_local):
        if is_local:
            return LocalCourse(*self.data.values())
        return OffsiteCourse(*self.data.values())


def main():
    id1 = Teacher("teacher name", [])
    print(id1)
    obj = CourseFactory("date.json")
    oc = obj.course_factory(False)
    print(oc)
    obj2 = CourseFactory("date2.json")
    lc = obj2.course_factory(True)
    print(lc)


if __name__ == '__main__':
    main()
