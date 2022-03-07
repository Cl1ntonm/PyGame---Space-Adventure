# importing necessary modules for program functions

import pygame
import random
import time

# Game Name - Space Adventure
# Game Premise - Set in space , where player takes control of a space ship
# Game Mechanics - Player has to avoid Asteroids , each with different difficulty settings
#                  and get to the safety of the Space station and win the game.
#                  Should the player crash into th Asteroids or not get to the space station in time,
#                  the player will loose the game.

# Task objectives met:
# One ‘player’ object - check
# Move player with up/down/left/right arrow keys - check
# player object collision end the game - check
# one prize object, collision wins the game- check

# Initialize the pygame modules

pygame.init()

# Defining the games screen parameters (width and height)

screen_width = 1040
screen_height = 680

# This creates the screen and gives it the width and height.

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the pygame window name to that of the game title

pygame.display.set_caption("Space Adventure ")

# This creates the items of the game (player, Asteroids and Space station )
# this step aps assigns the image file to represent them

player = pygame.image.load("space_ship.png")
asteroid_small = pygame.image.load("asteroid_small.png")
asteroid_medium = pygame.image.load("asteroid_medium.png")
asteroid_large = pygame.image.load("asteroid_large.png")
space_station = pygame.image.load("space_station.png")

# Gets the width and height of the images in order to do boundary detection

# Space Ship
space_ship_height = player.get_height()
space_ship_width = player.get_width()

# Asteroid Small
asteroid_small_height = asteroid_small.get_height()
asteroid_small_width = asteroid_small.get_width()

# Asteroid Medium
asteroid_medium_height = asteroid_medium.get_height()
asteroid_medium_width = asteroid_medium.get_width()

# Asteroid Large
asteroid_large_height = asteroid_large.get_height()
asteroid_large_width = asteroid_large.get_width()

# Space Station
space_station_height = space_station.get_height()
space_station_width = space_station.get_width()

# Store the positions of the player as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Sets Velocity / speed of the space ship, so that it can be changed later if needed
vel = 15

# Indicates pygame is running
run = True

# Make the Space Station start off screen and a6tytt a random y position.

space_stationXPosition = screen_width
space_stationYPosition = random.randint(0, screen_height - space_station_height)

# Make the asteroids start off screen and at a random y position:

# Asteroid Small
asteroid_smallXPosition = screen_width
asteroid_smallYPosition = random.randint(0, screen_height - asteroid_small_height)

# Asteroid Medium
asteroid_mediumXPosition = screen_width
asteroid_mediumYPosition = random.randint(0, screen_height - asteroid_medium_height)

# Asteroid Large
asteroid_largeXPosition = screen_width
asteroid_largeYPosition = random.randint(0, screen_height - asteroid_large_height)

# Before game s
# 5
# tarts , step displays the Game title and Objective

for event in pygame.event.get():
    # Displays the Game start screen on Time delay
    start = pygame.image.load("start_game.png")
    screen.blit(start, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    break

# Main Game loop
while run:

    # Sets up the  background for game play
    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))

    # This draws the player image to the screen at the position specified. (100, 50).

    screen.blit(player, (playerXPosition, playerYPosition))

    # Brings Space station image to screen

    screen.blit(space_station, (space_stationXPosition, space_stationYPosition))

    # Brings to screen Asteroid Small image

    screen.blit(asteroid_small, (asteroid_smallXPosition, asteroid_smallYPosition))

    # Brings to screen Asteroid Medium image

    screen.blit(asteroid_medium, (asteroid_mediumXPosition, asteroid_mediumYPosition))

    # Brings to screen Asteroid Large image image

    screen.blit(asteroid_large, (asteroid_largeXPosition, asteroid_largeYPosition))

    # This updates the screen display.

    pygame.display.flip()

    # key board movements function that loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # Stores keys pressed to be used as space ship movement instructions

    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and playerXPosition > 0:
        # Move the space ship to the Left
        playerXPosition -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and playerXPosition < 1040 - space_ship_width:
        # Move the Space ship to the right
        playerXPosition += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and playerYPosition > 0:
        # Move he space ship up
        playerYPosition -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and playerYPosition < 680 - space_ship_height:
        # Moves the space ship down
        playerYPosition += vel

    # To check for collision of the asteroids with the player. to see if player looses or wins the game
    # the following updates the objects box to the objects position,
    # in so doing  making the box stay around the objects image.
    # in this case the space ship , space station and all the Asteroids

    # Creating the Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Creating the Bounding box for the Space station
    space_stationBox = pygame.Rect(space_station.get_rect())
    space_stationBox.top = space_stationYPosition
    space_stationBox.left = space_stationXPosition

    # Creating the Bounding box for the Asteroids

    # Asteroid Small
    asteroid_smallBox = pygame.Rect(asteroid_small.get_rect())
    asteroid_smallBox.top = asteroid_smallYPosition
    asteroid_smallBox.left = asteroid_smallXPosition

    # Asteroid Medium
    asteroid_mediumBox = pygame.Rect(asteroid_medium.get_rect())
    asteroid_mediumBox.top = asteroid_mediumYPosition
    asteroid_mediumBox.left = asteroid_mediumXPosition

    # Asteroid Large
    asteroid_largeBox = pygame.Rect(asteroid_large.get_rect())
    asteroid_largeBox.top = asteroid_largeYPosition
    asteroid_largeBox.left = asteroid_largeXPosition

    # Test collision of the boxes: for win and loose and missed

    if playerBox.colliderect(asteroid_smallBox) or playerBox.colliderect(asteroid_mediumBox) or \
            playerBox.colliderect(asteroid_largeBox):
        game_over = pygame.image.load("game_over.png")
        screen.blit(game_over, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        break

    # setting up the display for the loose scenario should the player miss the space station

    if space_stationXPosition < 0 - space_station_width:
        game_over_failed = pygame.image.load("game_over_failed.png")
        screen.blit(game_over_failed, (0, 0))
        pygame.display.flip()
        time.sleep(2)
        break

    # Setting up the display if player lands on the space station for safety, player and wins the level

    if playerBox.colliderect(space_stationBox):
        # Display Winning Status
        win_screen = pygame.image.load("you_win.png")
        screen.blit(win_screen, (0, 0))
        pygame.display.flip()
        time.sleep(2)
        break

    # Make Space Station approach the player.

    space_stationXPosition -= 2

    # Make asteroid small approach the player.

    asteroid_smallXPosition -= 3

    # Make asteroid medium approach the player.

    asteroid_mediumXPosition -= 4

    # Make asteroid Large approach the player.

    asteroid_largeXPosition -= 5

    # ================The game loop logic ends here. =============
