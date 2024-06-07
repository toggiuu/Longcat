import unittest
from game_logic.powerup import PowerUp

class TestPowerUp(unittest.TestCase):
    def test_powerup_initialization(self):
        powerup = PowerUp((100, 100))
        self.assertEqual(powerup.rect.topleft, (100, 100))

if __name__ == '__main__':
    unittest.main()