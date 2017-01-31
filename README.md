This guide details how to set up logging from your host to Google Drive.

Begin by downloading the repository: 

	git clone https://github.com/ecthros/102

Now that you've downloaded the code, install the necessary dependencies:

	sudo ./setup.sh

Next, you need to create OAuth Credentials so that you can access your Google Sheet. Follow the directions here: http://gspread.readthedocs.io/en/latest/oauth2.html. Stop before step 5 - I've already done the rest for you with the setup script.

Now that you've downloaded the JSON file, you need to move the file to your host. There are a number of ways to do this - either using scp or uploading the file to dropbox and using wget.

You're almost there! Open the JSON file up, and you'll see an email associated with the "client_email" field. Copy it and share your Google Sheet with that email.

To run the script, use:

	log -k <yourJSONfile> -s <sheetid> -d <data>

The JSON file should be the absolute path to the file, like:
	/root/stuff/hacs.json

And your sheetid is the long string in the URL of the Google Sheet. If your URL is

https://docs.google.com/spreadsheets/d/1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM/edit#gid=1199366553

then your sheetid is: 1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM
