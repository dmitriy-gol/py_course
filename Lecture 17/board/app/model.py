from sqlalchemy import Integer, Column, DateTime, String, func

from app.database import Base


class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, server_default=func.now())
    author = Column(String, nullable=False)
    content = Column(String, nullable=False)