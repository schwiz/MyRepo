from abc import ABC, abstractmethod

class Abstract(ABC):
    def __init__(self,value):
        self.value=value
        super().__init__()
    
    @abstractmethod
    def do_smthn(self):
        pass

class Add42(Abstract):
    def do_smthn(self):
        return self.value + 42
    
class Mul42(Abstract):
    def do_smthn(self):
        return self.value * 42

x = Add42(10)
y = Mul42(10)

print(x.do_smthn())
print(y.do_smthn())

