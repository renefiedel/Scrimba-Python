friends = ['Mary', 'John', 'Peter', 'Jack', 'Lulu' ]
cars = [911,130,328,535,740,308]

#friends.reverse()
#friends.sort(reverse=True)
friends.append('Mariam')
# friends.insert(1, 'Grace')
# friends[2] = 'Mike' # replaces Peter with Mike
# friends.remove('Terry')
# friends.pop()  # remove a certain index
# friends.clear()  removes values in a list
# del friends  # clears the list
# friends.extend(cars) # extend adds other lists

#friends.sort()
# new_friends = friends[:] # copy a list or friends.copy()
print(friends)
print(min(cars))

# exercise - Selling Lemonades
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
new_day = input('Enter the sale of new day: ')
sales_w2.append(int(new_day))
sales_w1.extend(sales_w2)
sales = sales_w1
# sales.sort()
best_earnings = max(sales)*1.5 # dollar price
worst_earnings = min(sales)*1.5 # you can use slice as well

# print(sales_w2)
# print(sales)
print('The Best day earnings is:', best_earnings, '$')
print('The Worst day earnings is:', worst_earnings, '$')
print('The Combined earnings is:', best_earnings + worst_earnings, '$')
# print(f'The combined profit is: {best_earnings+worst_earnings}')
