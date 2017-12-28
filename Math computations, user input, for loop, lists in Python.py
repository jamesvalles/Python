#Math computations, user input, for loop in Python

#Problem A

import math

p1 = [1.4, 8.9]
p2 = [7.8, 12.6]
distance = math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[-1] - p1[-1]) ** 2))
print(distance)


#Problem B

wall_lengths = [8, 4, 4, 6, 4, 10]
total_cans= (sum(wall_lengths) * 10) / 250
print(math.ceil(total_cans))

#Problem C


user_xy = []
user_xy.append(eval(input('Please enter a new x point: ')))
user_xy.append(eval(input('Please enter a new y point: ')))

if 1.4 < user_xy[0] < 7.8  and 8.9 < user_xy[-1] < 12.6: 
        print('True')
        
else:
        print('False') 


#Problem D

ndivide = []
for number in range(1,151):
    if number%6 == 0 and not number%4 == 0 :
        ndivide.append(number)
print(ndivide)
        

#Problem E - Extra Credit

def average(list):
    'Returns the average of scores entered by user.'
    avg = sum(list)/len(list)
    return avg

number_scores = eval(input('Please enter the number of scores you would like to enter: '))
list = []
 
for s in range(number_scores):
    list.append(eval(input('Please enter each score: ')))
print(average(list))


                

                    
                    




                      
                    
                
    
                  
