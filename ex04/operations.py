import sys

def operations(A, B):
    "This function blah blah"
    try:
        x = int(A)
        y = int(B)
        print("Sum:        ", str(x + y))
        print("Difference: ", str(x - y))
        print("Product:    ", str(x * y))
        try:
            res = x / y
            formatted = '{:.4f}'.format(res)
            if len(formatted) < len(str(res)):
                print("Quotient:   ", formatted + '...')
            else:
                print("Quotient:   ", str(res))
            print("Remainder:  ", str(x % y))
        except ZeroDivisionError:
            print("Quotient:    ERROR (division by zero)")
            print("Remainder:   ERROR (modulo by zero)")
    except ValueError:
        print ("AssertionError: only integers")

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print ("AssertionError: too many arguments")
    else:
        operations(sys.argv[1], sys.argv[2])


