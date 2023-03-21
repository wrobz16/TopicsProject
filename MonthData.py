#
#
#
#
#

import csv

# reads CSV and returns a list of lists per line
# input: file name
def readCSV(file):

    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

# writes the output to a .csv
def writeCSV(header, data, filename):

    # create filename
    #filename = filename[:-4] + "_Total"

    # Specify the filename to write to
    filename = r"DiseaseData\Outputs\\" + filename + "_Total"

    # Open the file in write mode and specify the delimiter as a comma
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(header)
        
        # Write each row of the list of lists to the CSV file
        for row in data:
            csvwriter.writerow(row)

# calculates the sum for each month and returns a list [month, total]
# input: list formatted like [month, weekTotal] i.e. [["January", 3], ["January", 4], ...]
def getMonthTotals(list):
    monthDict = {}

    for item in list:
        key = item[0]
        value = item[1]
        
        if key in monthDict:
            monthDict[key] += value 
        else:
            monthDict[key] = value

    return [[key, value] for key, value in monthDict.items()]


# estimates the number of infections per month per year and returns a list of lists formatted like [[Jan1999, Feb1999, ...], [Jan2000, Feb2000, ...], ...]
# input: total list (formatted: ['total', 12, 34, ...]), avg list (formatted: [.032, .045, ...]), years list (formatted: ['1999', '2000', ...])
def getMonthPerYear(total, avgs, years):
    tempTotal = []
    for i in range(1, len(total) - 1):
        tempYear = [years[i-1]]
        for avg in avgs:
            tempYear.append(total[i] * avg)
        tempTotal.append(tempYear)

    return tempTotal

# calculates the per month per year data
def calcStateData(yearData, avgs):

    StateList = []
    for i in range(1, len(yearData) - 1):
        
        yearList = []
        for j in range(1, len(yearData[i]) - 1):
            monthList = []
            for avg in avgs:
                yearList.append(int(yearData[i][j].replace(",","")) * avg)
        StateList.append(yearList)
        

    return StateList

# builds header
def buildHeader(months, years):

    header = []
    header.append('States')
    for i in range(len(years)):
        for j in range(len(months)):
            tempString = months[j] + ' ' + years[i]
            header.append(tempString)



    return header

def main():

    #file1 = r"WestNile\UnitedStatesData\WestNile_1999_to_2021.csv"
    disease = input("Please enter disease (No spaces and capitalize the first letter of each word (WestNile)): ")

    file1 = r"DiseaseData\Diseases\\" + disease + "\\" + disease +  ".csv"
    yearData = readCSV(file1)

    file2 = r"DiseaseData\Diseases\\" + disease + "\\" + disease + "_Months.csv"
    monthDataTotal = readCSV(file2)

    # state list
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
              'Colorado', 'Connecticut', 'Delaware', 'D.C.', 'Florida', 'Georgia', 
              'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
              'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
              'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
              'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
              'New York', 'North Carolina', 'North Dakota', 'Ohio', 
              'Oklahoma', 'Oregon', 'Pennsylvania','Puerto Rico', 'Rhode Island', 
              'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 
              'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 
              'Wisconsin', 'Wyoming']
    
    # months list
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

    

    # get years
    years = []
    for i in range(1, len(yearData[0]) - 1):
        years.append(yearData[0][i])

    # get month data in format [[Month, WeekTotal]]
    monthData = []
    for i in range(1, len(monthDataTotal)):
        monthData.append([monthDataTotal[i][0], int(monthDataTotal[i][2].replace(",",""))])
    
    # get total infections per month
    monthTotals = getMonthTotals(monthData)

    # get totals
    totalData = yearData[-1]

    # remove commas from totals
    for i in range(1, len(totalData)):
        totalData[i] = int(totalData[i].replace(",",""))

    # get per month avg
    monthAvgs = []
    for sublist in monthTotals:
        monthAvgs.append(sublist[1] / int(totalData[-1]))

    # get esimated month reports per year
    monthYearTotals = getMonthPerYear(totalData, monthAvgs, years)

    # calculate state data
    rawStateData = calcStateData(yearData, monthAvgs)

    # add states
    for i in range(len(rawStateData)):
        rawStateData[i].insert(0, states[i])
    
    # build header
    header = buildHeader(months, years)

    # write to a csv
    writeCSV(header, rawStateData, disease)

main()