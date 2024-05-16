class TodoList:
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
        self.tasks = self.backend.getAll()

    def add(self, **kwargs):
        task = self.backend.add(**kwargs)
        self.tasks.append(task)

    def delete(self, index):
        task = self.tasks.pop(index)
        self.backend.delete(task)
