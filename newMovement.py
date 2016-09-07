#!/usr/bin/python
# -*- coding: utf-8 -*-
import curses
import xml.etree.cElementTree as ET
import time
import sys
import pyautogui as auto


def generateXML(lastLat, lastLng):
    gpx = ET.Element('gpx', version='1.1', creator='Xcode')
    wpt = ET.SubElement(gpx, 'wpt', lat=str(lastLat), lon=str(lastLng))
    ET.SubElement(wpt, 'name').text = 'PokemonLocation'
    ET.ElementTree(gpx).write('pokemonLocation.gpx')


def clickAction():
    auto.click(x=480, y=257)  # coordinates of simulate location button
    time.sleep(1)
    auto.click(x=480, y=650)  # coordinates of .gpx file selection
    time.sleep(1)
    auto.click(x=1000, y=490)  # coordinates of terminal window


def main():
    lastLat = 36.152847
    lastLng = -86.795847
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    stdscr.addstr(0, 10, "Hit 'q' to quit")

    stdscr.refresh()

    key = ''
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.addch(20, 25, key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            lastLat += 0.0002
        elif key == curses.KEY_DOWN:
            lastLat -= 0.0002
        elif key == curses.KEY_LEFT:
            lastLng -= 0.0002
        elif key == curses.KEY_RIGHT:
            lastLng += 0.0002
        generateXML(lastLat, lastLng)
        clickAction()

    curses.endwin()
    sys.exit()


main()
