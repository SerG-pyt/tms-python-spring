class Math:
    """Класс производит арифметические вычисления"""
    @staticmethod
    def add_num(a: int or float, b: int or float) -> int or float:
        """Ф-ция находит сумму двух входящих элементов"""
        print(f"{a} + {b} = {a + b}")
        return a + b

    @staticmethod
    def sub_num(a: int or float, b: int or float) -> int or float:
        """Ф-ция отнимает второй входящий элемент от первого"""
        print(f"{a} - {b} = {a - b}")
        return a - b

    @staticmethod
    def mul_num(a: int or float, b: int or float) -> int or float:
        """Ф-ция находит произведение двух входящих элементов"""
        print(f"{a} * {b} = {a * b}")
        return a * b

    @staticmethod
    def div_num(a: int or float, b: int or float) -> int or float:
        """Ф-ция делит первый входящий элемент на второй"""
        print(f"{a} / {b} = {a / b}")
        return a / b