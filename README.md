This guide details how to set up logging from your host to Google Drive.

	Note: Commands in this format should be run in the terminal on your OpenVZ Host.

Begin by downloading the repository: 

	sudo apt-get install git
	git clone https://github.com/ecthros/102

Now that you've downloaded the code, install the necessary dependencies:

	sudo ./setup.sh
	cd 102

Head to <a href=https://console.developers.google.com/apis/api/drive/overview>Google Developers Console</a>. Click on "Create Project" in the top right corner. Then select "Create a Project". Name the project anything (I named mine "Hacs 102 Group 2K). Agree to the terms and press "Create". Wait for it to load, and then next to "Google Drive API", make sure to click "Enable":

![image](https://cloud.githubusercontent.com/assets/14065974/22453363/4bd47b48-e74c-11e6-9d71-8c6c596d5561.png)

Click on one of the tabs on the left labeled "Credentials". Choose “New Credentials > Service Account Key”.

![image](https://cloud.githubusercontent.com/assets/14065974/22453376/7b2b506a-e74c-11e6-95a6-33cb8318966d.png)

Select "Compute Engine Default service account" and click "Create". A .json file will be downloaded.

Now that you've downloaded the .json file, you need to move the file to your host. There are a number of ways to do this - either using scp or uploading the file to dropbox and using wget.

You're almost there! Open the .json, and you'll see an email associated with the "client_email" field. Copy it and share your Google Sheet with that email.

To run the script, use:

	log -k <yourJSONfile> -s <sheetid> -d <data>

The JSON file should be the absolute path to the file, like:
	/root/stuff/hacs.json

And your sheetid is the long string in the URL of the Google Sheet. If your URL is

https://docs.google.com/spreadsheets/d/1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM/edit#gid=1199366553

then your sheetid is: 1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM
