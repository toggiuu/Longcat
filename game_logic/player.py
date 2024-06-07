import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos, empty_cells, obstacles):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/catHead.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_pos["x"], start_pos["y"])
        self.speed = 61  # 고양이의 머리 가로 크기
        self.body = []
        self.body_positions = set()  # 몸체 위치를 저장할 집합
        self.empty_cells = empty_cells
        self.obstacles = obstacles

        # 초기 위치에서 몸체를 추가
        self.add_body_part()

    def update(self, keys, bounds):
        move = None
        if keys[pygame.K_LEFT]:
            move = (-self.speed, 0)
        elif keys[pygame.K_RIGHT]:
            move = (self.speed, 0)
        elif keys[pygame.K_UP]:
            move = (0, -self.speed)
        elif keys[pygame.K_DOWN]:
            move = (0, self.speed)

        if move:
            self.move(*move, bounds)

    def move(self, dx, dy, bounds):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Check if the new position is in an empty cell, occupied by the body, or occupied by an obstacle
        cell_x = (new_x - bounds["left"]) // self.speed
        cell_y = (new_y - bounds["top"]) // self.speed
        grid_pos = (cell_y, cell_x)
        
        if grid_pos in self.empty_cells or grid_pos in self.obstacles or (new_x, new_y) in self.body_positions:
            return

        if bounds["left"] <= new_x <= bounds["right"] - self.rect.width:
            self.rect.x = new_x
        if bounds["top"] <= new_y <= bounds["bottom"] - self.rect.height:
            self.rect.y = new_y

        # Add new body part
        self.add_body_part()

    def add_body_part(self):
        body_part = pygame.sprite.Sprite()
        body_part.image = pygame.image.load('assets/sprites/catBody.png').convert_alpha()
        body_part.rect = body_part.image.get_rect()
        body_part.rect.topleft = self.rect.topleft
        self.body.append(body_part)
        self.body_positions.add((self.rect.x, self.rect.y))

    def draw(self, screen):
        for part in self.body:
            screen.blit(part.image, part.rect)
        screen.blit(self.image, self.rect)