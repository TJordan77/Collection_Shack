#Fibonacci Generator With Input

#User can determine the first x numbers of the fibonacci sequence
user = int(input("How many iterations you want?: "))

#Below is just a little something for fun, feel free to remove vvvvvvvv
if user <= 0:
    print("No, stop your bs. Put in a real number: ")
    user = int(input("How many iterations you want?: "))
    if user <= 0:
        print("What did I just say?")
        user = int(input("Put in a real number: "))
        if user <= 0:
            print("No, no, I'm done. Goodbye.")
#Trying to find an easier way to loop it back to the main program after denying 0 | negative numbers.
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Generator (SoloLearn teaches us how to make one)
def fibonacci(num):
    a,b = 0,1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        #Just like in calculus,
        # the equation on one side equals the equation on the other side of the equal sign
        a,b = b, a+b

#Calls the integer the user inputted and determines the stop point
for user in fibonacci(user):
    print(user)
