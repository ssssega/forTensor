#1
point = [0,0]
command = list(input("Where to move (e.g. 'Down 2'): ").split())
command[1] = float(command[1])

if command[0] == "Up" and command[1]>=0:
    point[1] += command[1]
elif command[0] == "Down" and command[1]>=0:
    point[1] -= command[1]
elif command[0] == "Right" and command[1]>=0:
    point[0] += command[1]
elif command[0] == "Left" and command[1]>=0:
    point[0] -= command[1]
else:
    print("Invalid command, try again")

print("Your hero at a point with coordinates: %s, %s" %(point[0],point[1]))

#2
point = [0,0]
while True:
    command = list(input("Where to move (e.g. 'Down 2'): ").split())

    if command[0] == "Up" and float(command[1])>=0:
        point[1] += float(command[1])
        print("Your hero at a point with coordinates: %s, %s" %(point[0],point[1]))
    elif command[0] == "Down" and float(command[1])>=0:
        point[1] -= float(command[1])
        print("Your hero at a point with coordinates: %s, %s" %(point[0],point[1]))
    elif command[0] == "Right" and float(command[1])>=0:
        point[0] += float(command[1])
        print("Your hero at a point with coordinates: %s, %s" %(point[0],point[1]))
    elif command[0] == "Left" and float(command[1])>=0:
        point[0] -= float(command[1])
        print("Your hero at a point with coordinates: %s, %s" %(point[0],point[1]))
    elif command[0] == "Stop":
        break
    else:
        print("Invalid command, try again")

#3
cf = list(map(float, input("Input a coefficients of the equation (e.g. '5 -6 3'): ").split()))
D = cf[1]**2 - 4*cf[0]*cf[2]
if cf[0]==0:
    print("Is linear equation!")
elif D > 0:
    x1 = (-cf[1]+D**0.5)/(2*cf[0])
    x2 = (-cf[1]-D**0.5)/(2*cf[0])
    print("Roots of equation: X1=%.2f, X2=%.2f" %(x1,x2))
elif D == 0:
    x = -cf[1]/(2*cf[0])
    print("Root of equation: X=%2f" %(x))
elif D < 0:
    print("Solution of equation is complex number")
else:
    print("Invalid value of coefficients, try again")

#4
cf = list(map(float, input("Input a coefficients of the equation (e.g. '5 -6 3'): ").split()))
cf = list(map(complex, cf))
D = cf[1] ** 2 - 4 * cf[0] * cf[2]
if cf[0] == 0:
    print("Linear equation!")
elif D != 0:
    x1 = (-cf[1]+D**0.5)/(2 * cf[0])
    x2 = (-cf[1]-D**0.5)/(2 * cf[0])
    x1 = complex(x1.real, x1.imag)
    x2 = complex(x2.real, x2.imag)
    if x1.imag == 0.0:
        x1 = x1.real
    if x2.imag == 0.0:
        x2 = x2.real
    print("Roots of equation: X1={:.2f}, X2={:.2f}" .format(x1,x2))
elif D == 0:
    x = -cf[1]/(2 * cf[0])
    x = complex(x.real, x.imag)
    print("Root of equation: X={:.2f}" .format(x))
else:
    print("Invalid value of coefficients, try again")