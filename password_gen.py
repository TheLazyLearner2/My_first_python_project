import random
import string

def password(passwd_length=int):
    print('WELCOME TO PASSWORD GENERATOR.')
    print('Password must be between 8 and 20 characteres long.\n')
    
    letters = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation
    
    all_symbols = letters + numbers + special_char
    

    while range(passwd_length):
        if passwd_length >= 8 and passwd_length <= 20:
            generated_password = random.sample(all_symbols, passwd_length)
            comb_password = "".join(generated_password)
            print('Your Password is', comb_password)
            return comb_password
        else:
            print('Password length cannot be less than 8 characters or more than 20 characters. Please try again')
            return None
        
    
def store_used_password(password):
    file = password + '\n'
    with open("used_passwords.txt", "a") as f:
        for i in file:
            f.write(i)
                      
                     
new_password = password(10)
store_used_password(new_password)










    
    
    
        
