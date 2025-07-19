raycount = 10
fov = 0.5

theta = 0
delta = (fov/raycount)
print(f"Delta: {delta}")
for i in range(2*raycount+1):
    theta = ((i)/raycount) - 1
    print(theta)
