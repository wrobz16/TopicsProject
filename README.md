# TopicsProject

### MonthData.py  
Takes in two files (All state data and total per month data) and estimates the average reports
per state per month.

**Necessary Packages**  
    - csv

To install, run `pip install csv` in cmd if not installed already

**Running**  
To run, go to the *TopicsProject* directory and use the command:

`python3 MonthData.py <DiseaseName>`

where `DiseaseName` is the name of the desired disease and is formatted *FirstwordSecondword* and so on.

Example for West Nile: `python3 MonthData.py WestNile`

**Output**  
The output is located in *DiseaseData\Outputs*  