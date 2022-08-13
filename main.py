class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.coursed_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка выставления оценки')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursed_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_students(self, student, course, grade):
        if isinstance(student, Student) and course in self.coursed_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка выставления оценки')
            return


student1 = Student('Pupkin', 'Vasiliy', 'Male')
student1.finished_courses += ['Git']
student1.courses_in_progress += ['Python']
student1.grades['Git'] = [10, 7, 9, 10, 7]
student1.grades['Python'] = [10, 9]

student2 = Student('Gadia', 'Petrovich', 'Female')
student2.finished_courses += ['Python']
student2.courses_in_progress += ['Git']
student2.grades['Python'] = [9, 4, 10, 5, 9]
student2.grades['Git'] = [6, 4]

lecturer1 = Lecturer('Rulon', 'Oboev')
lecturer1.coursed_attached += ['Python']
lecturer1.grades['Python'] = [10, 7, 4, 3]

lecturer2 = Lecturer('Nalog', 'Sdohodov')
lecturer2.coursed_attached += ['Git']
lecturer2.grades['Git'] = [3, 9, 10, 7, 6]

reviewer1 = Reviewer('Lux', 'Nebohodov')
reviewer1.coursed_attached += ['Git']

reviewer2 = Reviewer('Zapoi', 'Gusarov')
reviewer2.coursed_attached += ['Python']

# reviewer1.rate_students(student2, 'Git', 8)
# print(student1.finished_courses)
# print(student1.courses_in_progress)
# print(student1.grades)
# print(student2.finished_courses)
# print(student2.courses_in_progress)
# print(student2.grades)

# student1.rate_lecturer(lecturer1, 'Python', 9)
# print(lecturer1.coursed_attached)
# print(lecturer1.grades)
# print(lecturer2.coursed_attached)
# print(lecturer2.grades)
