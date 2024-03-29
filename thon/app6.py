command =""
started= False
while True:
    command=input(">")
    if command.lower()=="start":
        if started:
           print("car has already started")
        else:
            started=True
            print("car has started")    
   
    elif command.lower()=="stop":
        if not started:
               print("car has already stopped! ")
        else:
            started= False    
            print("Car stopped...")
    elif command.lower()=="help":
        print("""
Start - to start the car
stop - to stop the car  
quit - to quit 
            """)
    elif command.lower()== "quit":
         break
    else:
      print("sorry i dont understand that")
               