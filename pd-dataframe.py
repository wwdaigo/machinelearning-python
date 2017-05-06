import pandas as pd

d = {
	'name': pd.Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index = ['a', 'b', 'c', 'd']),
	'age': pd.Series([22,38,26,35], index = ['a', 'b', 'c', 'd']),
	'fare': pd.Series([7.25,71.83,8.05], index = ['a', 'b', 'd']),
	'survived?': pd.Series([False, True, True, False], index = ['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
#print df
'''
   age   fare       name  survived?
a   22   7.25     Braund      False
b   38  71.83   Cummings       True
c   26    NaN  Heikkinen       True
d   35   8.05      Allen      False
'''

cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'Kitten'])
#print cuteness > 3
'''
Cockroach    False
Fish         False
Mini Pig     False
Puppy         True
Kitten        True
dtype: bool
'''
#print cuteness[cuteness > 3]
'''
Puppy     4
Kitten    5
dtype: int64
'''


series = pd.Series(['Dave', 'Cheng-Han', 359, 9001], 
	index=['Instructor', 'Curriculum Manager','Course Number', 'Power Level'])
'''
Instructor                 Dave
Curriculum Manager    Cheng-Han
Course Number               359
Power Level                9001
'''
print series['Instructor']
#Dave

print series[['Instructor', 'Curriculum Manager', 'Course Number']]
'''
Instructor                 Dave
Curriculum Manager    Cheng-Han
Course Number               359
'''