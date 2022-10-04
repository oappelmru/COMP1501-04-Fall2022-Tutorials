'''
Functions for even and odd.
Main programs calls functions.
Main program prompts user for value and produces output, accordingly.
'''

def iseven(num):
    ans = False
    if (num % 2) == 0:
        ans = True
    else:
        ans = False

    return(ans)


def isodd(num:int)->bool:
    ans = False
    if (num % 2) == 0:
        ans = False
    else:
        ans = True

    return(ans)

def otherodd(num):
    return (not(iseven(num)))


def main():
    entered_num = int(input("Enter a positive integer ==> "))
    if iseven(entered_num):
        print(f'The number {entered_num:,d} is EVEN.')
    else:
        #if otherodd(entered_num):
        if isodd(entered_num):
            print(f'The number {entered_num:,d} is ODD.')

    print("That's all folks!\n")

main()
