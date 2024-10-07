# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# define variables (set lowbound to 0 for pt 3/initial solution and set lowbound to 1 for pt 4/revised solution)
pizza = LpVariable("pizza", lowBound=1) 
salad = LpVariable("salad", lowBound=1) 
cereal = LpVariable("cereal", lowBound=1)
beef = LpVariable("beef", lowBound=1) 
salmon = LpVariable("salmon", lowBound=1) 

#define the problem
prob = LpProblem("diet", LpMinimize)

#define constraints
#sodium
prob += 900*pizza + 340*salad + 150*cereal + 810*beef + 540*salmon <= 35000
#energy
prob += 310*pizza + 140*salad + 190*cereal + 180*beef + 60*salmon >= 14000
#protein
prob += 14*pizza + 2*salad + 9*cereal + 17*beef + 12*salmon >= 350
#vitamin d
prob += 0*pizza + 0.1*salad + 3*cereal + 1.6*beef + 18*salmon >= 140
#calcium
prob += 353*pizza + 60*salad + 333*cereal + 80*beef + 3*salmon >= 9100
#iron
prob += 1*pizza + 0.8*salad + 18*cereal + 2.9*beef + 0*salmon >= 126
#potassium
prob += 291*pizza + 240*salad + 360*cereal + 1150*beef + 194*salmon >= 32900

#define objective function
prob += 1.5*pizza + 1.33*salad + 0.6*cereal + 3.77*beef + 4.33*salmon

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")
# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    print(f"Objective = {value(prob.objective)}")
    print(f"")

