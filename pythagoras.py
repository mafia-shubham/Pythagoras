
import math 
from math import sqrt

class Pythagoras:
    def __init__(self):
        super().__init__()

        print("\n\n\n\n\n\n\n-----------------------------------------------------------------🔰 Welcome To Pythagoras Therom🔰----------------------------------------------------------------\n")
        print("❤️   Here You Can Get Your Answers About - Pythagoras Therom ! ❤️\n")
        print("⚠️  ⚠️  ⚠️   If You Dont Have Any Value - Set It 0 ⚠️  ⚠️  ⚠️\n ")
        print("❤️   Formula ----> (Hypotenius)² = (Base)² + (Height)²\n")
        print("❤️   Try To Use Pythagoras Triads !\n")
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        
        def inputs_work():

            while True :
                try :
                   print("⚠️    If You Want To Quit Enter - Ctrl + C - 🔰")
                   print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------") 

                   hypot = int(input("\n⚡  Enter Hypotenius : ---> "))
                   base = int(input("\n⚡  Enter Base : ---> "))
                   height = int(input("\n⚡  Enter Height : ---> "))

                   break

                except Exception as e :
                    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                    print("\n Please Enter Number Only . If You Dont Have Any Value - Set It 0  \n")
                
                except KeyboardInterrupt as f :
                                
                    print(" ")
                    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                    print("")                    
                    print(" ❤️   Ok - Quiting ! \n")
                    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n") 

                    exit()

            print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
            
            if hypot == 0 | base == 0 | height == 0 or hypot == 0 | base == 0 or hypot == 0 | height == 0 or base == 0 | height == 0 :
                print("\n Don't Make Me A Fool ! 😂 - Because - You Think You Are Bad , But I am Your Dad 😈 ")

            elif hypot == 0 :
                hypot = int(base) * int(base) + int(height) * int(height)
                print("")
                print(f"➡️   Hypotenius = {int(base)} ²  +  {int(height)} ² \n")
                print(f"➡️   Hypotenius = {int(base) * int(base)} + {int(height) * int(height)} \n")
                print(f"➡️   sqrt Hypotenius = sqrt {hypot} \n")
                print("💝 Your Hypotenius Is = ", end = "")
                print(sqrt(hypot))
            
            elif hypot < base or hypot < height :
                print("\n Don't Make Me A Fool ! - Because Hypotenius Is Bigger Than Both 👋") 


            elif base == 0 :
                base = int(hypot) * int(hypot) - int(height) * int(height)
                print("")
                print(f"➡️    Base = {int(hypot)} ²  -  {int(height)} ²\n")
                print(f"➡️    Base = {int(hypot) * int(hypot)} - {int(height) * int(height)} \n")
                print(f"➡️    sqrt Base = sqrt {base} \n")
                print("\n💝 Your Base Is = " , end = "")
                print(sqrt(base))       

            elif height == 0 :
                height = int(hypot) * int(hypot) - int(base) * int(base)
                print("")
                print(f"➡️    Height = {int(hypot)} ²  - {int(base)} ²\n")
                print(f"➡️    Height = {int(hypot) * int(hypot)} - {int(base) * int(base)} \n")
                print(f"➡️    sqrt Height = sqrt {height} \n")
                print("\n💝 Your Height Is = ", end = "" )
                print(sqrt(height))

            else :
                print("\n 🆗 Good Byy Sir 👋👋\n")
                print("\n 🔰 Thanks For Using Our Code ! 🔰\n")
            
        
        inputs_work()
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------\n") 
                        
window = Pythagoras()


