
# Number to Grade 
# Code By Samir Talukder 
# Point e point e coding 1

English= float(input("Enter English Marks: "))

Bangla= float(input("Enter Bangla Marks: "))

ICT = float(input("Enter ICT Marks: "))

Math = float(input("Enter Math Marks: "))

Science= float(input("Enter Science Marks: "))


total = English+Bangla+ICT+Math+Science
percentage = (total/500)*100

print ("Total Marks = %.2f" %total)

print ("Marks Percentage= %.2f " %percentage)

if (percentage >=90):
    print("High Garde")
 


