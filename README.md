# Dank-Memer-Grinder
<h6> <i> v1.0.3 </i> </h6>

### <h2 align="center"> <i> <b> A Python script which auto types commands to get ez money </b> </i> </h2>

<br>
<hr>
<br>

## Disclaimers
* Botting a user account is technically against Discord's ToS.
* The same thing applies to Dank Memer.

Quoted from [Dank Memer Rules](https://dankmemer.lol/rules):
```
RULE ONE - USERBOTS, SPAMMING, AND MACROS:
Userbotting, macros, scripts and anything else used to automate running commands is strictly forbidden.
On top of this, massive amounts of spam is not allowed and will be punished with the same severity.
```

### I very much doubt that they'll ban any of your accounts, but if they do, it's not my responsibility.
## Installing Dependencies 
1. Make sure you have Python 3 installed.
2. Run `python pip install -r requirements.txt` or `sudo python3 -m pip install --requirement requirements.txt` if you're on Linux.
## Running the script
1. Open the directory in your preferred terminal.
2. Open the Discord channel you want to type the commands in.
3. Run `python windowdetector.py` or `python3 windowdetector.py` if you're on Linux.
4. Copy the window name and paste it in the main script when it asks you to.
5. Run `python main.py` or `python3 main.py` if you're on Linux.
## Warning
* There is a bug in the Linux version in which the script doesn't detect window changes and will type the commands in any active window, So be careful.
## Required items in account inventory
* Hunting Rifle
* Fishing Pole
* Laptop

It is recommended to have at least 5 of each in case one breaks.

## Features
* Every single command is executed randomly (with random pauses between commands) to avoid getting banned (Except the "dep" command which is executed at the end of every loop)
* Fail-safe method, If you click away from the specified window, the script will automatically stop (currently only works on windows)

## Acknowledgments
* **Swayx113** gave me the idea to make this script so make sure to show him some love - [Github Profile](https://github.com/Swayx113).
* Current version (1.0.3) is only compatible with the [December 17th 2020 Update](https://discord.com/channels/470337009886429194/599044275291947016/788988188370796545) 
## To-Do List
- [ ] Add Comments
- [ ] Make a GUI
- [ ] Make an executable `.exe`
- [ ] Fix the Linux bug
