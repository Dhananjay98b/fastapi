# import pandas as pd 
# my_data = {
#     "mydata":"Dhananjay",
#     "surname":"Bhupathi",
#     "topper":[10,20,30,40]
# }

# print(my_data)
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  "names":["dhananjay","swami","simha"],
  "subject":["Python","sql","Ds"]

}

myvar = pd.DataFrame(mydataset)

print(myvar)
a = [1,73,2]
se = pd.Series(a,index=["x", "y", "z"])
print(se)
# print(se[0])
# print(se)
c = ["dhanu","swami","simha"]
da = pd.Series(c,index=["son","father","mother"])
print(da)

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

import pandas as pd

calories = {"da1": 420, "da2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["da", "da2"])

print(myvar)