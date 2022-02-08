#C=5/9*(F-32)
def F2C():
    '''Input Fahrenheit temp and return Celsius temp'''
    ftemp = float(input("Input Fahrenheit temp: "))
    ctemp = 5.0/9*(ftemp - 32)
    return(ctemp)



def main():
    print(f"Celsius temp is: {F2C()}")

if __name__ == '__main__':
    main()