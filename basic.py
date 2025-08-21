x=10
printer="HP"
print("I just printed {0} pages from the printer {1}".format(x,printer))
print("I just printed {x} pages from the printer {printer}".format(x=11,printer="Epson"))
print(f"I just printed {x} pages from the printer{printer}")

 #using format option for a
#value stored in a variable
str="This article is written in {}"
print(str.format("python"))

#using format option in a simple string

print("{},A Computer Science Engineering in.".format("Faculty of Engineering & Technology"))

#formatting a string using a numeric constant

print("Hello, I am {} years old !".format(18))

#python program using multiple place
#holders to demostrate str format()method
#different datatypes can be used in formatting

print("Hi! My name is {} and I am {} years old".format("user",19))

#The values passed as parameters are replaced in order  of their entry.
print("This is {} {} {} {}".format ("one","two","three","four"))

#To demostrate the use of fomatters
#with positional key arguments.
print("{0} love {1} !!".format("fetians","FET"))
#Reverse the Index numbers with the parameters of the placeholders.
print("{1} love {0} !!".format("fetians","FET"))
print("Every {} should know the use of {} {} programming and {} ".format("programmer","open","source","operating system"))
print("{gfg}is a {0} science portal for {1}".format ("computer","geeks",gfg="GeeksforGeeks"))


