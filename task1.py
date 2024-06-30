"""
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, 
год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса 
для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
"""
class Car:
    """_summary_
    """
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = 
        self.color = color
        self.price = price
    def output_data(self):
        """_summary_
        """
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
    def set_model(self, new_model):
        """_summary_

        Args:
            new_model (_type_): _description_
        """
        self.model = new_model
    def get_model(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.model
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
    def set_manufacturer(self, new_manufacturer):
        """_summary_

        Args:
            new_manufacturer (_type_): _description_
        """
        self.manufacturer = new_manufacturer
    def get_manufacturer(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.manufacturer
    def set_engine_volume(self, new_engine_volume):
        """_summary_

        Args:
            new_engine_volume (_type_): _description_
        """
        self.engine_volume = new_engine_volume
    def get_engine_volume(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.engine_volume
    def set_color(self, new_color):
        """_summary_

        Args:
            new_color (_type_): _description_
        """
        self.color = new_color
    def get_color(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.color
    def set_price(self, new_price):
        """_summary_

        Args:
            new_price (_type_): _description_
        """
        self.price = new_price
    def get_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price
    def new_output_data(self):
        """_summary_
        """
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
if __name__ == "__main__":
    car1 = Car("Toyota Camry", "2023", "Toyota", "2.5L", "черный", "$25,000")
    print("Данные первого автомобиля:")
    car1.output_data()
    car1.set_model("Toyota Corolla")
    car1.set_year("2022")
    car1.set_manufacturer("Toyota")
    car1.set_engine_volume("1.6L")
    car1.set_color("White")
    car1.set_price("$20,000")
    print("\nИзмененная модель:")
    car1.new_output_data()
