if __name__ == "__main__":
    class Market:
        """
        Класс "Рынок".
        """

        def __init__(self, name: str) -> None:
            """
            Создание и подготовка к работе объекта "Рынок".
            :param name: Название рынка
            Примеры:
            >>> market = Market('Ali')  # инициализация экземпляра класса
            """
            self.name = name

        def __str__(self) -> str:
            """
            Магический метод __str__(self).
            :return: Строка
            Примеры:
            >>> market = Market('Ali')  # инициализация экземпляра класса
            >>> print(market)
            """
            return f'Класс {self.__class__.__name__}'

        def __repr__(self) -> str:
            """
            Магический метод __repr__(self).
            :return: Строка
            Примеры:
            >>> market = Market('Ali')  # инициализация экземпляра класса
            >>> print(repr(market))
            """
            return f'{self.__class__.__name__}(name={self.name!r})'

        def pay(self) -> None:
            """
            Метод хранит разрешенные типы оплаты покупок.
            Примеры:
            >>> market = Market('Ali')  # инициализация экземпляра класса
            >>> market.pay()
            """
            ...

        def prod(self) -> None:
            """
            Метод хранит список товаров.
            Примеры:
            >>> market = Market('Ali')  # инициализация экземпляра класса
            >>> market.prod()
            """
            ...


    class OnlineMarket(Market):
        """
        Класс продажа онлайн.
        """

        def pay(self) -> None:
            """
            Метод хранит разрешенные типы оплаты покупок.
            Возможен только безналичный способ оплаты.
            Примеры:
            >>> on_market = OnlineMarket('Ali')  # инициализация экземпляра класса
            >>> on_market.prod()
            """
            ...