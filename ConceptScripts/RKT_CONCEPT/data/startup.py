fileIn = open("./climateData.txt", "r")
print (fileIn)

fileOut = open("datafile.txt", "w")
fileOut.write("HelloWorld!!!")

fileOut.close()

fileIn.close()

