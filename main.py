import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720

# Font
FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

# Screen setup
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

# Clock
CLOCK = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player = pygame.Rect(WIDTH - 100, HEIGHT // 2 -
                     PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(100, HEIGHT // 2 - PADDLE_HEIGHT //
                       2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Scores
player_score, opponent_score = 0, 0

# Ball
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT //
                   2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = random.choice([1, -1]), random.choice([1, -1])

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys_pressed[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5

    # Ball movement
    ball.x += ball_speed_x * 4
    ball.y += ball_speed_y * 4

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x, ball_speed_y = random.choice(
            [1, -1]), random.choice([1, -1])
    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x, ball_speed_y = random.choice(
            [1, -1]), random.choice([1, -1])

    # Opponent AI
    if opponent.centery < ball.centery:
        opponent.y += 3
    if opponent.centery > ball.centery:
        opponent.y -= 3

    # Draw everything
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, player)
    pygame.draw.rect(SCREEN, WHITE, opponent)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player_score_text = FONT.render(str(player_score), True, WHITE)
    opponent_score_text = FONT.render(str(opponent_score), True, WHITE)
    SCREEN.blit(player_score_text, (WIDTH // 2 + 20, 20))
    SCREEN.blit(opponent_score_text, (WIDTH // 2 - 40, 20))

    # Update display
    pygame.display.flip()
    CLOCK.tick(60)
