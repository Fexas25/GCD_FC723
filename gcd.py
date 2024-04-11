#this class is about the euclideanalgorithm
class EuclideanAlgorithm:
    #in this function calculate_gcd, we calculate gce between two number according to the algorithm
    #gcd(a,b)=gcd(b,a%b) gcd(b, 0) = b
    #repeat this until the remainder =0, then we find the gcd
    def calculate_gcd(self, a, b):
        while b != 0:
            remainder = a % b
            a = b#a->b
            b = remainder#b->remainder
        return a

a =  EuclideanAlgorithm()
print(a.calculate_gcd(10,20))

