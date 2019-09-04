from gekko import GEKKO
m = GEKKO()             # create GEKKO model

# Constants and Variables
a = 40 
x = m.Var(value=0)      # define new variable, initial value=0
y = m.Var(value=1)      # define new variable, initial value=1

# Equations
m.Equations([x + 2*y==0,     # equations
             x**2+y**2==1]) 

# solve
m.solve(disp=False)     
print([x.value[0],y.value[0]]) # print solution
