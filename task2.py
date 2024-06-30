"""
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год 
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода 
данных, реализуйте доступ к отдельным полям через методы класса.
"""
class Book:
    """_summary_
    """
    def __init__(self, namebook, year, publisher, genre, author, price):
        """_summary_

        Args:
            namebook (_type_): _description_
            year (_type_): _description_
            publisher (_type_): _description_
            genre (_type_): _description_
            author (_type_): _description_
            price (_type_): _description_
        """
        self.namebook = namebook
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    def output_data(self):
        """_summary_
        """
        print(f"Название книги: {self.namebook}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")
    def set_namebook(self, new_namebook):
        """_summary_

        Args:
            new_namebook (_type_): _description_
        """
        self.namebook = new_namebook
    def get_namebook(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.namebook
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
    def set_publisher(self, new_publisher):
        """_summary_

        Args:
            new_publisher (_type_): _description_
        """
        self.publisher = new_publisher
    def get_publisher(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.publisher
    def set_genre(self, new_genre):
        """_summary_

        Args:
            new_genre (_type_): _description_
        """
        self.genre = new_genre
    def get_genre(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.genre
    def set_author(self, new_author):
        """_summary_

        Args:
            new_author (_type_): _description_
        """
        self.author = new_author
    def get_author(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.author
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
        print(f"Название книги: {self.namebook}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")
if __name__ == "__main__":
    book1 = Book("\"1984\"", "1949", "Secker & Warburg",
                "дистопия, научная фантастик", "Джордж Оруэлл", "$10-15")
    print("Данные первой книги:")
    book1.output_data()
    book1.set_namebook("To Kill a Mockingbird")
    book1.set_year("1960")
    book1.set_publisher("J.B. Lippincott & Co.")
    book1.set_genre("роман, классическая литература")
    book1.set_author("Harper Lee")
    book1.set_price("$12-18")
    print("\nИзмененная книга:")
    book1.new_output_data()
