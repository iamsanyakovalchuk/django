class SanyaKovalchuk:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name if first_name is not None else 'Саня'
        self.last_name = last_name if last_name is not None else 'Ковальчук'
        self.birth_year = birth_year if birth_year is not None else 2008

    def calculate_course(self):
        current_year = 2025
        course = current_year - self.birth_year
        return f"Курс відповідно до року народження: {course} років"

    def create_name_list(self):
        name_list = [self.first_name, self.last_name]
        return name_list

# Створюємо екземпляр класу і перевіряємо методи
SanyaKovalchuk = SanyaKovalchuk()
print(SanyaKovalchuk.calculate_course())  # Виведе "Курс відповідно до року народження: 17 років"
print(SanyaKovalchuk.create_name_list())  # Виведе ["Саня", "Ковальчук"]
