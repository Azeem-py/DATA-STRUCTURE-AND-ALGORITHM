
# Assuming you want to drop a few grades off your list by the end of the semester, 
# you can use the method in the drop_first_last function.



def avg(values):
    average = sum(values)
    return average

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)



grades = [20, 50, 90, 86, 56, 78, 76, 49, 100, 94, 98]
print(drop_first_last(grades))


#now assuming you've gotten N lenght of data but you are aware the first and the second data are name and email respectively 
# but the rest of the structure is an unknown amout of phone number. 
# You can easily un pack them like this

record = ('Azeem', 'bljazeem@gmail.com', '+2349095021208', '+2349121292342')

name, email, *numbers = record

print(numbers)

# The starred variable can also be the first one in the list. For example, say you have a
# sequence of values representing your company’s sales figures for the last eight quarters.
# If you want to see how the most recent quarter stacks up to the average of the first seven,
# you could do something like this:

sales_record = [100.76, 459.56, 987.46, 234.89, 600.00, 945.57, 123.98, 786.74]

*first_seven, most_recent = sales_record
first_seven_avg = sum(first_seven)/len(sales_record)
print(first_seven_avg, 'vs', most_recent)

#the star unpacking can be useful when dealing with tuples of different lenth
#For example, a tuple that uses the first element as a tag
#imagine a list of students with their name, course department including the subjects they take (each student's data is a tuple)

#the first tag in each tuple is the name, second is the department while the rest are the subjects
students = [
    ('Azeem', 'science', "math", "physics", "ICT"),
    ('Kawojue', 'science', "math", "biology",),
    ('Ruqiyah', "Art", "creative art", "litrature", 'english'),
    ('Precious', "Commercial", 'economics'),
]



for name, dept, *subjects in students:
    print(f'Name is {name}, {dept} department. Takes this courses: {subjects}')



#another use case is string processing.
#Let's try to get the name of a repo from the url

*_, repo_name = 'https://github.com/Azeem-py/DATA-STRUCTURE-AND-ALGORITHM.git'.split('/')
print(repo_name)


#we can also use it for some kind of recursion.

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [2,8,7,5,7,4]

print(sum(items))