from game_settings import (display_surface,
                           pygame,
                           maps,
                           TILE_SIZE,
                           FONT_SIZE,
                           WINDOW_WIDTH,WINDOW_HEIGHT,
                           button_color,
                           sys,
                           join
                           )
from sprites import GroundSprite,CollisionSprite,AreaSprite
import pymunk
import pymunk.pygame_util

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = (0, 1000)
        self.draw_options = pymunk.pygame_util.DrawOptions(display_surface)

    def create_ground(self):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (400, 550)
        self.shape = pymunk.Segment(self.body, (-400, 0), (400, 0), 5)
        self.shape.friction = 0.9
        self.space.add(self.body, self.shape)

    def create_ball(self,position):
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 15))
        self.body.position = position
        self.shape = pymunk.Circle(self.body, 15)
        self.shape.elasticity = 0.7
        self.shape.friction = 0.5
        self.space.add(self.body, self.shape)
        return self.shape

    def run(self):
        self.create_ground()
        self.balls = [self.create_ball((400, 50))]

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.balls.append(self.create_ball(mouse_pos))

            self.space.step(1 / 60.0)
            display_surface.fill((0, 0, 0))
            self.space.debug_draw(self.draw_options)

            pygame.display.update()
            self.clock.tick(60)
        return
