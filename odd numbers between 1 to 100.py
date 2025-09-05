def print_odd(num): #function definition
    if num<= 100:   #condition
        if num%2!=0: #check odd
            print(num)#recursive call
        print_odd(num+1)
print_odd(1)
        
