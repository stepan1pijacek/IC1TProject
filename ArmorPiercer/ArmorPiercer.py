import click


@click.group()
def main():
    """Application for penetration testing of the SecureBank"""
    pass


@main.command()
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


@main.command()
@click.option('--auto', '-a')
def automated():
    

if __name__ == '__main__':
    main()
