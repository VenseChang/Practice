from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

nobel_winners =[
     {
        'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921
    },
    {
        'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933
    },
    {
        'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911
    }
]

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