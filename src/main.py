from src.settings import *
from src.support import *
from src.monster import Monster, Opponent
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monster_lists = ['Sparchu', 'Cleaf', 'Jacana']
        self.player_monsters = [Monster(name, self.back_surfs[name]) for name in player_monster_lists]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)
        opponent_name = 'Jacana'
        opponent_image = self.back_surfs[opponent_name]
        self.opponent = Monster(opponent_name, opponent_image)
        self.all_sprites.add(self.opponent)

    def import_assets(self):
        self.back_surfs = folder_importer('images', 'back')
        self.bg_surfs = folder_importer('images', 'other')

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(dt)

            # draw  
            self.display_surface.blit(self.bg_surfs['bg'], (0,0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()