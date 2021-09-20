# функции для 4 задачи - average_hw_scores, average_lecture_scores
# добавил несколько функций оценщикам - они могут завершать/открывать курсы (finish_course, reopen_course)
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {_average_dict_values(self.grades)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        return _average_dict_values(self.grades) < _average_dict_values(other.grades)

    def __gt__(self, other):
        return _average_dict_values(self.grades) > _average_dict_values(other.grades)

    def __le__(self, other):
        return _average_dict_values(self.grades) <= _average_dict_values(other.grades)

    def __ge__(self, other):
        return _average_dict_values(self.grades) >= _average_dict_values(other.grades)

    def __eq__(self, other):
        return _average_dict_values(self.grades) == _average_dict_values(other.grades)

    def __ne__(self, other):
        return _average_dict_values(self.grades) != _average_dict_values(other.grades)

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {_average_dict_values(self.grades)}\n'

    def __lt__(self, other):
        return _average_dict_values(self.grades) < _average_dict_values(other.grades)

    def __gt__(self, other):
        return _average_dict_values(self.grades) > _average_dict_values(other.grades)

    def __le__(self, other):
        return _average_dict_values(self.grades) <= _average_dict_values(other.grades)

    def __ge__(self, other):
        return _average_dict_values(self.grades) >= _average_dict_values(other.grades)

    def __eq__(self, other):
        return _average_dict_values(self.grades) == _average_dict_values(other.grades)

    def __ne__(self, other):
        return _average_dict_values(self.grades) != _average_dict_values(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def finish_course(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.courses_in_progress.remove(course)
            student.finished_courses.append(course)
        else:
            return 'Ошибка'

    def reopen_course(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            student.finished_courses.remove(course)
            student.courses_in_progress.append(course)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def _average_score_list(person_list, course):
    count_grades = 0
    all_grades = 0
    for person in person_list:
        if course in person.grades:
            for grade in person.grades[course]:
                all_grades += grade
                count_grades += 1
    if count_grades == 0:
        average_score = 0
    else:
        average_score = round(all_grades / count_grades, 1)
    return average_score


def _average_dict_values(dict_scores):
    count_grades = 0
    all_grades = 0
    for course in dict_scores:
        for score in dict_scores[course]:
            all_grades += score
            count_grades += 1
    if count_grades == 0:
        average_score = 0
    else:
        average_score = round(all_grades / count_grades, 1)
    return average_score


def average_hw_scores(students_list, course):
    for student in students_list:
        if not isinstance(student, Student):
            return 'Ошибка'
    return _average_score_list(students_list, course)


def average_lecture_scores(lecturers_list, course):
    for lecture in lecturers_list:
        if not isinstance(lecture, Lecturer):
            return 'Ошибка'
    return _average_score_list(lecturers_list, course)


# следующий далее код демонстрирует работу программы


student_1 = Student('Ivan', 'Ivanov', 'M')
student_2 = Student('Pavel', 'Pavlov', 'M')
student_3 = Student('Viktoria', 'Vikovich', 'F')
lecturer_1 = Lecturer('Oleg', 'Olegov')
lecturer_2 = Lecturer('Valentina', 'Valerievna')
reviewer_1 = Reviewer('Denis', 'Denisov')

lecturer_1.courses_attached = ['Python', 'C', 'Java', 'Random']
lecturer_2.courses_attached = ['Git', 'Github', 'Random']

reviewer_1.courses_attached = ['Python', 'C', 'Java', 'Git', 'Github', 'Random']


student_1.courses_in_progress = ['Python', 'Git', 'C', 'Random']
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 5)
reviewer_1.rate_hw(student_1, 'C', 9)
student_1.rate_lectures(lecturer_1, 'Python', 8)
student_1.rate_lectures(lecturer_2, 'Git', 5)
student_1.rate_lectures(lecturer_1, 'C', 7)
student_3.rate_lectures(lecturer_1, 'Random', 5)
reviewer_1.finish_course(student_1, 'C')

student_2.courses_in_progress = ['Python', 'Git', 'Github', 'Java', 'Random']
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Github', 8)
reviewer_1.rate_hw(student_2, 'Java', 4)
student_2.rate_lectures(lecturer_1, 'Python', 8)
student_2.rate_lectures(lecturer_2, 'Git', 5)
student_2.rate_lectures(lecturer_2, 'Github', 10)
student_2.rate_lectures(lecturer_1, 'Java', 5)
student_2.rate_lectures(lecturer_1, 'Random', 10)
reviewer_1.finish_course(student_2, 'Python')

student_3.courses_in_progress = ['Git', 'Github', 'Java', 'C', 'Random']
reviewer_1.rate_hw(student_3, 'C', 6)
reviewer_1.rate_hw(student_3, 'Git', 9)
reviewer_1.rate_hw(student_3, 'Github', 9)
reviewer_1.rate_hw(student_3, 'Java', 7)
student_3.rate_lectures(lecturer_1, 'C', 7)
student_3.rate_lectures(lecturer_2, 'Git', 10)
student_3.rate_lectures(lecturer_2, 'Github', 10)
student_3.rate_lectures(lecturer_1, 'Java', 9)
student_3.rate_lectures(lecturer_2, 'Random', 7)

print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 == student_2)
print(student_1 != student_2)

print(f'Средние оценки студентов за курс Git: {average_hw_scores([student_1, student_2, student_3], "Git")}')
print(f'Средние оценки лекторов за курс Random: {average_lecture_scores([lecturer_1, lecturer_2], "Random")}')

print('Студенты:')
print(student_1, student_2, student_3, sep='\n')
print()
print('Лекторы:')
print(lecturer_1, lecturer_2, sep='\n')
print()
print('Проверяющие:')
print(reviewer_1)
