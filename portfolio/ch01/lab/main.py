import random
# Part A
weeks = 16
print(weeks, " ", type(weeks))
classes = 5
print(classes, " ", type(classes))
tuition = 6000  
print(tuition, " ", type(tuition))
cost_per_week = (tuition / classes) / weeks
print(cost_per_week, " ", type(cost_per_week)) 
print("Cost per week:", cost_per_week)
classes_per_week = 10
print(classes_per_week, " ", type(classes_per_week))
cost_per_week = cost_per_week / classes_per_week
print(cost_per_week, " ", type(cost_per_week))
cost_per_class = cost_per_week/classes_per_week
print(cost_per_class, " ", type(cost_per_class))
print("The cost per class is: ", cost_per_class)

#Part B
nums = [1,2,3,4]
print(nums, " ", type(nums))
random_num = random.choice(nums)
print(random_num, " ", type(random_num))
print("The randomly selected number is: ", random_num)

