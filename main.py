#!/usr/bin/env python3

import subprocess
import sys
import argparse

sys.argv[0] # name of script

subprocess.run(["ls", "-al"])

parse = argparse.ArgumentParser(description="Tool")
parse.add_argument("-a", "--all", action="store", help="Tell me")
args = parse.parse_args()

print(f"You gave me {args.all}")

# grab target and targzip it

