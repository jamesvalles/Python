#Arrays, Basic computations in Python

#Part A

temp_f = (22 * 1.8) + 32
print(temp_f)

# Part B
answer = "Pseudohypoparathyroidism"
print("popar" in answer)

#Part C
cart = [ "Skip" ]
cart.append( "Broad" )
cart.append( "Slippery" )
cart.append( "Previous" )
cart.append( "Transport" )
cart.append( "Tab" )
print(cart)
print(len(cart))
print(max(cart, key=len))
print(min(cart, key=len))

#Part D
pulse= [70, 92, 68, 67, 89, 75, 89, 77, 81, 60, 81, 90]
print( pulse )
print(len(pulse))
print(min(pulse))
print(max(pulse))
avg = sum(pulse) / len(pulse)
print(avg)

#Part E
my_friends = ['Vito', 'Michael', 'Kay', 'Fredo', 'Connie', 'Luca']
my_friends.sort()
print(my_friends[0], my_friends[-1])


      
