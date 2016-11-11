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
    auto.click(x=540, y=594)  # coordinates of simulate location button
    time.sleep(1)
    auto.click(x=675, y=647)  # coordinates of .gpx file selection
    time.sleep(1)
    auto.click(x=1191, y=389)  # coordinates of terminal window


def main():
    lastLat = input("Enter the Lat: ")
    lastLat = float(lastLat)  # starting latitude
    lastLng = input("Enter the Lng: ")
    lastLng = float(lastLng)  # starting longitude
    generateXML(lastLat, lastLng)
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    stdscr.refresh()

    key = ''
    speed = 0.0002  # increment value for directions
    while key != ord('q'):
        key = stdscr.getch()
        if key == curses.KEY_UP:
            lastLat += speed
        elif key == curses.KEY_DOWN:
            lastLat -= speed
        elif key == curses.KEY_LEFT:
            lastLng -= speed
        elif key == curses.KEY_RIGHT:
            lastLng += speed
        generateXML(lastLat, lastLng)
        clickAction()

    curses.endwin()
    sys.exit()


main()
