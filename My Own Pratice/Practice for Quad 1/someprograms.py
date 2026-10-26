#WAP to take 5 marks from user and check the percentage and assign the grade then show both whre each subject total marks is 100
"""
grade system
marks above 90 -> A+
between 80 - 90 -> A
between 70 - 80 -> B
between 60 - 70 -> C
below 60 -> Needs improvements
"""
def program1_easy():
    marks1 = int(input("Enter your subject 1 marks : "))
    marks2 = int(input("Enter your subject 2 marks : "))
    marks3 = int(input("Enter your subject 3 marks : "))
    marks4 = int(input("Enter your subject 4 marks : "))
    marks5 = int(input("Enter your subject 5 marks : "))
    #first easy percentage calculation
    # totalMarksObtained = marks1 + marks2 + marks3 + marks4 + marks5
    # percentage = (totalMarksObtained / 500) * 100
    #best method for percentage calculation
    percentage = ((marks1 + marks2 + marks3 + marks4 + marks5) / 500) * 100

    if percentage >= 90 :
        grade = 'A+'
    elif percentage >= 80 and percentage < 90 :
        grade = "A"
    elif percentage >= 70 and percentage < 80 :
        grade = "B"
    elif percentage >= 60 and percentage < 70 :
        grade = "C"
    elif  percentage < 60 :
        grade = "Needs improvements"
    else :
        grade = "Something wrong happened"
    print(f"Student percentage {percentage:.2f}% \nGrade = {grade}")

def program1_efficient():
    marks = []
    totalMarksObtained = 0
    for i in range(1,6): # 0 - 4
        x = int(input(f"Enter your subject {i}/. marks : "))
        marks.append(x)
        totalMarksObtained += x 
    percentage = (totalMarksObtained/500) * 100
    if percentage >= 90 :
        grade = 'A+'
    elif percentage >= 80 and percentage < 90 :
        grade = "A"
    elif percentage >= 70 and percentage < 80 :
        grade = "B"
    elif percentage >= 60 and percentage < 70 :
        grade = "C"
    elif  percentage < 60 :
        grade = "Needs improvements"
    else :
        grade = "Something wrong happened"
    print(f"Student percentage {percentage:.2f}% \nGrade = {grade}")
    
# program1_easy()
# program1_efficient()


"""
💻 Python Assignment: Retail Business Performance Calculator
Problem Statement
You are asked to write a Python program for a local retail store to calculate its financial performance for the month. The program should take the financial data as input and calculate Gross Sales, Net Sales, Total Cost, and Net Profit or Loss.
Formula Reference Guide
• Gross Sales = Total Quantity Sold x Selling Price Per Unit
• Net Sales = Gross Sales - Cost of Sales Returns (Refunds)
• Total Cost = Cost of Goods Sold (COGS) + Operating Expenses (Rent, Salaries, Utilities)
• Net Profit / Loss = Net Sales - Total Cost
📝 The Question for Students
Write a Python program that does the following:
1. Defines a function calculate_finances() to handle the logic.
2. Prompts the user to input:
	• Product Name
	• Quantity Sold
	• Selling Price per unit
	• Sales Returns (Total amount refunded to customers)
	• Cost of Goods Sold (COGS)
	• Operating Expenses
3. Calculates and displays a formatted summary of Gross Sales, Net Sales, Total Cost, and whether the business made a Profit or a Loss (along with the exact amount).
"""

def calculate_finances():
    ProductName = input("Enter the Product Name : ")
    QuantitySold = int(input("Enter how many Quantity Sold : "))
    SellingPricePU = float(input("Enter your selling price per unit : "))
    SalesReturn = int(input("Enter how many units has returned : "))
    COGS = float(input("Enter your cost of good sold (Total): "))
    COGS_PU = COGS/float(QuantitySold)
    OE = float(input("Enter your operating expences : "))
    grossSales = QuantitySold * SellingPricePU
    NetSales = grossSales - SalesReturn*COGS_PU
    TotalCost = COGS + OE
    Profit_Loss = NetSales - TotalCost
    PL = ""
    if Profit_Loss > 0 :
        PL = "Profit"
    elif Profit_Loss <0:
        PL = "Loss"
    else :
        PL = "Break Even Point"
    output = {
        "Product name" : ProductName,
        "Gross Sales" : grossSales,
        "Net Sales" : NetSales,
        "Total Cost" : TotalCost,
        "PL":PL,
        "Profit_Loss":Profit_Loss
    }
    return output
#     output = f"""
#  | Product name : {ProductName} |
# --------------------------------------
# Gross Sales : {grossSales}
# Net Sales : {NetSales}
# Total Cost : {TotalCost}
# The company makes the {PL} of amount {Profit_Loss}
# --------------------------------------
#             """

output = calculate_finances()
print(output)
print(
    f"""
 | Product name : {output["Product name"]} | 
----------------------------------------------
Gross Sales : {output["Gross Sales"]}
Net Sales : {output["Net Sales"]}
Total Cost : {output["Total Cost"]}
The company makes the {output["PL"]} of amount {output["Profit_Loss"]}
"""
)























def newFile(text):
    output = calculate_finances()
    path = "E:\\Programming Codes\\Anika-Python\\Python-Programming\\My Own Pratice\\Practice for Quad 1\\output.txt"
    with open(path,"w") as f:
        f.write(f"{output} \n {text}")
        print("File created succfully path = ' ",path,"' ")
    # f.close()

def readFile():
    try:
        path = "E:\\Programming Codes\\Anika-Python\\Python-Programming\\My Own Pratice\\Practice for Quad 1\\output.txt"
        file = open(path,"r")
        file.read()
    except Exception as e:
        print(e)
    return str(file)

def mergeFiles():
    oldText = readFile()
    print("Old text recovered...")
    newText = newFile(oldText)
    print("New text received...")
    print("Merged result...")

# try:
#     mergeFiles()
# except Exception as e:
#     print(e)









