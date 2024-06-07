import pygame

def check_collision(player, obstacles, powerups):
    # 플레이어와 장애물 간의 충돌 확인
    if pygame.sprite.spritecollideany(player, obstacles):
        return 'hit_obstacle'

    # 플레이어와 파워업 간의 충돌 확인
    powerup_hit = pygame.sprite.spritecollideany(player, powerups)
    if powerup_hit:
        powerup_hit.kill()
        return 'hit_powerup'

    return None