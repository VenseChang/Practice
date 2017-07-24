from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Enum



engine = create_engine('sqlite:///data/nobel_prize.db', echo = True)
Base = declarative_base()

class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return '<Winner(name = {name}, category = {category}, year = {year})>'.format(name = self.name, category = self.category, year = self.year)


Base.metadata.create_all(engine)