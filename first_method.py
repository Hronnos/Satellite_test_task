# first try

list_of_values = [(1, 'event11'), (5, 'event12'), (15, 'event13'),
                  (3, 'event21'), (5, 'event22'), (7, 'event23'), (2, 'event31')
                  ]

myDict = {list_of_values[i][0]: list_of_values[i][1] for i in range(0, len(list_of_values), 1)}

print(myDict)
# {1: 'event11', 5: 'event22', 15: 'event13', 3: 'event21', 7: 'event23', 2: 'event31'}

dict_sorted_by_key = {k: v for k, v in sorted(myDict.items())}
list_sorted_by_key = [[key, value] for key, value in dict_sorted_by_key.items()]

print(list_sorted_by_key)
# [[1, 'event11'], [2, 'event31'], [3, 'event21'], [5, 'event22'], [7, 'event23'], [15, 'event13']]