import pygame
from objects import *

pygame.init()

SCREEN_WITH = 1280
SCREEN_HEITH = 720

screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEITH))

clock = pygame.time.Clock()


pedrinho = Cobra(Vector(SCREEN_WITH/2, SCREEN_HEITH/2), _num_segments=20, _distance_segments=20, _speed=5)


def logical_update():
    
    
    buttons_pressed = pygame.mouse.get_pressed(num_buttons=3)
    mouse_pos = pygame.mouse.get_pos()
        
    if (buttons_pressed[0] == True):
        pedrinho.update(mouse_pos)
        
  
        

def grafic_render():
    for seg in pedrinho.segments:
        pygame.draw.circle(screen, "yellow", (seg.position.x, seg.position.y), pedrinho.distance_segments/1.5)



while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                pedrinho.add_segment()
                
 
            if event.key == pygame.K_q:
                pedrinho.remove_segment()

    # Do logical updates here.
    logical_update()

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    grafic_render()

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    
    
