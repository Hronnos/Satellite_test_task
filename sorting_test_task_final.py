# final_method
list_of_values = [(1, 'event11'), (5, 'event12'), (15, 'event13'),
                  (3, 'event21'), (5, 'event22'), (7, 'event23'), (2, 'event31')
                  ]
sorted_list = []
def gen(list_of_values):
   while len(list_of_values) != 0:
      minn = list_of_values.pop(list_of_values.index(min(list_of_values)))
      yield minn

for i in gen(list_of_values):
   sorted_list.append(i)

print(sorted_list)
