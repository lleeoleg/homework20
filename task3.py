"""
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год 
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода 
данных, реализуйте доступ к отдельным полям через методы класса.
"""
class Stadium:
    """_summary_
    """
    def __init__(self, name, year, country, city, capacity):
        """_summary_

        Args:
            name (_type_): _description_
            year (_type_): _description_
            country (_type_): _description_
            city (_type_): _description_
            capacity (_type_): _description_
        """
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity
    def output_data(self):
        """_summary_
        """
        print(f"Название стадиона: {self.name}")
        print(f"Год постройки: {self.year}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")
    def set_name(self, new_name):
        """_summary_

        Args:
            new_name (_type_): _description_
        """
        self.name = new_name
    def get_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name
    def set_year(self, new_year):
        """_summary_

        Args:
            new_year (_type_): _description_
        """
        self.year = new_year
    def get_year(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.year
    def set_country(self, new_country):
        """_summary_

        Args:
            new_country (_type_): _description_
        """
        self.country = new_country
    def get_country(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.country
    def set_city(self, new_city):
        """_summary_

        Args:
            new_city (_type_): _description_
        """
        self.city = new_city
    def get_city(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.city
    def set_capacity(self, new_capacity):
        """_summary_

        Args:
            new_capacity (_type_): _description_
        """
        self.capacity = new_capacity
    def get_capacity(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.capacity
    def new_output_data(self):
        """_summary_
        """
        print(f"Название стадиона: {self.name}")
        print(f"Год постройки: {self.year}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")
if __name__ == "__main__":
    stadium1 = Stadium("Национальный стадион Уэмбли", "1923", "Великобритания",
                "Лондон", "около 90 000 зрителей")
    print("Данные первого стадиона:")
    stadium1.output_data()
    stadium1.set_name("TКамп Ноу (Camp Nou)")
    stadium1.set_year("1957")
    stadium1.set_country("Испания")
    stadium1.set_city("Барселона")
    stadium1.set_capacity("около 99 000 зрителей")
    print("\nИзмененный стадион:")
    stadium1.new_output_data()
