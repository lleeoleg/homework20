"""
Напишите программу, в которой есть главный класс с текстовым полем. В главное классе 
должен быть метод для присваивания значения полю: без аргументов и с одним текстовым 
аргументом. Объект главного класса создаётся передачей одного текстового аргумента 
конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно 
добавить числовое поле. У конструктора класса-потомка два аргумента
"""
class MainClass:
    """_summary_
    """
    def __init__(self, text):
        """_summary_

        Args:
            text (_type_): _description_
        """
        self.text_field = text
    def set_text(self, text=None):
        """_summary_

        Args:
            text (_type_, optional): _description_. Defaults to None.
        """
        if text is not None:
            self.text_field = text
    def get_text(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.text_field

class ChildClass(MainClass):
    """_summary_

    Args:
        MainClass (_type_): _description_
    """
    def __init__(self, text, number):
        """_summary_

        Args:
            text (_type_): _description_
            number (_type_): _description_
        """
        super().__init__(text)
        self.number_field = number
    def set_number(self, number):
        """_summary_

        Args:
            number (_type_): _description_
        """
        self.number_field = number
    def get_number(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.number_field

if __name__ == "__main__":
    main_obj = MainClass("Всем привет!")
    main_obj.set_text("Hey, everybody!")
    print(main_obj.get_text())
    child_obj = ChildClass("Текст", 7)
    print(child_obj.get_text())
    print(child_obj.get_number())
    child_obj.set_number(15)
    print(child_obj.get_number())
