def print_even(num): #function definition
    if num<= 100:   #condition
        if num%2==0: #check even
            print(num)#recursive call
        print_even(num+1)
print_even(1)
        
