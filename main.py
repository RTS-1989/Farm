class Animals:
    '''Модель животного'''

    weight_sum = 0
    
    def __init__(self, animal_type, name: str, weight: int, voice):
        self.type = animal_type
        self.name = name
        self.weight = weight
        self.voice = voice
        self.hunger = 'голодный'
        Animals.weight_sum += self.weight

    def __repr__(self) -> str:
        return ('{Animal: вид %s, имя: %s, вес: %s кг, говорит: %s, состояние: %s}' \
                % (self.type, self.name, self.weight, self.voice, self.hunger))
                 
    def feed(self):
        '''
        Кормит живтоных
        '''
        self.hunger = 'сытый'

         
class Mammal(Animals):
    
    milk_state = 'Нужно доить'

    def __init__(self, animal_type, name, weight, voice, milk_state):
        Animals.__init__(self, animal_type, name, weight, voice)
        self.milk_state = milk_state

    def __repr__(self) -> str:
        return ('{Animal: вид %s, имя: %s, вес: %s кг, говорит: %s, состояние: %s, Молоко: %s}' \
                % (self.type, self.name, self.weight, self.voice, self.hunger, self.milk_state))
     
    def milk(self):
        self.milk_state = 'Подоили'
        
        
class Sheep(Animals):

    def __init__(self, animal_type, name, weight, voice, wool):
        Animals.__init__(self, animal_type, name, weight, voice)
        self.wool = wool

    def __repr__(self) -> str:
        return ('{Animal: вид %s, имя: %s, вес: %s кг, говорит: %s, состояние: %s, Шерсть: %s}' \
                    % (self.type, self.name, self.weight, self.voice, self.hunger, self.wool))

    def cutwool(self):
        self.wool = 'Овцу подстригли'


class Bird(Animals):

    def __init__(self, animal_type, name, weight, voice, eggs):
        Animals.__init__(self, animal_type, name, weight, voice)
        self.eggs = eggs

    def __repr__(self) -> str:
        return ('{Animal: вид %s, имя: %s, вес: %s кг, говорит: %s, состояние: %s, Яйца: %s}' \
                    % (self.type, self.name, self.weight, self.voice, self.hunger, self.eggs))

    def collect(self):
        self.eggs = 'Яйца собрали'

        
if __name__ == '__main__':
    
    goose1 = Bird('Гусь', 'Серый', 5, 'Га-га-га!', 'Нужно собрать яйца')
    goose2 = Bird('Гусь', 'Белый', 8, 'Га-га-га!', 'Нужно собрать яйца')
    cow = Mammal('Корова', 'Манька', 450, 'Му!', 'Нужно доить')
    sheep1 = Sheep('Овца', 'Барашек', 60, 'Бе-е-е-е!', 'Пора стричь')
    sheep2 = Sheep('Овца', 'Кудрявый', 70, 'Бе-е-е-е!','Пора стричь')
    cheeken1 = Bird('Курица', 'Ко-Ко', 2, 'Кукареку!', 'Нужно собрать яйца')
    cheeken2 = Bird('Курица', 'Кукареку', 3, 'Кукареку!', 'Нужно собрать яйца')
    goat1 = Mammal('Коза', 'Рога', 60,'Ме-е-е', 'Нужно доить')
    goat2 = Mammal('Коза', 'Копыта', 70,'Ме-е-е', 'Нужно доить')
    duck = Bird('Утка', 'Кряква', 4, 'Кря!', 'Нужно собрать яйца')


animals = [goose1, goose2, cow, sheep1, sheep2, cheeken1, cheeken2, goat1, goat2, duck]
weight_dict = {}

for animal in animals:
    new_dict = {animal.name: animal.weight}
    weight_dict.update(new_dict)

print(f'Максимальной массой {max(weight_dict.values())} кг обладает {max(weight_dict, key=weight_dict.get)}')
print(f'Общая масса всех животных с фермы составляет - {Animals.weight_sum} кг')

