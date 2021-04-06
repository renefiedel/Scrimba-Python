# friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
# for friend in friends:
# if friend == 'Eric':
#     print('Found ' + friend + '!')
#      continue

#   print(friend)

# print("For Loop done!")

# exercise party invitation
names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)
for index in range(2):
    names.append(input('Enter two extra names: '))

for friend in names:
    print(f'{(friend.title())}! You are invited to the party on Saturday.')


