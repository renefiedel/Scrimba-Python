# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split(' ')) # the ' ' will account to spaces or object
# print(csv.split(','))
# print('-'.join(friends_list)) # adds hyphens
# print(''.join(msg.split()))
# eliminates all spaces


# Exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print((','.join(','.join(csv.split(':')).split(';'))).split(','))
print('replace', csv.replace(':',',').replace(';',',').split(','))
friends_list = (','.join(','.join(csv.split(':')).split(';'))).split(',')
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

