# def greet(greeting="Hello", name=""):
#     print(f"{greeting} {name}! How are you doing")
    
    
def greet(greeting="Hello", name=""):
    print(f"{greeting} {name}! How are you doing")



d = {
    "greeting": "Salam",
    "name": "Shahzaib"
}
# greet(greeting="Salam", name="Shahzaib")
greet(**d)