print( "\t\t\t PRINT STATEMENTS TYPES ")
name = "sharan"
age = 20
list = [1,2,3,4,5]
mark = 75.5
tuple = ("pen", "pencil", 23,89, True)
set = {"lion", "cat", 45,65, False}
dictionary ={"no. ": 34, "street" : "second street", "area" : "avadi","state" : "tamilandu","country":"india"}
print("\t\t\tFIRST PRINT TYPE:")
print( "my name is " +name+ " and age is " +str(age)+" .\n" "my mark is "+str(mark)+ " .\n" "item in list " +str(list)+ "\n" "items in tuple "
       +str(tuple)+ "\n" " items in set " +str(set)+".\n" " items in dictionary " +str(dictionary))
print("\n")
print("\t\t\t SECOND PRINT TYPE;")
print(" my name is %s and age is %s.\n my mark is %s.\n item in list %s\n items in tuple %s\n items in set %s\n items in dictionary %s"
     %(name, age, mark, list, tuple, set, dictionary))
print("\n")
print("\t\t\t THIRD PRINT TYPE:")
print(""" my name is {} and age is {}.\n my mark is {}.\n items in list {}\n items in tuple {}\n items in set {}\n items in dictionary {}"""
      .format(name, age, mark, list, tuple, set, dictionary))
print("\n")
print("\t\t\t FOURTH PRINT TYPE:")
print(f" my name is {name} and age is {age}.\n my mark is {mark}.\n item in list {list}\n items in tuple {tuple}\n items in set{set}\n "
      f"items in dictionary {dictionary}")
