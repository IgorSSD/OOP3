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
 
    def rate_lecture(self, lecturer, course, grade):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        avg_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
 
    def __lt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self < avg_grade_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
 
    def __str__(self):
        avg_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
 
    def __lt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self < avg_grade_other


class Reviewer(Mentor):
    def grade_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nУ лекторов:"
 
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_lecturer = Lecturer('Some', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.grade_lecture(cool_lecturer, 'Python', 9)
cool_reviewer.grade_lecture(cool_lecturer, 'Python', 8)
cool_reviewer.grade_lecture(cool_lecturer, 'Python', 10)
 
print(cool_lecturer)
print(best_student)
print(cool_reviewer)


another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached += ['Python']
cool_lecturer.grade_lecture(best_student, 'Python', 10)
another_lecturer.grade_lecture(best_student, 'Python', 9)

print(cool_lecturer < another_lecturer) 


another_student = Student('Another', 'Student', 'your_gender')
another_student.courses_in_progress += ['Python']
best_student.rate_lecture(cool_lecturer, 'Python', 9)
another_student.rate_lecture(cool_lecturer, 'Python', 10)

print(best_student < another_student)  
