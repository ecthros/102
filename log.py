#!/usr/bin/python
import json
import gspread
import argparse
import os
from oauth2client.client import SignedJwtAssertionCredentials

# Finds the first empty row of the worksheet.
def find_next_row(worksheet):
    val_list = worksheet.col_values(1)
    row_num = 1
    for row in val_list:
        if row == '':
            return row_num
        row_num += 1
    return None

#Authenticates the user to be able to use the sheet
def authenticate(key):
	json_key = json.load(open(key))
	scope = ['https://spreadsheets.google.com/feeds']
	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
	gc = gspread.authorize(credentials)
	return gc

def main():
	sheet = ""

	#parse arguments

	parser = argparse.ArgumentParser(prog="log")
	parser.add_argument("-k", "--key", required=True, help="The json key file needed for authentication")
	parser.add_argument("-s", "--sheet", required=True, help="The URL of the google sheet")
	parser.add_argument("-d", "--data", required=True, help="Data to update the sheet with, separated by commas")
	parser.add_argument("-w", "--worksheet", help="Worksheet name - only if you are using a sheet that isn't the first sheet")
	parser.add_argument("-D", "--delimiter", help="Delimiter if you want to use something other than commas")

	args = parser.parse_args()
	
	#just in case...

	file = open("/logging/log.txt", "a+")
	file.write(args.data)
	file.write("\n")
	file.close()

	try:

		auth = authenticate(str(args.key))
		spread = auth.open_by_url(str(args.sheet))
		
		if(args.worksheet == None):
			wks = spread.sheet1
		else:
			wks = spread.worksheet(str(args.worksheet))
		
		startCol = 'A'
		startRow = str(find_next_row(wks))

		if(args.delimiter == None):
			for segment in args.data.split(','):
				wks.update_acell(str(startCol) + startRow, segment)
				startCol = chr(ord(startCol) + 1)
		else:
			for segment in args.data.split(args.delimiter):
				wks.update_acell(str(startCol) + startRow, segment)
				startCol = chr(ord(startCol) + 1)
		
		print("Successfully updated!")
	#ICOF
	except Exception as e:
		print("Error:")
		print(e.message)

main()