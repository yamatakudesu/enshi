def Tarai(x, y, z):
    if x <= y:
        return y
    else:
        return Tarai(Tarai(x-1, y, z), Tarai(y-1, x, z), Tarai(z-1, x, y))

x = input('x = ')
y = input('y = ')
z = input('z = ')

print ("Tarai(x, y, z) = {}".format(Tarai(x, y, z)))
