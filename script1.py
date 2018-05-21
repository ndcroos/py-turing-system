import numpy as np

T = 250

delta_x = 1
delta_y = 1
delta_t = 0.05

# Gauss Jacobi data
l = 100
x = np.arange(0, 500, delta_x)
y = np.arange(0, 500, delta_y)

m = x.len()
n = y.len()
t = np.arange(0, T, delta_t)

# Parameters
D = 0.516
alpha = 0.899
gamma = -alpha
beta = -0.91
delta = 2
r1 = 3.5
r2 = 0

u = np.zeros([n+2,m+2])
v = np.zeros([n+2, m+2])

# Initialization

for j in range(2,m+1):
  for i in range (2,n+1):
    u(j,i) = 0.25
    v(j,i) = 0.25
    
step = 0
u_new = u
v_new = v

#TODO
for k in range(0,T,delta_t):
  step = step + 1
  for j in range(2,n+1):
    for i in range(2:m+1):
      u_new(j,i) = u(j,i) + 
