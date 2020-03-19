import math

min_value = 9999
min_list = []

l2 = math.log(2.0)
l3 = math.log(3.0)
l5 = math.log(5.0)
l7 = math.log(7.0)
l11 = math.log(11.0)
l13 = math.log(13.0)
l17 = math.log(17.0)
l19 = math.log(19.0)
l23 = math.log(23.0)

for n1 in range(10):
    print n1
    for n2 in range(10):
        for n3 in range(10):
            for n4 in range(10):
                for n5 in range(5):
                    for n6 in range(5):
                        for n7 in range(5):
                            for n8 in range(3):
                                for n9 in range(3):
                                    if (2*n1+1)*(2*n2+1)*(2*n3+1)*(2*n4+1)*(2*n5+1)*(2*n6+1)*(2*n7+1)*(2*n8+1)*(2*n9+1)>1999:
                                        t = n1*l2+n2*l3+n3*l5+n4*l7+n5*l11+n6*l13+n7*l17+n8*l19+n9*l23
                                        if t<min_value:
                                            min_value = t
                                            min_list = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
                                            break

print min_list
