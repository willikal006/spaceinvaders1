# Create bullet groups
# TODO: assign pygame.sprite.Group() to my_player_bullet_group
my_player_bullet_group = pygame.sprite.Group()
# TODO: assign pygame.sprite.Group() to my_alien_bullet_group
my_alien_bullet_group = pygame.sprite.Group()

# Create a player group and Player object
# TODO: assign pygame.sprite.Group() to my_player_group
my_player_group = pygame.sprite.Group()
# TODO: assign Player(my_player_bullet_group) to my_player
my_player = Player(my_player_bullet_group)
# TODO: call the my_player_group.add() function and pass in my_player as the argument.
my_player_group.add(my_player)

# Create an alien group. Will add Alien objects via the game's start new round method
# TODO: assign pygame.sprite.Group() to my_alien_group
my_alien_group = pygame.sprite.Group()

# Create a Game object
