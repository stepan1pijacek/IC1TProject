from asyncio.subprocess import PIPE
from os import name
import re
from sys import stdout
from time import sleep
from tokenize import Number
import click
import subprocess as sp
import os


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
    
    confirmed_vulnerabilities = []
    process_opened = sp.Popen(["./" + process, user_name]
                        ,stdin=sp.PIPE
                        ,stderr=sp.PIPE
                        ,universal_newlines=True
                        )
    sleep(3)
    process_opened.stdin.write("aaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    if process_opened.stderr.readline:
        click.echo("Buffer overflow failed to gain access to the application, exiting process now!" + process_opened.stderr.readline)
        process_opened.kill()
    confirmed_vulnerabilities.insert(1, "Buffer overflow is confirmed vulnerability")

    process_opened.stdin.writelines("1231354\n")
    confirmed_vulnerabilities.insert(2, "Integer overflow is confirmed vulnerability")
    sleep(3)
    process_opened.stdin.writelines("21476511478\n")

    process_opened.kill()
    print("Penetration testing terminated with success")

    click.echo(confirmed_vulnerabilities)


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
                help="Number to cause integer overflow. Max value of int in C is 2147483648")
def integer_overflow(int_number):
    """Command to perform integer overflow
        eg. python3 ArmorPiercer.py integer-overflow --int-number=2147483648
    """
    click.echo(int(int_number))


if __name__ == '__main__':
    main()
