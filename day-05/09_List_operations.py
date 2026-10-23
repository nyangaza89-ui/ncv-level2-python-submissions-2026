marks=[]

mark = int(input('Enter mark (or -1 to stop):'))

while mark != -1:
    marks.append(mark)
    mark = int(input("Enter mark (-1 to stop):"))
    
print(f'Our list has {len(marks)} elements')

for x in range(len (marks)):
    print(f'Mark {x+1} is {marks[x]}')
sum=0

for x in range(len(marks)):
    mark=marks[x]
    sum=sum+mark
    
    print(f'The sum of all marks = {sum}')
    tot=0
    for x in range(len(marks)):
        mark = marks[x]
        tot = tot+mark
        avg=tot/len (marks)
        
        print("Average of marks:{avg}")
        
    
    