"""
Tic-Tac-Toe
Made by Zeus James Baltazar
Date Started: 05/10/2018
Date Finished: 05/11/2018

"""
# Import libraries
import pygame
from settings import *
from sprites import *
# Main class of the game
class GAME:
    # Initialize pygame
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tic-tac-toe")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load('Elevator_music.mp3')
        self.running = True
        self.style = pygame.font.match_font('arial')
        self.x_mouse = pygame.image.load('xcursor.png')
        self.o_mouse = pygame.image.load('ocursor.png')
        self.x_mouse_rect = self.x_mouse.get_rect()
        self.o_mouse_rect = self.o_mouse.get_rect()
        self.SCORE_POINTS = [0, 0]
    # New game method
    def new(self):
        pygame.mixer.music.play(-1)
        self.X_WIN = False
        self.O_WIN = False
        self.OXbool = [True, False]
        # This is for selection in x
        self.SELECTION = [False, False, False,
                          False, False, False,
                          False, False, False]
        self.SX = [False, False, False,
                   False, False, False,
                   False, False, False]
        self.SO = [False, False, False,
                   False, False, False,
                   False, False, False]
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.area_group = pygame.sprite.Group()
        # Area instances
        self.area1 = Area(*POINTS[0]); self.area2 = Area(*POINTS[1]); self.area3 = Area(*POINTS[2])
        self.area4 = Area(*POINTS[3]); self.area5 = Area(*POINTS[4]); self.area6 = Area(*POINTS[5])
        self.area7 = Area(*POINTS[6]); self.area8 = Area(*POINTS[7]); self.area9 = Area(*POINTS[8])
        # Area instances' group
        self.areas = [self.area1, self.area2, self.area3,
                      self.area4, self.area5, self.area6,
                      self.area7, self.area8, self.area9]
        # Add area instances to sprite group
        for area in self.areas:
            self.area_group.add(area)
        # X instances
        self.x1 = X(*POINTS[0]); self.x2 = X(*POINTS[1]); self.x3 = X(*POINTS[2])
        self.x4 = X(*POINTS[3]); self.x5 = X(*POINTS[4]); self.x6 = X(*POINTS[5])
        self.x7 = X(*POINTS[6]); self.x8 = X(*POINTS[7]); self.x9 = X(*POINTS[8])
        # O instances
        self.o1 = O(*POINTS[0]); self.o2 = O(*POINTS[1]); self.o3 = O(*POINTS[2])
        self.o4 = O(*POINTS[3]); self.o5 = O(*POINTS[4]); self.o6 = O(*POINTS[5])
        self.o7 = O(*POINTS[6]); self.o8 = O(*POINTS[7]); self.o9 = O(*POINTS[8])
        # Initialize run method
        self.run()
    # Run method
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # Event method
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # If mouse button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If selection is not true (It prevents the image to be doubled)
                if self.SELECTION[0] != True:
                    if self.area1.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x1.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x1)
                            self.OXbool = [False, True]
                            # This score in SX[0]
                            if self.SO[0] != True:
                                self.SX[0] = True
                        elif self.OXbool[1]:
                            if self.o1.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o1)
                            self.OXbool = [True, False]
                            # This scores in SO[0]
                            if self.SX[0] != True:
                                self.SO[0] = True
                        self.SELECTION[0] = True
                if self.SELECTION[1] != True:
                    if self.area2.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x2.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x2)
                            self.OXbool = [False, True]
                            # This scores in SX[1]
                            if self.SO[1] != True:
                                self.SX[1] = True
                        elif self.OXbool[1]:
                            if self.o2.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o2)
                            self.OXbool = [True, False]
                            # This scores in SO[1]
                            if self.SX[1] != True:
                                self.SO[1] = True
                        self.SELECTION[1] = True
                if self.SELECTION[2] != True:
                    if self.area3.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x3.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x3)
                            self.OXbool = [False, True]
                            # This scores in SX[2]
                            if self.SO[2] != True:
                                self.SX[2] = True
                        elif self.OXbool[1]:
                            if self.o3.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o3)
                            self.OXbool = [True, False]
                            # This scores in SO[2]
                            if self.SX[2] != True:
                                self.SO[2] = True
                        self.SELECTION[2] = True
                if self.SELECTION[3] != True:
                    if self.area4.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x4.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x4)
                            self.OXbool = [False, True]
                            # This scores in SX[3]
                            if self.SO[3] != True:
                                self.SX[3] = True
                        elif self.OXbool[1]:
                            if self.o4.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o4)
                            self.OXbool = [True, False]
                            # This scores in SO[3]
                            if self.SX[3] != True:
                                self.SO[3] = True
                        self.SELECTION[3] = True
                if self.SELECTION[4] != True:
                    if self.area5.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x5.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x5)
                            self.OXbool = [False, True]
                            # This scores in SX[4]
                            if self.SO[4] != True:
                                self.SX[4] = True
                        elif self.OXbool[1]:
                            if self.o5.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o5)
                            self.OXbool = [True, False]
                            # This scores in SO[4]
                            if self.SX[4] != True:
                                self.SO[4] = True
                        self.SELECTION[4] = True
                if self.SELECTION[5] != True:
                    if self.area6.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x6.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x6)
                            self.OXbool = [False, True]
                            # This scores in SX[5]
                            if self.SO[5] != True:
                                self.SX[5] = True
                        elif self.OXbool[1]:
                            if self.o6.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o6)
                            self.OXbool = [True, False]
                            # This scores in SO[5]
                            if self.SX[5] != True:
                                self.SO[5] = True
                        self.SELECTION[5] = True
                if self.SELECTION[6] != True:
                    if self.area7.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x7.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x7)
                            self.OXbool = [False, True]
                            # This scores in SX[6]
                            if self.SO[6] != True:
                                self.SX[6] = True
                        elif self.OXbool[1]:
                            if self.o7.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o7)
                            self.OXbool = [True, False]
                            # This scores in SO[6]
                            if self.SX[6] != True:
                                self.SO[6] = True
                        self.SELECTION[6] = True
                if self.SELECTION[7] != True:
                    if self.area8.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x8.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x8)
                            self.OXbool = [False, True]
                            # This scores in SX[7]
                            if self.SO[7] != True:
                                self.SX[7] = True
                        elif self.OXbool[1]:
                            if self.o8.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o8)
                            self.OXbool = [True, False]
                            # This scores in SO[7]
                            if self.SX[7] != True:
                                self.SO[7] = True
                        self.SELECTION[7] = True
                if self.SELECTION[8] != True:
                    if self.area9.rect.collidepoint(event.pos):
                        if self.OXbool[0]:
                            if self.x9.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.x9)
                            self.OXbool = [False, True]
                            # This scores in SX[8]
                            if self.SO[8] != True:
                                self.SX[8] = True
                        elif self.OXbool[1]:
                            if self.o9.rect.collidepoint(event.pos):
                                self.all_sprites.add(self.o9)
                            self.OXbool = [True, False]
                            # This scores in SO[8]
                            if self.SX[8] != True:
                                self.SO[8] = True
                        self.SELECTION[8] = True
        self.CHECKO()
        self.CHECKX()
        self.CHECKOX()
    # Update method
    def update(self):
        # Update sprites
        self.all_sprites.update()
        self.area_group.update()
    def CHECKX(self):
        # For X
        if self.SX[0] and self.SX[1] and self.SX[2]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[0] and self.SX[3] and self.SX[6]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[0] and self.SX[4] and self.SX[8]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[1] and self.SX[4] and self.SX[7]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[2] and self.SX[5] and self.SX[8]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[3] and self.SX[4] and self.SX[5]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[6] and self.SX[7] and self.SX[8]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
        if self.SX[2] and self.SX[4] and self.SX[6]:
            self.SCORE_POINTS[0] += 1
            self.X_WIN = True
            self.playing = False
    def CHECKO(self):
        # For O
        if self.SO[0] and self.SO[1] and self.SO[2]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[0] and self.SO[3] and self.SO[6]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[0] and self.SO[4] and self.SO[8]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[1] and self.SO[4] and self.SO[7]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[2] and self.SO[5] and self.SO[8]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[3] and self.SO[4] and self.SO[5]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[6] and self.SO[7] and self.SO[8]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
        if self.SO[2] and self.SO[4] and self.SO[6]:
            self.SCORE_POINTS[1] += 1
            self.O_WIN = True
            self.playing = False
    # Checks if someone wons the game
    def CHECKOX(self):
        if sum(self.SELECTION) == 9 and sum(self.SO) != 3:
            self.playing = False
    # Draw method
    def draw(self):
        self.screen.fill(GRAY)
        self.all_sprites.draw(self.screen)
        for line in LINES:
            pygame.draw.line(self.screen, BLACK, line, LINES[line], 5)
        self.mouse_pos = pygame.mouse.get_pos()
        # Draws line whenever one wins
        if self.SX[0] and self.SX[1] and self.SX[2] or self.SO[0] and self.SO[1] and self.SO[2]:
            pygame.draw.line(self.screen, GREEN, POINTS[0], POINTS[2], 10)
        if self.SX[0] and self.SX[3] and self.SX[6] or self.SO[0] and self.SO[3] and self.SO[6]:
            pygame.draw.line(self.screen, GREEN, POINTS[0], POINTS[6], 10)
        if self.SX[0] and self.SX[4] and self.SX[8] or self.SO[0] and self.SO[4] and self.SO[8]:
            pygame.draw.line(self.screen, GREEN, POINTS[0], POINTS[8], 10)
        if self.SX[1] and self.SX[4] and self.SX[7] or self.SO[1] and self.SO[4] and self.SO[7]:
            pygame.draw.line(self.screen, GREEN, POINTS[1], POINTS[7], 10)
        if self.SX[2] and self.SX[5] and self.SX[8] or self.SO[2] and self.SO[5] and self.SO[8]:
            pygame.draw.line(self.screen, GREEN, POINTS[2], POINTS[8], 10)
        if self.SX[3] and self.SX[4] and self.SX[5] or self.SO[3] and self.SO[4] and self.SO[5]:
            pygame.draw.line(self.screen, GREEN, POINTS[3], POINTS[5], 10)
        if self.SX[6] and self.SX[7] and self.SX[8] or self.SO[6] and self.SO[7] and self.SO[8]:
            pygame.draw.line(self.screen, GREEN, POINTS[6], POINTS[8], 10)
        if self.SX[2] and self.SX[4] and self.SX[6] or self.SO[2] and self.SO[4] and self.SO[6]:
            pygame.draw.line(self.screen, GREEN, POINTS[2], POINTS[6], 10)
        if self.OXbool[0]:
            self.screen.blit(self.x_mouse, [self.mouse_pos[0] - self.x_mouse_rect.width/2, self.mouse_pos[1] - self.x_mouse_rect.height/2])
        else:
            self.screen.blit(self.o_mouse, [self.mouse_pos[0] - self.o_mouse_rect.width/2, self.mouse_pos[1] - self.o_mouse_rect.height/2])
        pygame.display.flip()
    # Show game over screen
    def Show_go_screen(self):
        pygame.time.delay(1000)
        pygame.mixer.music.stop()
        self.waiting = True
        self.x = 0
        self.y = height - 30
        while self.waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.waiting = False
            self.MOVE()
            self.draw_go_screen()
    # Create texts
    def GO_TEXTs(self):
        self.GOFONT = pygame.font.Font(self.style, 64)
        self.GO = self.GOFONT.render('GAME OVER!', True, BLACK)
        self.rect = self.GO.get_rect()
        self.rect.center = (width/2, height/6)
        self.ZEUS_FONT = pygame.font.Font(self.style, 20)
        self.ZEUS = self.ZEUS_FONT.render('Made by Zeus James Baltazar', True, BLACK)
        self.ZEUS_rect = self.ZEUS.get_rect()
        self.ZEUS_rect.topleft = (self.x, self.y)
        self.PRESS_FONT = pygame.font.Font(self.style, 32)
        self.PRESS = self.PRESS_FONT.render('Click anywhere to restart', True, BLACK)
        self.PRESS_rect = self.PRESS.get_rect()
        self.PRESS_rect.center = (width/2, height - 70)

        self.SCORE_FONT = pygame.font.Font(self.style, 30)
        self.SCOREtext = self.SCORE_FONT.render("SCORE", True, BLACK)
        self.SCOREtext_rect = self.SCOREtext.get_rect()
        self.SCOREtext_rect.center = (width/2, height/2 - 28)
        self.SCORE = self.SCORE_FONT.render("X: %s ; O: %s" %(str(self.SCORE_POINTS[0]), str(self.SCORE_POINTS[1])), True, BLACK)
        self.SCORE_rect = self.SCORE.get_rect()
        self.SCORE_rect.center = (width/2, height/2)
    # Move Zeus James Baltazar text
    def MOVE(self):
        self.x += 0.5
        if self.x > width:
            self.x = -self.ZEUS_rect.width
    # Draw things in game over screen
    def draw_go_screen(self):
        self.GO_TEXTs()
        self.screen.fill(GRAY)
        self.screen.blit(self.GO, self.rect)
        self.screen.blit(self.ZEUS, self.ZEUS_rect)
        self.screen.blit(self.PRESS, self.PRESS_rect)
        self.screen.blit(self.SCORE, self.SCORE_rect)
        self.screen.blit(self.SCOREtext, self.SCOREtext_rect)
        self.FONT = pygame.font.Font(self.style, 50)
        if self.X_WIN:
            self.XW = self.FONT.render('X wins', True, BLACK)
            self.XWrect = self.XW.get_rect()
            self.XWrect.center = (width/2, height/6 + 60)
            self.screen.blit(self.XW, self.XWrect)
        elif self.O_WIN:
            self.OW = self.FONT.render('O wins', True, BLACK)
            self.OWrect = self.OW.get_rect()
            self.OWrect.center = (width/2, height/6 + 60)
            self.screen.blit(self.OW, self.OWrect)
        else:
            self.D = self.FONT.render('Draw', True, BLACK)
            self.Drect = self.D.get_rect()
            self.Drect.center = (width/2, height/6 + 60)
            self.screen.blit(self.D, self.Drect)
        pygame.display.flip()
    # Show start screen
    def Show_start_screen(self):
        waiting = True
        # Loop of the start screen
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
            self.draw_start_screen()
    # Draw things in show start screen
    def draw_start_screen(self):
        self.START_TEXTs()
        self.screen.fill(GRAY)
        self.screen.blit(self.TIC, self.TICrect)
        self.screen.blit(self.TICPRESS, self.TICPRESS_rect)
        pygame.display.flip()
    # Create texts
    def START_TEXTs(self):
        self.TIC_FONT = pygame.font.Font(self.style, 100)
        self.TIC = self.TIC_FONT.render('TIC-TAC-TOE', True, BLACK)
        self.TICrect = self.TIC.get_rect()
        self.TICrect.center = (width/2, height/2)
        self.TICPRESS_FONT = pygame.font.Font(self.style, 32)
        self.TICPRESS = self.TICPRESS_FONT.render('Click anywhere to start', True, BLACK)
        self.TICPRESS_rect = self.TICPRESS.get_rect()
        self.TICPRESS_rect.center = (width/2, height - 70)
g = GAME()
g.Show_start_screen()
if __name__=="__main__":
    while g.running:
        g.new()
        g.Show_go_screen()
    pygame.quit()








    
