import math

min_value = 99999999
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
l29 = math.log(29.0)
l31 = math.log(31.0)
l37 = math.log(37.0)
l41 = math.log(41.0)
l43 = math.log(43.0)

for n1 in range(10):
    print n1
    for n2 in range(5):
        for n3 in range(5):
            for n4 in range(3):
                for n5 in range(3):
                    for n6 in range(3):
                        for n7 in range(3):
                            for n8 in range(3):
                                for n9 in range(3):
                                    for n10 in range(3):
                                        for n11 in range(3):
                                            for n12 in range(3):
                                                for n13 in range(3):
                                                    for n14 in range(3):
                                                            if (2*n1+1)*(2*n2+1)*(2*n3+1)*(2*n4+1)*(2*n5+1)*(2*n6+1)*(2*n7+1)*(2*n8+1)*(2*n9+1)*(2*n10+1)*(2*n11+1)*(2*n12+1)*(2*n13+1)*(2*n14+1)>7999999:
                                                                t = n1*l2+n2*l3+n3*l5+n4*l7+n5*l11+n6*l13+n7*l17+n8*l19+n9*l23+n10*l29+n11*l31+n12*l37+n13*l41+n14*l43
                                                                if t<min_value:
                                                                    min_value = t
                                                                    min_list = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14]
                                                                    break

print min_list

# answer
print 8*27*25*49*11*13*17*19*23*29*31*37
