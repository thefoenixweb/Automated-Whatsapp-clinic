Technologies Used:

Python: Language
Twilio: Virtual Number
MongoDB: Database
Whatsapp: Texting APP
Heroku: Hosting

Using Live Version:

Step 1:
Add Twilio number to your whatsapp contact list:
+1(415) 523-8886

Step 2:
Join Twilio Sandbox by texting "Join copy-silence" to Twilio contact

Step 3:
Proceed to communicate with bot.
Demo video linK:
https://youtu.be/T2KDWsZG3j8?si=-53A9caZIhN4sVyv

Demo video part 2:
If you say hello again or any other incorrect response.
https://youtu.be/7ugiNH8BhM4?si=ViLXuyHQFK99Wj5-


Running Local Version:

Step 1:
Install python IDE and the following dependancies:

flask
pymongo

Step 2:
Download app to local folder then run "python app.py" in directory using selected IDE

Step 3:
Open a seperate terminal and run the following code in that same directory: "nodemon --watch "app.py" --exec "lt --subdomain <subdomainname> --port 5000" --delay 2"
Note: name the subdomain whatever name you can come up with. The terminal will give you a url, copy it.

Optional:
Create your own MongoDB database and cluster and create your own users and orders databases. Then add your connection string to the app.py file.
![image](https://github.com/thefoenixweb/Automated-Whatsapp-clinic/assets/71729650/c28d4b42-da8b-4881-93ba-08be3196715c)

Note: Make sure to put your password in your link there will be a space for it like this: "<Password>"


Step 4: 
Create a Twilio account(its free), go to your console, on the left-panel, you will see a two headings: "Develop" and "Monitor", click on develop then you will see a tab that says "messaging", click on it and you will get a dropdown-list. 
Click on the option that says "Try it Out", then click on "Send a whatsapp message".

![image](https://github.com/thefoenixweb/Automated-Whatsapp-clinic/assets/71729650/cea968da-8d51-43da-ba58-794fc6cd767e)

You will see two titles: Sandbox and Sandox Settings, click on the settings.
You will see a space to paste a url in, above that space the header will say "When a message comes in". Paste your local subdomain url in that space.
Next to that space there is an option to choose between a GET method or a POST method, choose POST. 
Then click save below

![image](https://github.com/thefoenixweb/Automated-Whatsapp-clinic/assets/71729650/43040a91-fefe-43f6-8a97-9364e144ea64)

Step 5:

When you scroll down you will see your "Sandbox Participants" details, which is the Whatsapp number and joining code you will use to communicate with the bot. 

