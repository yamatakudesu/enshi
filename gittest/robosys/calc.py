def ave(data):
    ave = float(sum(data))/len(data)
    print ave

def var(data):
    s = 0
    t = 0
    for i in data:
        s += i**2
        t += i
    var = float(s)/len(data) - (float(t)/len(data))**2
    print var

if __name__ == '__main__':
    data = [1,2,3,4,5,10]
    ave(data)
    var(data)
    
    
