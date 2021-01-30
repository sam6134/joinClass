## Join Class using Terminal through Zoom Client

It is a simple Python script that you can run on your UNIX systems which automatically redirects you to the class as specified in the Time-Table Schedule.

*PS-A Much Better Alternative than DC's Rust Script*

## Features

The folder contains two scripts-
### startClass
This allows one to join the class just by typing the command on the terminal. It will look up the class code based on your time-table and redirect you to the zoom-link.

### nextClass
This command gives the list of the upcoming classes in of the day, so that you could get free-up of checking the time-table again and again.


## Instructions for modifying Time-Table

New time-table slots can be added based on your schedule, but you have timings based on your convenience. 
Here, I have made 10 min changes so that classes could be joined prior to the class timings. Eg 9:20 slot -> 9:10.
So make sure to update the desired changes as per your convenience.

*Note-You will only be able to join the class during the timings specified in the time-table so make sure to give prior timings if you need to join class early*

## Instructions of setting up the Scripts

Firstly you need to configure the python interpreter path which can be done by running command, depending on your python version (3 or 2).
```
which python3
which python 
```
Modify this path at the top of the files startClass.py and nextClass.py i.e
#!/usr/bin/python3 to #!{Your Path}. \
Next give permissions to the script by running the following commands in the code directory.
```
chmod +x startClass.py
chmod +x nextClass.py
```
Next delete the .py extensions from both startClass, nextClass python files.
To add the scripts to the global path open ~/.bashrc or ~/.zshrc depending on your terminal and add the following lines-

export PYTHON_UTILS="$HOME/joinClass"
export PATH="$PYTHON_UTILS:$PATH"

Now you can easily run the commands just by typing in your terminal
```
startClass
nextClass
```

