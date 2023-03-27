import argparse
import sys
from termcolor import colored

class ColoredArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (colored(self.prog, "red"), colored(message, "red")))
