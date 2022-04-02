# IC1TProject

##Exploitable
securebank.c contains three vulnerabilities. First is string format. Attacker is able to read or modify variable (e.g. sys_pwd) by printing address of variable with %s or %n formatters.
For instance by passing $(python -c 'print "\xc2\xd8\xff\xff"+"%08x-"*3+"%s"') to argv[1] where hex symbols are address of target variable in little endian order, 3 is number of addresses
which stands between esp and controlled memory space, then due to %s target variable will be printed. Addresses can be read from gdb or any other debugger. Disabling ASLR is required.  

Second vulnerability is buffer overflow. Attacker doesn't have to exploit string format to break password. You can easily let buffer overflow to overwrite authorized variable and despite 
"Wrong password!" notification grant access to system.

After authorization user find out that he is indebted, but not for long, because of (probably) last vulnerability - integer overflow. You are able to pay a huge amount (the sum of the
debt and the paid amout must be greater than the integer lower bound). Now the user is dollar billionaire. 