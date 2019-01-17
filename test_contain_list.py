
big_list = [['cybershake', '50', 'input01'], ['cybershake', '100', 'input02']]

sub_list = ['cybershake', '50', 'input01']

i = 0
n = 0

while i == 0 and n < len(big_list):
    if(sub_list == big_list[n]):
        i = n + 1
        print("found in " + str(i))
    
    n += 1

if(i == 0):
    print("not found")