import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list

        self.title("To-Do App")
        self.geometry("300x400")

        # Add a todo list widget
        self.todo_list_widget = tk.Listbox(self)
        self.todo_list_widget.pack(side=tk.TOP, fill=tk.X)
        self.update_todo_list()

        # Add a done button
        self.done_button = tk.Button(
            self,
            text="Mark as Done",
            command=self.mark_as_done
        )
        self.done_button.pack(pady=10, fill=tk.X)

        # Add task create input
        self.task_create = tk.Text(self, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        self.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            self.todo_list.add(description=task_text)
            self.update_todo_list()

        self.task_create.delete(1.0, tk.END)

    def mark_as_done(self):
        task_index = self.todo_list_widget.curselection()[0]
        self.todo_list.delete(task_index)
        self.update_todo_list()

    def update_todo_list(self):
        self.todo_list_widget.delete(0, tk.END)
        self.todo_list.tasks

        for task in self.todo_list.tasks:
            self.todo_list_widget.insert(tk.END, task.description)
