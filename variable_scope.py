# global variable
name = "mrkhun webdev"

def  sayMyName () :
    # local variable ( local can asset global | can't asset on global )
    global name
    newName = "mrKhunwin"
    print(f'It is local variable value: {newName}')

sayMyName()

print(f'It is  global value: {name}')
# print(newname) (local variable can't outside )