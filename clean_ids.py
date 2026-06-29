import sys
import re
import logging

logging.basicConfig(
	filename="pipeline_audit.log",
	level=logging.WARNING, #sets the minimal level of severity to get logged
	format="%(asctime)s - %(message)s") #formats the message with a time stamp and the message

pattern_ids = re.compile(r'^[A-Za-z0-9_-]{11}$') # compiling the pattern outside of the loop


def main():
	for line in sys.stdin:
		line = line.strip()
		if not line: # if theres a empty space for some reason
			continue
		if pattern_ids.match(line):
			sys.stdout.write(line + "\n")
			sys.stdout.flush() #sends out the ids as they are processed, doesn't hold anything in memory
		else:
			logging.error(f"Invalid YouTube ID: '{line}'")

if __name__ == "__main__":
    main()

