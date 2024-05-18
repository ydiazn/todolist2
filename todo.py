class TodoList:
    def __init__(self):
        super().__init__()
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def delete(self, index):
        del self.tasks[index]
