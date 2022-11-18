
class Student:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {round(self.average_rating,2)}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):

        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за лекции: {round(self.average_rating,2)}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\n \
        Фамилия: {self.surname}'
        return res

#Лекторы

lecturer_1 = Lecturer('Oleg', 'Kemerov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Maxim', 'Lavrov')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Anton', 'Pavlov')
lecturer_3.courses_attached += ['Python']

#Проверяющие

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Sergey', 'Valhamov')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

#Студенты

student_1 = Student('Anna', 'Rogacheva')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Kirill', 'Semanov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Garik', 'Harlamov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

#Оценки за лекции:

#Первого студента

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 9)

student_1.rate_hw(lecturer_2, 'Java', 8)

student_1.rate_hw(lecturer_3, 'Python', 7)
student_1.rate_hw(lecturer_3, 'Python', 10)

#Второго студена

student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Java', 9)

student_2.rate_hw(lecturer_3, 'Python', 10)

#Третьего студента

student_3.rate_hw(lecturer_1, 'Python', 10)

student_3.rate_hw(lecturer_2, 'Java', 8)
student_3.rate_hw(lecturer_2, 'Java', 7)
student_3.rate_hw(lecturer_2, 'Java', 10)

student_3.rate_hw(lecturer_3, 'Python', 9)

#Оценки за ДЗ

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 10)

reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 10)


lecturer_list = [lecturer_1, lecturer_2, lecturer_3]
student_list = [student_1, student_2, student_3]

def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return round(average_for_all, 2)



def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return round(average_for_all, 2)


print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()

print(f'Результат сравнения студентов по средним оценкам за ДЗ: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

print(f'Результат сравнения лекторов по средним оценкам за лекции: '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()