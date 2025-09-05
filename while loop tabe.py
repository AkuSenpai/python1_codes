table_num=int(input("Enter the table number:"))
num_times=int(input("Enter the value of start:"))
nums_runs=int(input("Enter the number of runs:"))
while(num_times<=nums_runs):
    result=num_times*table_num
    print( table_num,"x",num_times,"=",result)
    num_times=num_times+1
