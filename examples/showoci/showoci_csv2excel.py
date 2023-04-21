############################################
# @author: Adi Zohar
#
# Supports Python 3 and above
#
# coding: utf-8
############################################
# Required: Pandas, openpyxl
# Install:
# python3 -m pip install pandas openpyxl
############################################
import glob
import sys
import pandas as pd

# Get the parameter of the folder
if sys.argv is None or len(sys.argv) < 2:
    print("Please specify the csv location including initial name")
    sys.exit()

csv_location = sys.argv[1]

print("ShowOCI CSV to Excel, CSV = " + csv_location + " ...")

# Get file list
file_list = []
for file in glob.glob(csv_location + "*.csv"):
    file_list.append(file)

excel_name = csv_location + '.xlsx'

# convert to excel
writer = pd.ExcelWriter(excel_name)

for file in sorted(file_list):
    df = pd.read_csv(file)
    sheet_name = file[len(csv_location) + 1:-4]
    print('   Handling ' + sheet_name + " ...")
    df.to_excel(writer, sheet_name=sheet_name)

writer.close()
print("Completed, Excel = " + excel_name)
