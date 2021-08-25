# final_method
list_of_values = [[(1, 'event11'), (5, 'event12'), (15, 'event13')],
                  [(3, 'event21'), (5, 'event22'), (7, 'event23')], [(2, 'event31')]
                  ]
lv = []
def flatten(value, depth):
    if depth and isinstance(value, list):
        for v in value: yield from flatten(v, depth - 1)
    else:
        yield value
        
for i in flatten(list_of_values, 2):
    lv.append(i)

sorted_list = []
def gen(lv):
    while len(lv) != 0:
        minn = lv.pop(lv.index(min(lv)))
        yield minn

for i in gen(lv):
    sorted_list.append(i)

print(sorted_list)

