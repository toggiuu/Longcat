import unittest
from game_logic.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        player = Player()
        self.assertIsNotNone(player.rect)

if __name__ == '__main__':
    unittest.main()