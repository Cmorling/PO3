from z3 import *

one_p = 2 #input('Hur många med styrka 1 ?')
two_p = 4 #input('hur många med styrak 2 ?')
three_p = 6 #input('Hur många med styrka 3 ?')
four_p = 8 #input('Hur många med styrka 4 ?')

comp_list = [one_p, two_p, three_p, four_p]

str_one_team = (one_p + 2*two_p + 3*three_p + 4*four_p)/2
mem_one_team = (one_p + two_p + three_p + four_p)/2

team_one = [Int(f'{i} 1') for i in range(1,5)]
team_two =[Int(f'{i} 2') for i in range(1,5)]

pp(team_one)
pp(team_two)

s = Solver()
s.add(Sum(team_one) == mem_one_team)
s.add(Sum(team_two) == mem_one_team)
s.add(Sum([n_people * (i+1) for i, n_people in enumerate(team_one)]) == str_one_team)

s.add(Sum([n_people * (i+1) for i, n_people in enumerate(team_two)]) == str_one_team)

for i in range(4):
	s.add(team_one[i] + team_two[i] == comp_list[i])
	s.add(team_one[i] >= 0)
	s.add(team_two[i] >= 0)

c = s.check()
print(c, '\n')
if c == sat:
	m = s.model()

	team_one_comp = [m.evaluate(mem) for mem in team_one]
	team_two_comp = [m.evaluate(mem) for mem in team_two]

	print('Lag 1: ', ''.join([f'{mem} ' for mem in team_one_comp]))
	print('Lag 2: ', ''.join([f'{mem} ' for mem in team_two_comp]))
