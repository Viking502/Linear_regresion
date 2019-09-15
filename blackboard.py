import pygame
import random
import numpy as np
from regresion import Regresion


class Blackboard:

    points = []

    def __init__(self):
        pygame.init()
        win_size = (1200, 800)
        self.window = pygame.display.set_mode(win_size, pygame.RESIZABLE)

        self.coefficient_a = 1/2
        self.coefficient_b = 5
#        self.rand_points()

        self.neuron = Regresion(1)

    def add_points_cloud(self, position, numbers, dispersion):
        for i in range(numbers):
            dx = random.randint(-dispersion, dispersion)
            dy = random.randint(-dispersion, dispersion)
            self.points.append(np.add(position, [dx, dy]))

    def add_point(self, position):
        self.points.append(position)

    def rand_points(self):
        self.points.clear()
        for i in range(50):
            x = random.randint(100, 1100)
            y = random.randint(100, 700)
            self.points.append([x, y])

    def draw(self):
        pygame.draw.line(self.window, pygame.Color(200, 200, 200), [0, 0], [0, 700], 4)
        pygame.draw.line(self.window, pygame.Color(200, 200, 200), [0, 0], [1100, 0], 4)

        pygame.draw.line(self.window, pygame.Color(40, 220, 20), [0, int(self.neuron.bias)],
                         [1100, int(1100 * self.neuron.weight[0] + self.neuron.bias)], 2)

        for p in self.points:
            pygame.draw.circle(self.window, pygame.Color(0, 220, 220), p, 5)
#            pygame.draw.circle(self.window, pygame.Color(0, 200, 0), p, 7, 2)

    def run(self):

        clock = pygame.time.Clock()
        run_flag = True
        learn_flag = False

        while run_flag:
            clock.tick(30)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run_flag = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_d:
                        print('learning...')
                        for p in self.points:
                            self.neuron.learn(p)
                        print('finished')
                    if e.key == pygame.K_r:
                        self.points.clear()
                    if e.key == pygame.K_SPACE:
                        #self.add_points_cloud(pygame.mouse.get_pos(), 10, 40)
                        self.add_point(pygame.mouse.get_pos())
                        print(self.points)


                self.window.fill((40, 40, 40))
                self.draw()
                pygame.display.update()


if __name__ == "__main__":
    board = Blackboard()
    board.run()