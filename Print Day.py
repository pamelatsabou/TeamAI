"""written in pycharm
written on 10/03/22
by @BertinAm

"""

def numb(days):
    if days == 0:
        print("Sunday")
    elif days == 1:
        print("Monday")
    elif days == 2:
        print("Tuesday")
    elif days == 3:
        print("Wednesday")
    elif days == 4:
        print("Thursday")
    elif days == 5:
        print("Friday")
    elif days == 6:
        print("Saturday")
    else:
        print("please enter the indicated numbers\n")
    return "Happy weekdays"


print(numb(int(input("Enter a number \n"))))
