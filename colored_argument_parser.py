"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

import argparse
import sys
from termcolor import colored

class ColoredArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (colored(self.prog, "red"), colored(message, "red")))
