import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1700, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 10

# Bullet
bullet_width = 10
bullet_height = 20
bullet_speed = 30
bullets = []

# Enemy
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Spawn a row of enemies
def spawn_enemies():
    for i in range(9):
        x = 80 * i + 40
        y = 50
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))
a = 1
b = 11
while b >= a:  
    for i in range(10):
        spawn_enemies()
    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BLACK)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_d] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 100:  # Limit bullets on screen
                bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2,
                                     player_y, bullet_width, bullet_height)
                bullets.append(bullet)

        # Update bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Update enemies
        for enemy in enemies[:]:
            enemy.x += enemy_speed
            if enemy.right > WIDTH or enemy.left < 0:
                enemy_speed *= -1
                for e in enemies:
                    e.y += 20
                break

        # Check collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

        # Draw player
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, RED, bullet)

        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, WHITE, enemy)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()
