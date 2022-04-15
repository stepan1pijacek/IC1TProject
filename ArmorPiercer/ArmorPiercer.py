import click
from ArmorPiercer import AutomatedPenTest as AtP


@click.command()
@click.option('--help', '-h')
def main():
    """Application for penetration testing of the SecureBank"""
    pass


@click.command()
@click.option('--help', '-help')
def help_command():
    click.echo('ArmorPiercer version 0.0.0.1 \n'
               'ArmorPiercer supports two possible methods of penetration testing:   \n'
               '---------------------------------------------------------------------\n'
               '    * Automated: --auto| -a \n'
               '    * Manual: you can manually trigger any of the three exploits \n'
               '        ** StringFormat:    --StrForm  | -sf \n'
               '        ** BufferOverflow:  --BufOver  | -bf \n'
               '        ** IntegerOverflow: --IntOver  | -if \n'
               '---------------------------------------------------------------------\n')


@click.command()
@click.option('--auto', '-a', help='Automated penetration test')
@click.option('--process-path', '-i',
            required=False, help="Path to the process under the attack")
def automated(process_path):
    print('Fuck you')
    test = AtP.AutomatedPenTest("~/IC1TProject/SecureBank/build/output 'bob'")
    test.begin_pen_test()

