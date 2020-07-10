class EventSourcer():
    # Do not change the signature of any functions
    
    def __init__(self):
        self.value = 0
        self.operations = []
        self.operands = []
        self.undo_operations = 0

    def add(self, num: int):
        self.value += num
        self.operations.append('a')
        self.operands.append(num)

    def subtract(self, num: int):
        self.value -= num
        self.operations.append('s')
        self.operands.append(num)

    def undo(self):
        for i in range(len(self.operations)-self.undo_operations-1,-1,-1):
            if self.operations[i] == 'a':
                self.value -= self.operands[i]
            else:
                self.value += self.operands[i]
            self.undo_operations += 1
            break

    def redo(self):
        for i in range(len(self.operations)-self.undo_operations-1,-1,-1):
            if self.operations[i] == 'a':
                self.value += self.operands[i]
            else:
                self.value -= self.operands[i]
            break

    def bulk_undo(self, steps: int):
        for i in range(len(self.operations)-1,len(self.operations)-1-steps,-1):
            if self.operations[i] == 'a':
                self.value -= self.operands[i]
            else:
                self.value += self.operands[i]

    def bulk_redo(self, steps: int):
        for i in range(len(self.operations)-1,len(self.operations)-1-self.undo_operations,-1):
            if self.operations[i] == 'a':
                self.value += self.operands[i]
            else:
                self.value -= self.operands[i]
