import numpy
import pygame

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
balls = [(90, 90)]


def draw(screen):
    color = (32, 64, 96)
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, WIDTH, HEIGHT))

    for ball_pos in balls:
        pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)


def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == LEFT_CLICK:
            pos = pygame.mouse.get_pos()
            balls.append(pos)
        if event.button == RIGHT_CLICK:
            pos = pygame.mouse.get_pos()
            remove_el = None
            for ball in balls:
                diff = numpy.subtract(pos, ball)
                if numpy.linalg.norm(diff) <= BALL_RADIUS:
                    remove_el = ball
                    break
            if remove_el is not None:
                balls.remove(remove_el)


def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Simple physics')

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            handle_event(event)

        draw(screen)
        pygame.display.flip()
        clock.tick(FRAMERATE_LIMIT)


if __name__ == "__main__":
    main_loop()
