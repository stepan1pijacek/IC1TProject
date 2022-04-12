import re
import subprocess as sp


class CreateProcess:
    def __init__(self, program_path):
        self.program_path = program_path
        self.process = sp.Popen([self.program_path], stdout=sp.PIPE, stdin=sp.PIPE)

    def start_process(self):
        current_console_out = self.process.stdout.readline()

        if not re.match("password|login", current_console_out.decode("utf-8")):
            return "Failed, application did not start"

        return self.process

    def kill_process(self):
        self.process.kill()
        return "Process killed successfully"

