import pygame
import math
import random

# --- Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# Physics
GRAVITY = 0.2
FRICTION = 0.99
BOUNCE = 0.8

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vy += GRAVITY
        self.vx *= FRICTION
        self.vy *= FRICTION
        self.x += self.vx
        self.y += self.vy

        # Wall collisions
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -BOUNCE
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.vx *= -BOUNCE
        
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -BOUNCE
        
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

class Bumper:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = BLUE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, ball):
        dx = ball.x - self.x
        dy = ball.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < ball.radius + self.radius:
            # Simple bounce logic
            angle = math.atan2(dy, dx)
            speed = math.sqrt(ball.vx**2 + ball.vy**2) + 2 # Add a little kick
            ball.vx = math.cos(angle) * speed
            ball.vy = math.sin(angle) * speed
            # Move ball outside bumper
            ball.x = self.x + math.cos(angle) * (ball.radius + self.radius)
            ball.y = self.y + math.sin(angle) * (ball.radius + self.radius)
            return True
        return False

class Paddle:
    def __init__(self, x, y, width, height, side):
        self.rect = pygame.Rect(x, y, width, height)
        self.side = side # 'left' or 'right'
        self.angle = 0
        self.target_angle = 0
        self.base_y = y

    def update(self, active):
        if active:
            self.target_angle = -30 if self.side == 'left' else 30
        else:
            self.target_angle = 0
        
        self.angle += (self.target_angle - self.angle) * 0.3

    def draw(self, screen):
        # Rotating paddle is complex with Rect, drawing simple rectangle for now
        # For a better look, use a surface or polygon
        pygame.draw.rect(screen, RED, self.rect)

    def check_collision(self, ball):
        if self.rect.collidepoint(ball.x, ball.y + ball.radius):
            ball.vy = -abs(ball.vy) * 1.2 - 2
            ball.vx += (ball.x - (self.rect.x + self.rect.width/2)) * 0.1
            return True
        return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pinball")
    clock = pygame.time.Clock()

    ball = Ball(SCREEN_WIDTH // 2 + 50, 100, 10)
    bumpers = [
        Bumper(100, 150, 30),
        Bumper(300, 150, 30),
        Bumper(200, 300, 40)
    ]
    
    left_paddle = Paddle(50, 550, 100, 20, 'left')
    right_paddle = Paddle(250, 550, 100, 20, 'right')

    running = True
    score = 0
    font = pygame.font.SysFont(None, 36)

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        l_active = keys[pygame.K_LEFT]
        r_active = keys[pygame.K_RIGHT]

        # Update
        ball.update()
        left_paddle.update(l_active)
        right_paddle.update(r_active)

        for bumper in bumpers:
            if bumper.check_collision(ball):
                score += 10
        
        left_paddle.check_collision(ball)
        right_paddle.check_collision(ball)

        # Reset if ball falls
        if ball.y > SCREEN_HEIGHT:
            ball.x, ball.y = SCREEN_WIDTH // 2, 100
            ball.vx, ball.vy = 0, 0
            score = 0

        # Draw
        ball.draw(screen)
        for bumper in bumpers:
            bumper.draw(screen)
        left_paddle.draw(screen)
        right_paddle.draw(screen)

        score_text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
