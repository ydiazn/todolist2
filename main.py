from todo import TodoList
from ui import MainWindow


def main():
    todo_list = TodoList()
    window = MainWindow()
    window.mainloop()


if __name__ == "__main__":
    main()