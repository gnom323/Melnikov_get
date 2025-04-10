class University:
    def __init__(self, name, location, year_of_foundation, budget, num_of_students):
        self.name = name
        self.location = location
        self.year_of_foundation = year_of_foundation
        self.budget = budget
        self.num_of_students = num_of_students

    def get_budget(self):
        print(f"Бюджет {self.name}: {self.budget}$")

    def scholarship(self):
        single_amount = int(input("Размер стипендии ($): "))
        full_amount = single_amount * self.num_of_students
        if full_amount > self.budget:
            print(f'Недостаточно средств в бюджете. Необходимо еще {full_amount - self.budget}$')
        else:
            print(f"Потрачено {full_amount}$. В бюджете осталось {self.budget - full_amount}")
            self.budget -= full_amount

class Faculty(University):
    def __init__(self, name, location, year_of_foundation, budget, num_of_students):
        super().__init__(name, location, year_of_foundation, budget, num_of_students)
        
    
    def Exam(self):
        exam_type = input('Тип экзамена: ')
        exam_subject = input('Предмет: ')
        exam_date = input('Дата экзамена: ')
        print(f"{exam_type} по предмету -> {exam_subject} будет проведен {exam_date}")
    
    def get_budget(self):
        super().get_budget()
    
    def scholarship(self):
        super().scholarship()
        

MIPT = University('MIPT', 'Dolgoprudny', 1946, 10000000, 5000)

FPQE = Faculty('FPQE', 'Dolgoprudny', 1964, 100000, 800)
MIPT.get_budget()
FPQE.get_budget()
FPQE.Exam()
FPQE.scholarship()