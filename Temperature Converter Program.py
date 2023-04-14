def cels_to_fahr(cels):
    fahr = float(cels * 9/5 + 32)
    return fahr
    
def fahr_to_cels(fahr):
    cels = float((fahr-32) * 5/9)
    return cels

def cels_to_kelv(cels):
    kelv = float(cels + 273.15)
    return kelv

def kelv_to_cels(kelv):
    cels = float(kelv - 273.15)
    return cels

print("Select Converter:")
print("1. Celsius to Fahrenheit Converter")
print("2. Fahrenheit to Celsius Converter")
print("3. Celsius to Kelvin Converter")
print("4. Kelvin to Celsius Converter")
   
def convert():
    while True:
        choice = input("Enter Choice (1/2/3/4): ")
        if choice in("1", "2", "3", "4"):
            value = float(input("Enter the value: "))
            
            if choice == "1":
                print ("The temperature is", cels_to_fahr(value), "degree Fahrenheit")
            
            elif choice == "2":
                print ("The temperature is", fahr_to_cels(value), "degree Celsius")
            
            elif choice == "3":
                print("The temperature is", cels_to_kelv(value), "Kelvin")
            
            elif choice == "4":
                print("The temperature is", kelv_to_cels(value), "degree Celsius")
            
            other_convertion = input("Do you want to do other convertion? (y/n): ")
            if other_convertion == "n":
                print ("Thank you and Have a nice day! :)") 
                
                break
        
        else:
            print ("Invalid input!")
            
convert()