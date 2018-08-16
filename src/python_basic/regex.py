import re

#Check if the string starts with "The" and ends with "Spain":

txt = "cr something\rsomethingelse\r"
x = re.findall("cr ((.|\n|\r)*)", txt)

print(x)

if x:
  print("YES! We have a match!")
else:
  print("No match")
