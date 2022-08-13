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
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.coursed_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка выставления оценки')
            return

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
              f'Курсы в процессе изучения: {(", ".join(self.courses_in_progress))}\n' \
              f'Завершённые курсы: {(", ".join(self.finished_courses))}'
        return res

    def average_grade(self):
        self.grades_list = [grade for grades in self.grades.values() for grade in grades]
        if self.grades_list:
            return round(sum(self.grades_list) / len(self.grades_list), 1)
        else:
            return 'Нет оценок'

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Второй не студент, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Второй не студент, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Второй не студент, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursed_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

    def average_grade(self):
        self.grades_list = [grade for grades in self.grades.values() for grade in grades]
        if self.grades_list:
            return round(sum(self.grades_list) / len(self.grades_list), 1)
        else:
            return 'Нет оценок'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Второй не лектор, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Второй не лектор, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Второй не лектор, сравнение невозможно')
            return 'Ошибка'
        else:
            return self.average_grade() < other.average_grade()


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

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_course_grade_student(students, course):
    if all([isinstance(item, Student) for item in students]):
        average_course_grade = []
        for student in students:
            if course in student.grades:
                average_course_grade += student.grades[course]
            if average_course_grade:
                return sum(average_course_grade) / len(average_course_grade)
    else:
        return 'В списке должны быть только студенты'


def average_course_grade_lecturer(lecturers, course):
    if all([isinstance(item, Lecturer) for item in lecturers]):
        average_course_grade = []
        for lecturer in lecturers:
            if course in lecturer.grades:
                average_course_grade += lecturer.grades[course]
            if average_course_grade:
                return sum(average_course_grade) / len(average_course_grade)
    else:
        return 'В списке должны быть только лекторы'


# Инициируем студентов, лекторов и проверяторов
student1 = Student('Pupkin', 'Vasiliy', 'Male')
student1.finished_courses += ['Git', 'C++']
student1.courses_in_progress += ['Python', 'Pascal']
student1.grades['Git'] = [10, 7, 9, 10, 7]
student1.grades['Python'] = [10, 9]

student2 = Student('Gadia', 'Petrovich', 'Female')
student2.finished_courses += ['C++', 'Pascal']
student2.courses_in_progress += ['Git', 'Python']
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

# Проверяем вывод действующих лиц
# print(student1)
# print(student2)
# print(lecturer1)
# print(lecturer2)
# print(reviewer1)
# print(reviewer2)

# Проверяем выставление оценок
# print(student2.grades)
# reviewer1.rate_students(student2, 'Git', 8)
# print(student2.grades)

# print(lecturer1.grades)
# student1.rate_lecturer(lecturer1, 'Python', 6)
# print(lecturer1.grades)

# Проверяем вывод средних оценок за курс
# print(average_course_grade_student([student1, student2], 'Git'))
# print(average_course_grade_lecturer([lecturer1, lecturer2], 'Python'))