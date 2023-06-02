#Задание 1
class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0
    
    
    def push(self, item) -> None:
        self.data.insert(0, item)

    def pop(self):
        if self.is_empty():
            pass
        else:
            return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            pass
        else:
            return self.data[0]

    def size(self):
        return len(self.data)
    
#Задание 2
def check_figure_balance(data:str):
    
    figure_dict = {
                '{':'f','}':'f',
                '(':'c',')':'c',
                '[':'s',']':'s'
                }
    
    for figure in data:
        if figure in ['(','{','[']:
            Stacker.push(figure_dict[figure])
        elif figure in [')','}',']']:
            if Stacker.peek() == figure_dict[figure]:
                Stacker.pop()
            else:
                print('Несбалансировано')
                return
            
    if Stacker.is_empty():
        print('Сбалансировано')
        return
    
if __name__ == '__main__':
    Stacker = Stack()
    data_1 = "(((([{}]))))"
    data_2 = "[([])((([[[]]])))]{()}"
    data_3 = '{{[()]}}'
    #
    data_4 = "}{}"
    data_5 = "{{[(])]}}"
    data_6 = "[[{())}]"
    check_figure_balance(data_1)
    




