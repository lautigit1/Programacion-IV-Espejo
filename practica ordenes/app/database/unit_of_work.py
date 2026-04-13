from sqlmodel import Session
from app.database.session import engine

class UnitOfWork:
    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = Session(engine)
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.session.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()
