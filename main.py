# This is a sample Python script.
# newPrice = contranct * math
# this script calc newPrice ,apped newPrice to that row and write a new file
import csv

dataFIlePath = "./sample_coin.txt"
outFilePath = "./sample_coin_out.txt"
def parse_data(readFilePath, outFilePath):
    with open(readFilePath) as fd:
        with open(outFilePath,'w+',newline='') as outFd:
            csvWrite = csv.writer(outFd)
            csvRows = csv.reader(fd)
            for row in csvRows:
                contract = float(row[2])
                math = float(row[3].replace("*",""))
                newPrice = contract * math
                row.append(newPrice)
                csvWrite.writerow(row)
                print(row)

parse_data(dataFIlePath, outFilePath)
