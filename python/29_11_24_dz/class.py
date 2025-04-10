import functools

def add_give_milk(cls):
    def give_milk(self):
        print(f"{self.name} gives milk")
    cls.give_milk = give_milk
    return cls

@add_give_milk
class Cow:
    def __init__(self, name = 'cow', age = 1, weight = 500, quote = 'moo'):
        self._name = f'cow {name}'
        self._age = age
        self._weight = weight
        self._quote = quote
    @property
    def name(self):
        return self._name

    def eat(self):
        print(f"{self._name} кушает.")

    def give_quote(self):
        print(f'{self._name} издает звук: {self._quote}')
        
cow = Cow("Буренка", 3, 750)
cow.eat() 
cow.give_quote()
cow.give_milk()
print(cow.name)