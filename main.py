from sqlalchemy import create_engine
from backend import Backend
from models import Base
from todo import TodoList
from ui import MainWindow


def main():
    print("Initializing database engine!")
    engine = create_engine("sqlite+pysqlite:///todo.db", echo=True)
    Base.metadata.create_all(engine)

    todo_list = TodoList(Backend(engine))
    window = MainWindow(todo_list)
    window.mainloop()


if __name__ == "__main__":
    main()