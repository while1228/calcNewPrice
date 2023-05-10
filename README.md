# calcNewPrice

##this script is calclate newPrice and write it to a new file.


---
Have a TXT file with data. This is how python script is set up

Coin.txt
Name, Buy , 4.58,* 10

name = input_data[0]
contract = float(input_data[2])
math = float(input_data[3])

newprice = contract * math

ERROR: math = float(input_data[3])
ValueError: could not convert string to float: '* 10 \n'