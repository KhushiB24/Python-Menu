ans=True
while ans:
    print("""
    1.Add Fruit Name
    2.Show Fruit Name
    3.Delete a Fruit Name
    4.Look Up Fruit Name
    5.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      fruitString = input()
      print('The Fruit Name is', fruitString)
      print("\nFruit is Added")
    elif ans=="2":
      fruitString = input()
      print('This fruit has been added')
      print("\n Fruit Name displayed")
    elif ans=="3":
      fruitString = input()
      print('This fruit has been deleted')
      print("\n Fruit is Deleted")
    elif ans=="4":
      fruitString = input()
      print('This fruit has been found!')
      print("\n Fruit Record Found")
    elif ans=="5":
      print("\n Finished") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
