import sys
import numpy
import pygame
from physics import *

WIDTH = 640
HEIGHT = 480
FRAMERATE_LIMIT = 120

LEFT_CLICK = 1
MIDDLE_CLICK = 2
RIGHT_CLICK = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

BALL_COLOR = (255, 128, 0)
BALL_RADIUS = 10

def new_ball(pos, spd):
    return PhysicsObject(
        ObjectType.BALL, props=(BALL_RADIUS,),
        pos=pos, spd=spd)

objects = [new_ball(pos=(90, 90), spd=(+1, +1))]


def draw(screen):
    color = (32, 64, 96)
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, WIDTH, HEIGHT))

    for object in objects:
        pygame.draw.circle(screen, BALL_COLOR, object.pos, BALL_RADIUS)


def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == LEFT_CLICK:
            pos = pygame.mouse.get_pos()
            objects.append(new_ball(pos=pos, spd=(-1,-1)))
        if event.button == RIGHT_CLICK:
            pos = pygame.mouse.get_pos()
            remove_el = None
            for obj in objects:
                diff = numpy.subtract(pos, obj.pos)
                if numpy.linalg.norm(diff) <= BALL_RADIUS:
                    remove_el = obj
                    break
            if remove_el is not None:
                objects.remove(remove_el)


def draw_fps(screen, fps, font):
    fps_surface = font.render(str(fps), True, pygame.Color('white'))
    screen.blit(fps_surface, (0, 0))


def update_physics(time_diff_ms):
    for obj in objects:
        obj.update_position(time_diff_ms)


def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 30)
    pygame.display.set_caption('Simple physics')

    done = False
    while not done:
        dt_ms = clock.tick(FRAMERATE_LIMIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            handle_event(event)
        update_physics(dt_ms)

        draw(screen)
        draw_fps(screen, int(clock.get_fps()), font)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()
