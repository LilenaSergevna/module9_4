

first = 'Мама мыла раму'
second = 'Рамена мало было'

rezult=list(map(lambda x, y: x==y, first, second))
print(rezult)


def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'a') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')
        return 0

    return write_everything



write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice
class MysticBall:
    word=[]
    def __init__(self,*word):
        self.word=word

    def  __call__(self):
        return choice(self.word)



# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())





