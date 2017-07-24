from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Enum

engine = create_engine('sqlite:///data/nobel_prize.db', echo = True)
Base = declarative_base()

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



Session = sessionmaker(bind = engine)
session = Session()
# add
winner_rows = [Winner(**w) for w in nobel_winners ]
session.add_all(winner_rows)
session.commit()


# select
result = session.query(Winner).filter_by(category = 'Physics')
print(list(result))
# ----------
result = session.query(Winner).filter(Winner.category == 'Physics', Winner.nationality != 'Swiss')
print(list(result))
# ----------
result = session.query(Winner).get(3)
print(result)
# ----------
result = session.query(Winner).order_by('year')
print(list(result))
# ----------
def inst_to_dict(inst, delete_id = True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat

winner_rows= session.query(Winner)
nobel_winners = [inst_to_dict(w) for w in winner_rows]
print(nobel_winners)