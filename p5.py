import json
import os
from datetime import datetime
FILENAME="data.json"

    
def savechanges():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
        
def expense_entry(amt,cate):        
    
    tb=data["total_budget"]

    if tb<amt:
     print("total budget insufficient")
     return 0
    else:
     if data["cat_budget"][0][cate]<amt:
    
      print(f"Not enough budget in category {cate}")
      return 0
     else:
         expense={
            "amount":amt,
            "date":datetime.now().date().isoformat(),
            "cate" :cate   
         }
         data["expense"].append(expense)
         data["total_budget"]-=amt
         data["cat_budget"][0][cate]-=amt
         
         
    savechanges()
    show_entry()
        
        
    
    
def show_entry():
    
    total_spent=0
    if os.path.exists(FILENAME):
      for exp in data["expense"]:
         total_spent += exp["amount"]
       
      return total_spent
    else:
        
        total_spent=0
    return total_spent
    



def set_budget():
    total_budget=int(input("your budget : "))
    categories = ["a", "b", "c", "d"]
    cat_budget = {}
    for cate in categories:
      cat_budget[cate] = int(input(f"Enter budget for {cate}: "))
    data["total_budget"]=total_budget
    data["cat_budget"][0]=cat_budget
    
    print(f"new budget is set as {data["total_budget"]} and {data["cat_budget"]}")
    return data["total_budget"],data["cat_budget"]








if os.path.exists(FILENAME):
    
    with open(FILENAME,"r") as f:
     data=json.load(f)       
else:
    
    data={"expense":[],
      "total_budget":0,
      "cat_budget":[]} 
    expense = {
        "amount":0,
        "date":datetime.now().date().isoformat(),
        "cate":"a"
    }
    total_budget=int(input("your budget : "))
    categories = ["a", "b", "c", "d"]
    cat_budget = {}
    for cate in categories:
      cat_budget[cate] = int(input(f"Enter budget for {cate}: "))
    data["total_budget"]=total_budget
    data["cat_budget"].append(cat_budget)
    
    

while True:
    print("1. Add expense")
    print("2. View report")
    print("3. set budget")
    print("4. exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            expense_entry(int(input("Enter the amount to spend : ")),input("enter category : "))
        case "2":
            x=show_entry()
            print(f" total spend is {x}")
            print(f"remaining budget is {data["total_budget"]} and given as {data["cat_budget"]}")
            
        case "3":
          set_budget()
        case "4":
          break
        




      


