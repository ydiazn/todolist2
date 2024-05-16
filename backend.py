from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Task

class Backend:
    def __init__(self, engine):
        self.engine = engine

    def getAll(self):
        tasks = []

        with Session(self.engine, expire_on_commit=False) as session:
            for row in session.execute(select(Task)):
                tasks.append(row[0])

        return tasks

    def add(self, **kwargs):
        task = Task(**kwargs)
        with Session(self.engine, expire_on_commit=False) as session:
            session.add(task)
            session.commit()

        return task

    def delete(self, task):
        with Session(self.engine, expire_on_commit=False) as session:
            session.delete(task)
            session.commit()
