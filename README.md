This guide details how to set up logging from your host to Google Drive. Your group has to do this so that we can periodically grade your logs. It may take up to 15 minutes to complete (sorry).

	Note: Commands in this format should be run in the terminal on your OpenVZ Host.

Begin by downloading the repository: 

	sudo apt-get install git
	git clone https://github.com/ecthros/102

Now that you've downloaded the code, install the necessary dependencies:

	cd 102
	sudo ./setup.sh

Head to the <a href=https://console.developers.google.com/apis/api/drive/overview>Google Developers Console</a>. Click on "Create Project" in the top right corner. Then select "Create a Project". Name the project anything (I named mine "Hacs 102 Group 2K).

![image](https://cloud.githubusercontent.com/assets/14065974/22453687/95824976-e74e-11e6-87fe-7fd09ae55345.png)

Agree to the terms and press "Create". Wait for it to load, and then next to "Google Drive API", make sure to click "Enable":

![image](https://cloud.githubusercontent.com/assets/14065974/22453698/b5fe0e42-e74e-11e6-862f-cda06bc661e2.png)

Click on one of the tabs on the left labeled "Credentials". Choose “New Credentials > Service Account Key”.

![image](https://cloud.githubusercontent.com/assets/14065974/22453376/7b2b506a-e74c-11e6-95a6-33cb8318966d.png)

Select "Compute Engine Default service account" and click "Create". A .json file will be downloaded.

![image](https://cloud.githubusercontent.com/assets/14065974/22453807/95c3e81c-e74f-11e6-80af-0376334e2e80.png)

Now that you've downloaded the .json file, you need to move the file to your host. There are a number of ways to do this - either using scp or uploading the file to dropbox and using wget. If you have port forwarding enabled, you could also copy and paste. You will need the location of this file for later.

You're almost there! Open the .json file, and you'll see an email associated with the "client_email" field. Copy it and share ALL your google sheets (or just your folder) with that email.

![image](https://cloud.githubusercontent.com/assets/14065974/22453754/0ec0ccb8-e74f-11e6-8b5f-f841df75119d.png)


To run the script, use:

	log -k <yourJSONfile> -s <sheetid> -d <data>

Where you need to replace the things inside the angle brackets (and the angle brackets themselves!) with the following data:

1. The JSON file should be the absolute path to the file, like:
	/root/stuff/hacs.json

2. And your sheetid is the URL of the Google Sheet. If your URL is

3. data is comma-separated values for your data, for example, "Toby,George,Matt,Louis-Henri". If I wanted to update the sheet with all the TAs' names, I would use the following command:

	log -k /root/stuff/hacs.json -s 1tlssiBoaiolsFMpvJFaC9JCFA7tfrYu30rIU4TVvNcM -d "Toby,George,Matt,Louis-Henri"


You've finished!! Now you need to figure out how often you want to run the logging command and which logs you want to update.

If you want, feel free to play around with the -w and -d options. For help, type:
	log --help