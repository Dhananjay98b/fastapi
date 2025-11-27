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
