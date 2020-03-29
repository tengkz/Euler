f = open('p054_poker.txt','r')
data = f.readlines()

card_dict = {'T':10,'J':11,'Q':12,'K':13,'A':14}
dict_card = {10:'A',11:'B',12:'C',13:'D',14:'E'}

def re_card(num):
    if num<=9:
        return str(num)
    else:
        return dict_card[num]

def parse_card(s):
    s1 = s[0]
    s2 = s[1]
    if s1>='2' and s1<='9':
        return (int(s1),s2)
    else:
        return (card_dict[s1],s2)

def parse_hand(h):
    hands = [parse_card(card) for card in h]
    return hands

def extract_hand(h):
    # statistics
    num_dict = {}
    suit_dict = {}
    for item in h:
        num_dict[item[0]] = num_dict.get(item[0],0)+1
        suit_dict[item[1]] = num_dict.get(item[1],0)+1
    num_k = num_dict.keys()
    suit_k = suit_dict.keys()
    # is royal flush,0/1
    royal_flush_flag = '0'
    if len(num_k)==5 and max(num_k)==14 and min(num_k)==10 and len(suit_k)==1:
        royal_flush_flag='1'
    # is straight flush,min_value
    straight_flush_flag = '0'
    if len(num_k)==5 and max(num_k)-min(num_k)==4 and len(suit_k)==1:
        straight_flush_flag=re_card(min(num_k))
    # four of a kind,value
    four_of_a_kind_flag = '0'
    for k,v in num_dict.iteritems():
        if v==4:
            four_of_a_kind_flag= re_card(k)
    # full house,value of three card
    full_house_flag = '0'
    if 3 in num_dict.values() and 2 in num_dict.values():
        for k,v in num_dict.iteritems():
            if v==3:
                full_house_flag = re_card(k)
    # flush,0/1
    flush_flag = '0'
    if len(suit_dict.keys())==1:
        flush_flag='1'
    # straight,min_value
    straight_flag = '0'
    if len(num_k)==5 and max(num_k)-min(num_k)==4:
        straight_flag = re_card(min(num_k))
    # three of a kind,value
    three_of_a_kind_flag = '0'
    for k,v in num_dict.iteritems():
        if v==3:
            three_of_a_kind_flag=re_card(k)
    # two pairs,max_value
    two_pairs_flag = '0'
    max_value = 0
    if num_dict.values().count(2)==2:
        for k,v in num_dict.iteritems():
            if v==2:
                if k>max_value:
                    max_value = k
    two_pairs_flag = re_card(max_value)
    # one pair
    one_pair_flag = '0'
    max_value = 0
    for k,v in num_dict.iteritems():
        if v==2:
            if k>max_value:
                max_value = k
    one_pair_flag = re_card(max_value)
    # high card
    high_card_flag = re_card(max(num_k))
    ret = ''.join([royal_flush_flag,straight_flush_flag,four_of_a_kind_flag,full_house_flag,flush_flag,straight_flag,three_of_a_kind_flag,two_pairs_flag,one_pair_flag,high_card_flag])

    return ret

s1 = 0
s2 = 0
s0 = 0
for d in data:
    t = d.strip().split(' ')
    r1 = extract_hand(parse_hand(t[0:5]))
    r2 = extract_hand(parse_hand(t[5:10]))
    if r1>r2:
        s1+=1
    elif r1<r2:
        s2+=1
    else:
        s0+=1
print s1,s2,s0

#t = data[0].strip().split(' ')
#test0 = ['TC','JC','QC','KC','AC']
#test1 = ['9C','TC','JC','QC','KC']
#test2 = ['8S','8D','8H','8A','9C']
#test3 = ['8S','8S','9C','9S','9D']
#test4 = ['2C','3C','4C','5C','7C']
#test5 = ['2C','3S','4D','5C','6S']
#test6 = ['3C','3D','3S','9S','TD']
#test7 = ['3C','3D','4C','4D','5S']
#test8 = ['3C','3D','4C','5D','7S']
#test9 = ['2C','4D','6S','8D','9H']
#print test0,extract_hand(parse_hand(test0))
#print test1,extract_hand(parse_hand(test1))
#print test2,extract_hand(parse_hand(test2))
#print test3,extract_hand(parse_hand(test3))
#print test4,extract_hand(parse_hand(test4))
#print test5,extract_hand(parse_hand(test5))
#print test6,extract_hand(parse_hand(test6))
#print test7,extract_hand(parse_hand(test7))
#print test8,extract_hand(parse_hand(test8))
#print test9,extract_hand(parse_hand(test9))
