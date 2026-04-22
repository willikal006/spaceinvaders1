 my_alien_group.update()
    my_alien_group.draw(display_surface)

    # TODO: repeat the last 2 todo's with my_player_bullet_group
    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    # TODO: repeat the last 2 todo's with my_alien_bullet_group
    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    # Update and draw Game object
    # TODO: call my_game.update() with no arguments
    my_game.update()
    # TODO: call my_game.draw() with no arguments
    my_game.draw()

    # Update the display and tick clock
    # TODO: call pygame.display.update() with no arguments
    pygame.display.update()
    # TODO: call clock.tick() with FPS as its only argument
    clock.tick(FPS)

# End the game
pygame.quit()
exitcode = 1
if exitcode == 0:
    pygame.quit()
