class SanyaKovalchuk:
    def init(self, name=None, surname=None, birth_year=None, course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.course = course

    def get_info(self):
        course_info = self.course if isinstance(self.course, int) and self.course < 5 else "Випускник або невідомо"
        return f"Ім'я: {self.name} {self.surname}, Рік народження: {self.birth_year}, Курс: {course_info}"

    def get_names_list(self, students):
        return [f"{student.name} {student.surname}" for student in students]


class Onl_Denis(Denis):
    def init(self, name=None, surname=None, birth_year=None, course=None, online_platform=None, in_ukraine=None, device_used=None):
        super().init(name, surname, birth_year, course)
        self.online_platform = online_platform
        self.in_ukraine = in_ukraine
        self.device_used = device_used

    def _get_platform_info(self):
        return f"Online platform: {self.online_platform}"

    def __device_info(self):
        return f"Device used: {self.device_used}"

    def get_info(self):
        basic_info = super().get_info()
        platform_info = f", Платформа: {self.online_platform}"
        location_info = f", За кордоном: {'Так' if not self.in_ukraine else 'Ні'}"
        return basic_info + platform_info + location_info

Student1 = Denis("Денис", "Швайковський", 2008)
Student2 = Denis("Данила", None, 2000)
Student3 = Denis("Віталік", "Спарта", 2007, 2)

Student4 = Onl_Denis("Давид", "Снейк", 2005, 3, "Zoom", False, "ПК")
Student5 = Onl_Denis("Джек", "Рипек", 2008, 3, "Google Meet", True, "Ноутбук")

Students = [Student1, Student2, Student3, Student4, Student5]
Names_list = Student1.get_names_list(Students)

print(Names_list)
print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())
print(Student4.get_info())
print(Student5.get_info())\
