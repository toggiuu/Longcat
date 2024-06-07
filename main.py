import sys
import pygame
import settings
from game_logic.level import Level
from controls.input_handler import handle_input

def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption("Longcat")
    clock = pygame.time.Clock()
    level_files = ['levels/level1.json', 'levels/level2.json', 'levels/level3.json', 'levels/level4.json']  # 레벨 파일 리스트
    current_level_index = 0
    level = Level(level_files[current_level_index])

    reset_button = pygame.Rect(10, 10, 100, 50)
    next_level_button = pygame.Rect(120, 10, 100, 50)
    prev_level_button = pygame.Rect(230, 10, 100, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint(event.pos):
                    level = Level(level_files[current_level_index])
                if next_level_button.collidepoint(event.pos):
                    if current_level_index < len(level_files) - 1:
                        current_level_index += 1
                        level = Level(level_files[current_level_index])
                if prev_level_button.collidepoint(event.pos):
                    if current_level_index > 0:
                        current_level_index -= 1
                        level = Level(level_files[current_level_index])

        handle_input(level.player, level.puzzle_bounds)
        level.update()
        level.draw(screen)

        pygame.draw.rect(screen, (255, 0, 0), reset_button)
        pygame.draw.rect(screen, (0, 255, 0), next_level_button)
        pygame.draw.rect(screen, (0, 0, 255), prev_level_button)

        font = pygame.font.Font(None, 36)
        reset_text = font.render('Reset', True, (255, 255, 255))
        next_text = font.render('Next', True, (255, 255, 255))
        prev_text = font.render('Prev', True, (255, 255, 255))
        screen.blit(reset_text, (20, 20))
        screen.blit(next_text, (130, 20))
        screen.blit(prev_text, (240, 20))

        pygame.display.flip()
        clock.tick(settings.FPS)
    pygame.quit()

if __name__ == "__main__":
    main()