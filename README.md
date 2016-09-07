# PokemonGOController
Manually control your PokemonGO character (Liable to get you banned)

This functions by simulating your iPhone's location through XCode debugging and a .gpx file.  The program refreshes the .gpx file and resimulates your location to move your character around.

To make this work, create a blank XCode iPhone project and import the .gpx file by referece.  Then, while your device is tethered, go into debug mode on your device and there will be a menu option for simulating location.  Note the coordinates for this button and then note the coordinates for the .gpx file to be selected after this button is pressed.  Fill these in at the appropriate place in the code.
