# carlist.py
# Infodb list
InfoDb = []
# List with dictionary key/values placed in a list
InfoDb.append({
   "Food": "Fruit",
   "Beverage": "Soda",
   "Dessert": "Ice Cream",
   "Cake": "Chocolate",
   "Restaurant": ["Rubio's", "Wendy's", "Pollo Loco"]
})


# given and index this will print InfoDb content

def print_data(n):
    print(InfoDb[n]["Dessert"], InfoDb[n]["Cake"])  # using comma puts space between values
    print("\t", "Places: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Restaurant"]))  # join allows printing a string list with separator
    print()
# for loop iterates on length of InfoDb
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
  
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
  
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
  
def driver():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
# this is test driver or code that plays when executed directly,
# versus import which will not run these statements
  
if __name__ == "__main__":
    driver()