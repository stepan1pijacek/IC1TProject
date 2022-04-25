# IC1TProject
## Exploiter

ArmorPiercer.py is PYTHON script intended to pen test *securebank.c* application. ArmorPiercer is inteded to be used as CLI application.
### Table of commands for the application
| Command name | Command | Command options | output |
| ------------ | ------- | --------------- | ------ |
| Version      | --version | NaN           | Current version of the app |
| Help         | --help  | NaN             | Returns list of available commands |
| Buffer overflow | buffer-overflow | --count [INT] | Uppon providing *count* option it prints given number of the *a*'s to the console |
| Integer overflow | integer-overflow | --int-number [INT] | Prints given number in to the console |
| Automated attack | automated-attack | Multiple options, see table below | Performs automated attack on the given process using python sub process |

#### Table of automated attack options
| option | input type | help output |
| ------ | ---------- | ----------- |
| --process | STR | Process to be attacked |
| --user-name | STR | User name of the SecureBank user |
| --bank-account | INT | Bank account for attacka purposes |

~~test~~

## Exploitable

securebank.c contains three vulnerabilities. First is string format. Attacker is able to read or modify variable (e.g. sys_pwd) by printing address of variable with %s or %n formatters.
For instance by passing $(python -c 'print "\xc2\xd8\xff\xff"+"%08x-"*3+"%s"') to argv[1] where hex symbols are address of target variable in little endian order, 3 is number of addresses
which stands between esp and controlled memory space, then due to %s target variable will be printed. Addresses can be read from gdb or any other debugger. Disabling ASLR is required.  

Second vulnerability is buffer overflow. Attacker doesn't have to exploit string format to break password. You can easily let buffer overflow to overwrite authorized variable and despite 
"Wrong password!" notification grant access to system.

After authorization user find out that he is indebted, but not for long, because of (probably) last vulnerability - integer overflow. You are able to pay a huge amount (the sum of the
debt and the paid amout must be greater than the integer lower bound). Now the user is dollar billionaire. 
