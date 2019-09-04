from gekko import GEKKO
m = GEKKO()             # create GEKKO model
m._path = r'C:\test'    # save modell to files

# Constants and Variables
a = m.Var(value=0.5) 
x = m.Var(value=0)      # define new variable, initial value=0
y = m.Var(value=1)      # define new variable, initial value=1

# Equations
m.Equations([x + 2*y==0,     # equations
             x**2+y**2==1,
             a+x==1]) 

# solve
m.solve(disp=False)     
print([x.value[0],y.value[0],a.value[0]]) # print solution
