# TODO: assign Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group) to my_game
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
# TODO: call the my_game.start_new_round() function with no arguments.
my_game.start_new_round()

# The main game loop
# TODO: assign True to running
running = True
# TODO: while running:
while running:
    # TODO: for event in pygame.event.get()
    for event in pygame.event.get():
        # Check to see if the user wants to quit
        # TODO: if event.type == pygame.QUIT
        if event.type == pygame.QUIT:
            # TODO: assign False to running
            running = False

        # The player wants to fire
        # TODO: if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            # TODO: if event.key == pygame.K_SPACE:
            if event.key == pygame.K_SPACE:
                # TODO: call my_player.fire() function with no arguments.
                my_player.fire()

    # Fill the display
    # TODO: call display_surface.fill() function and pass in (0, 0, 0) for the argument.
    display_surface.fill((0, 0, 0))

    # Update and display all sprite groups
    # TODO: call my_player_group.update() with no arguments.
    my_player_group.update()
    # TODO: call my_player_group.draw() passing in display_surface as its argument
    my_player_group.draw(display_surface)

