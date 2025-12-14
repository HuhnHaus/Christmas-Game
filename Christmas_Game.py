import pygame, sys
import random


pygame.init()

W, H = 900, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Christmas Game")
clock = pygame.time.Clock()
score = 0 
font = pygame.font.SysFont(None, 28)
player_x = 450
player_y = 500
player_w = 50
player_h = 50
player_img = pygame.image.load("assets/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (player_w, player_h))
flake_img = pygame.image.load("assets/snowflake.png").convert_alpha()
flake_img = pygame.transform.scale(flake_img, (24, 24))
flakes = []
lives = 5
state = "play"  # "play", "win", "lose"
TARGET = 20
player_speed = 500  # pixels pro Sekunde (anpassen 300–800)
spawn_timer = 0  # Timer für regelmäßiges Spawnen





while True:

    # === Event === #
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            score = 0
            lives = 5
            flakes.clear()
            spawn_timer = 0
            state = "play"


    # === Update === #
    dt = clock.tick(60) / 1000
    
    

    if state == "play":

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed * dt

        player_x = max(10, min(W - player_w - 10, player_x))

        
        # Jede Sekunde eine Flocke spawnen
        spawn_timer += dt
        if spawn_timer >= 1.0:
            flakes.append([random.randint(0, 900), -10, random.randint(6, 12), random.randint(120, 180)])
            spawn_timer = 0


        for i in range(len(flakes) -1, -1, -1,):
            x, y, r, vy = flakes[i]
            y += vy * dt
            flakes[i][1] = y
            
            flake_rect = pygame.Rect(int(x - r), int(y - r), int(2 * r), int(2 * r))

            if player_rect.colliderect(flake_rect):
                score += 1
                flakes.pop(i)

            if y > H + 30:
                lives -= 1
                flakes.pop(i)

        if score >= TARGET:
            state = "win"
        if lives <= 0:
            state = "lose"

        
        
    player_rect = pygame.Rect(int(player_x), int(player_y), player_w, player_h)

        
    
    # === Draw === #
    screen.fill((10, 15, 30))
    
    for x, y, r, vy in flakes:
        flake_rect = pygame.Rect(int(x - r), int(y - r), int(2 * r), int(2 * r))
        screen.blit(flake_img, flake_rect)

    screen.blit(player_img, player_rect)
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (15, 15))
    
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (15, 40))

    if state != "play":
        overlay = pygame.Surface((W, H), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        msg = "YOU WIN!" if state == "win" else "GAME OVER"
        end_text = font.render(msg + "  (Press R)", True, (255, 255, 255))
        screen.blit(end_text, (W//2 - end_text.get_width()//2, H//2))


    # === Flip === #
    pygame.display.flip()