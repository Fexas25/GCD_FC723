#in this function calculate_gcd, we calculate gce between two number according to the algorithm
#gcd(a,b)=gcd(b,a%b) gcd(b, 0) = b
#repeat this until the remainder =0, then we find the gcd
def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a%b)#a->b, b->remainder(a%b)

#this is a input function, only avaiable for positive number
def get_number():
    while True:
        a = int(input("Enter a non-negative number:"))
        b = int(input("Enter a non-negative number:"))
        if a < 0 or b < 0:
            print("Invalid number")#give error message
        else:
            print(f"GCD of {a} and {b} is {calculate_gcd(a, b)}")
            break

get_number()