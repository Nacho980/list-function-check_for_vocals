"""
function to confirm a vocal has been typed
"""
#function to do the logic and confirm vocal or something else
def vocal(letter):
    #define list of vocals
    vocals=['a','e','i','o','u']
    #checking process using 'if'
    if letter in vocals:
        return  True
    else:
        return False
    #asking for a vocal from keyboard
x = input("Type a vocal ")
#calling to function to do the logic with the paremeter from the line just above
print(vocal(x))
