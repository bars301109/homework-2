# ООП
# Принципы ООП

class Book:
    strr = 400

    #Методы

    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author}, \n'
                f'color: {self.color}, {self.strr}, \n')

    def __len__(self):
        return len(self.title + self.author + self.color)

# объект\экзэмпляр класса
gород_воров = Book('Город воров', 'Каныкей', 'Зеленый')
kапитанская_дочка = Book('Капитанская дочка', 'Пушкин', 'Серый')

beka = Book('Этомир', "beka", 'black')
print(len(beka))


print(gород_воров)
print(kапитанская_дочка)

ls = [1, 1, 1, 1, 1]
print(ls)
#gород_воров.info()
#kапитанская_дочка.info()
