This Alexa skill allows you to ask "Alexa, who is in the house?", and she will tell you.

OK, so this repo is for my own development purposes only.
But some of the code might be useful for anyone who wants Alexa to read out a string from Thingspeak.

The basic operation is as follows:

ESP-01 wifi board is configured to connect to my network, but with a SoftAP
The SoftAP records all MAC addresses of all devices that attempt a connection
It then compares the MAC addresses with a list of 'known' devices ('friends').

Every two minutes, it uploads a string containing those friends into a Thingspeak database.

This code resides on Heroku.
Every time you ask Alexa "Who is in the house", the skill connects to Heroku to run this python code.

I have not hosted the ESP code here.

Steve