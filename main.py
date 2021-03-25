# /*
#  * @Author: Pasindu Akalpa 
#  * @Date: 2021-03-25 15:44:47 
#  * @Last Modified by: Pasindu Akalpa 
#  * @Last Modified time: 2021-03-25 15:44:47
#  * @Reference: AllTech(2018). console horizontal histogram in python 😀.Available at:https://www.youtube.com/watch?v=h_qlWgIvOZo (Accessed: 25 March 2021).
#  */

def histogram(list):
    for n in list:
        print(n, end=' ')
    print()

    while not all(n <= 0 for n in list):
        toPrint = ''
        
        for i in range(len(list)):
            if list[i] > 0:
                toPrint += '* '
                list[i] -= 1
            else:
                toPrint += '  '
        print(toPrint)

histogram([2, 3, 6, 5, 4, 8]) # parse your list here 