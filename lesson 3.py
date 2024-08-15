# Принципы ООП, git clone
# Наследование полиморфизм инкапсуляция Абстракция

# DRY - НЕ повторяйся


# Parent class
class Book:
    def __init__(self, title, author, price,):
        self.title = title
        self.author = author
        self.price = price

    def reads(self):
        print('Я читаю книгу под авторством', self.author)
    def __str__(self):
        return (f'Название:{self.title}\n'
                f'Автор:{self.author}\n'
                f'Цена:{self.price}\n')

tamirlan = Book('Bleach', 'Tamirlan', 2500)
print(tamirlan)
tamirlan.reads()




#Child class
class Nowella(Book):
    def __init__(self, title, author, price, png):
        super().__init__(title, author, price)
        Book.__init__(self, title, author, price)
        self.png = png

    def reads(self):
        print('Я читаю книгу под авторством:', self.author, 'и я купил ее за', self.price,)
    def __str__(self):
        return (f'{super().__str__()}'
                f'Размер:{self.png}\n')
dan = Nowella('Naruto', 'Dan', 2000, '70x20')
dan.reads()
print(dan)


class Manga: ...
class Anime: ...