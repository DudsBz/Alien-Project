import sys
from settings import Settings
import pygame as pg
from ship import Ship

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    #A linha pg.init()  inicializa as configurações de segundo plano de que o Pygame precisa para funcionar de forma apropriada
    pg.init()
    screen = pg.display.set_mode((1375, 675))
    pg.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    ai_settings = Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    while True:
        screen.fill(bg_color)
        pg.display.flip()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # pg.event.get() dentro do laço while repete conforme os eventos (mouse, teclado etc)
        for event in pg.event.get():   
            if event.type == pg.QUIT: 
                sys.exit()
            pg.display.flip()
run_game()
