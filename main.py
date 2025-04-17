import numpy as np
import pygame


# 6.6743015 * (10 ** -11)
G = 1
WIDTH, HEIGHT = 1280, 720
SCALE = 2  # 1 million meters = 1 pixel

class Body:
    def __init__(self, x, y, vx, vy, mass, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.color = color

    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def apply_force(self, fx, fy, dt):
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * dt
        self.vy += ay * dt

    def draw(self, screen):
        if not (np.isfinite(self.x) and np.isfinite(self.y)):
            return
        screen_x = int(self.x / SCALE + WIDTH // 2)
        screen_y = int(self.y / SCALE + HEIGHT // 2)
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), 6)


class Sim:
    def __init__(self):
        self.bodies = [
            Body(640, 360, 0, 0, 1e6, (255, 255, 0)),  # Sun in the middle
            Body(740, 360, 0, 50, 1, (0, 255, 255)),   # Planet A
            Body(540, 360, 0, -50, 1, (255, 0, 255))   # Planet B
        ]

    def compute_gravity(self, dt):
        for i, b1 in enumerate(self.bodies):
            fx, fy = 0.0, 0.0
            for j, b2 in enumerate(self.bodies):
                if i == j:
                    continue
                dx = b2.x - b1.x
                dy = b2.y - b1.y
                dist_squared = dx**2 + dy**2
                dist = np.sqrt(dist_squared) + 1e-10 # avioding 0 division
                force = G * b1.mass * b2.mass / dist_squared
                fx += force * dx / dist
                fy += force * dy / dist
            b1.apply_force(fx, fy, dt)

    def update(self, dt):
        self.compute_gravity(dt)
        for body in self.bodies:
            body.update_position(dt)

    def draw(self, screen):
        for body in self.bodies:
            body.draw(screen)

def run():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        sim = Sim()

        while True:
            dt = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    raise SystemExit

            sim.update(dt)
            screen.fill((0, 0, 0))
            sim.draw(screen)
            pygame.display.flip()

if __name__ == "__main__":
    run()
