import unittest
from game_logic.obstacle import Obstacle

class TestObstacle(unittest.TestCase):
    def test_obstacle_initialization(self):
        obstacle = Obstacle((100, 100))
        self.assertEqual(obstacle.rect.topleft, (100, 100))

if __name__ == '__main__':
    unittest.main()