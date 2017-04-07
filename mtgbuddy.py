#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


from random import randint

print("MTGBuddy 1.0")
print("Copyleft 2017 Carsan Hofelt")
print()

counter = 0 #Also used to keep player info synced across lists, if that makes sense

players = input("Who's playing? ").split(" ")
life = [input("Starting Life totals? ")] * len(players) #Makes a list of life totals with one entry for each player.

poison = [0] * len(players) #Might as well just declare this now.
xp = [0] * len(players) #Also this

while True:
	counter = 0
	
	while counter != len(players):
		#Reiterate life totals and poison counters
		print("Player", str(counter + 1) + ":", players[counter] + ":", life[counter], "life", poison[counter], "poison", xp[counter], "XP")
		counter += 1
	
	counter = 0 #Make 
	
	com = input("Change [L]ife totals, add [P]oison counters, add [E]xperience counters, [R]oll dice, or [Q]uit? ")
	com = com.lower()
	
	if com == "l":
		target = int(input("Which player? (1 - " + str(len(players)) + ") ")) - 1
		change = int(input("How much do they gain/lose? (To subtract, use negative numbers.) "))
		life[target] = int(life[target]) + change
		
	elif com == "p":
		target = int(input("Which player? (1 - " + str(len(players)) + ") ")) - 1
		change = int(input("How many do they gain/lose? (To subtract, use negative numbers.) "))
		poison[target] = int(poison[target]) + change
	
	elif com == "e":
		target = int(input("Which player? (1 - " + str(len(players)) + ") ")) - 1
		change = int(input("How many do they gain/lose? (To subtract, use negative numbers.) "))
		xp[target] = int(xp[target]) + change
		
	elif com == "r":
		sides = int(input("How many sides? "))
		die = int(input("How many die? "))
		
		while counter != die:
			print(randint(1, sides))
			counter += 1
			
	elif com == "q":
		print("Goodbye.")
		break
		
#Communism will prevail!
