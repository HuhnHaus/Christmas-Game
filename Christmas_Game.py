import pygame, sys

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Christmas Game")
clock = pygame.time.Clock()
score = 0 
font = pygame.font.SysFont(None, 28)
player_x = 450
player_y = 500
player_w = 50
player_h = 50
flakes = []
dt = clock.tick(60) / 1000

while True:
    for e in pygame.event.get():
        print(e)
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((10, 15, 30))
    pygame.draw.rect(screen, (190, 190, 190), player_rect, border_radius=12)
    pygame.draw.rect(screen, (255, 255, 255), player_rect, width=2, border_radius=12)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (15, 15))
    pygame.display.flip()
    player_rect= pygame.Rect(int(player_x), int(player_y), player_w, player_h)

    for i in range(len(flakes) -1, -1, -1,):
        x, y, r, vy = flakes[i]
        y += vy * dt
        flakes[i][1] = y
        
        flake_rect = pygame.Rect(int(x - r), int(y - r), int(2 * r), int(2 * r))

        if player_rect.colliderect(flake_rect):
            score += 1
            flakes.pop(i)
    

    