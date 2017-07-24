import dataset

db = dataset.connect('sqlite:///data/nobel_prize.db')
wtable = db['winners']

# insert 
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

with db as tx:
    for w in nobel_winners:
        tx['winners'].insert(w)

# select
winners = wtable.find()
print(list(winners))

# delete
winners = wtable.delete()
winners = wtable.delete(nationality = 'Swiss')

# export csv
winners = wtable.find()
dataset.freeze(winners, format='csv', filename='data/nobel_winners_ds.csv')
print(open('data/nobel_winners_ds.csv').read())