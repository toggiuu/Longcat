import pygame
import json
from game_logic.player import Player
from game_logic.obstacle import Obstacle
import settings

class Level:
    def __init__(self, level_data_path):
        self.load_level_data(level_data_path)
        self.player = Player(self.player_start, self.empty_cells, self.get_obstacle_positions())
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player)

        # Load background image
        self.background = pygame.image.load('assets/backgrounds/background.png').convert()

        # Add obstacles from level data
        for obstacle_pos in self.obstacle_positions:
            obstacle = Obstacle(self.get_pixel_position(obstacle_pos))
            self.obstacles.add(obstacle)
            self.all_sprites.add(obstacle)

        self.puzzle_solved = False

    def load_level_data(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            self.player_start = data["player_start"]
            self.puzzle_bounds = data["puzzle_bounds"]
            self.puzzle_size = data["puzzle_size"]
            self.empty_cells = set((cell["row"], cell["col"]) for cell in data.get("empty_cells", []))
            self.obstacle_positions = [self.get_grid_position(cell["x"], cell["y"]) for cell in data.get("obstacles", [])]

    def get_obstacle_positions(self):
        return self.obstacle_positions

    def get_grid_position(self, x, y):
        return ((y - self.puzzle_bounds["top"]) // settings.CELL_SIZE,
                (x - self.puzzle_bounds["left"]) // settings.CELL_SIZE)

    def get_pixel_position(self, grid_pos):
        return (self.puzzle_bounds["left"] + grid_pos[1] * settings.CELL_SIZE,
                self.puzzle_bounds["top"] + grid_pos[0] * settings.CELL_SIZE)

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.puzzle_bounds)

        # Check if the puzzle is solved
        if not self.puzzle_solved and self.is_puzzle_solved():
            self.puzzle_solved = True

    def draw(self, screen):
        # Draw background
        screen.blit(self.background, (0, 0))

        # Draw puzzle grid
        self.draw_puzzle(screen)

        # Draw game elements
        self.obstacles.draw(screen)
        self.player.draw(screen)

        # Draw "Puzzle Solved!" message if puzzle is solved
        if self.puzzle_solved:
            font = pygame.font.Font(None, 36)
            text = font.render('Puzzle Solved!', True, (255, 255, 255))
            screen.blit(text, (screen.get_width() - 250, 10))  # 오른쪽 상단에 표시

    def draw_puzzle(self, screen):
        for row in range(self.puzzle_size):
            for col in range(self.puzzle_size):
                if (row, col) not in self.empty_cells:
                    x = self.puzzle_bounds["left"] + col * settings.CELL_SIZE
                    y = self.puzzle_bounds["top"] + row * settings.CELL_SIZE
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, settings.CELL_SIZE, settings.CELL_SIZE), 1)

    def is_puzzle_solved(self):
        # Calculate filled cells as grid positions (row, col)
        filled_cells = {((part.rect.y - self.puzzle_bounds["top"]) // settings.CELL_SIZE,
                         (part.rect.x - self.puzzle_bounds["left"]) // settings.CELL_SIZE)
                        for part in self.player.body}
        
        all_cells = {(row, col)
                     for row in range(self.puzzle_size) for col in range(self.puzzle_size)
                     if (row, col) not in self.empty_cells and (row, col) not in self.get_obstacle_positions()}

        return all_cells == filled_cells