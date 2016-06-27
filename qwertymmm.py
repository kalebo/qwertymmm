#!/usr/bin/env python
import sys
from pyfiglet import Figlet
import curses
import random

FONT = Figlet(font="big")
KEYBOARD = r"""',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz[]"""

def main(stdscr):
    try:
        my, mx = stdscr.getmaxyx()

        curses.curs_set(0)

        curr  = random.choice(KEYBOARD)
        while True:
            stdscr.clear()
            stdscr.box()
            fig = FONT.renderText(curr.upper()).splitlines()
            for y, line in enumerate(fig):
                stdscr.addstr(my/2 - len(fig)/2 + y, mx/2 - len(line)/2, line)
            if chr(stdscr.getch()) == curr:
                curr  = random.choice(KEYBOARD)
            stdscr.refresh()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    curses.wrapper(main)

