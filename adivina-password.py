MY_PASSWORD = 'python3'

def password():
    current_password = hash(MY_PASSWORD)
    
    intentos=1
    while intentos <=3:
        pass_attemp = input("Write Password: ")

        if hash(pass_attemp) == current_password:
            result = "Password is valid"
            
            return result
            
        elif intentos < 3:
            result = f"Only have left {intentos}"
            intentos += 1
            print(result)
            
        else:
            result = "Password is invalid"
            
            return result

if __name__=='__main__':
    
    print(password())