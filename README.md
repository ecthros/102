This guide details how to set up logging from your host to Google Drive.

	Note: Commands in this format should be run in the terminal on your OpenVZ Host.

Begin by downloading the repository: 

	sudo apt-get install git
	git clone https://github.com/ecthros/102

Now that you've downloaded the code, install the necessary dependencies:

	sudo ./setup.sh
	cd 102

Head to <a href=https://console.developers.google.com/project>Google Developers Console</a> and create a new project. 
Under “API & auth”, in the API enable “Drive API”.
Enabled APIs
Go to “Credentials” and choose “New Credentials > Service Account Key”.
Google Developers Console
You will automatically download a JSON file with this data.

Download Credentials JSON from Developers Console
This is how this file may look like:

{
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473 … hd@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    "type": "service_account"
}
You’ll need client_email and private_key.

Next, you need to create OAuth Credentials so that you can access your Google Sheet. Follow the directions <a href=http://gspread.readthedocs.io/en/latest/oauth2.html>here</a>: . You'll need to "create a new project" - Just name it anything (I named mine "Hacs 102 Group 2K). Stop before step 5 - I've already done the rest for you with the setup script.

Now that you've downloaded the JSON file, you need to move the file to your host. There are a number of ways to do this - either using scp or uploading the file to dropbox and using wget.

You're almost there! Open the JSON file up, and you'll see an email associated with the "client_email" field. Copy it and share your Google Sheet with that email.

To run the script, use:

	log -k <yourJSONfile> -s <sheetid> -d <data>

The JSON file should be the absolute path to the file, like:
	/root/stuff/hacs.json

And your sheetid is the long string in the URL of the Google Sheet. If your URL is

https://docs.google.com/spreadsheets/d/1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM/edit#gid=1199366553

then your sheetid is: 1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM
