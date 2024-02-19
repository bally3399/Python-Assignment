from unittest import TestCase
from Gun import Gun


class TestGunFunction(TestCase):
    def setUp(self):
        self.Gun = Gun()

    def test_that_chamber_is_empty(self):
        self.assertTrue(self.Gun.chamber_is_empty())

    def test_that_i_can_add_bullet(self):
        self.assertTrue(self.Gun.chamber_is_empty())
        self.Gun.add_bullet()
        self.assertFalse(self.Gun.chamber_is_empty())

    def test_that_i_can_shoot_bulletReduced(self):
        self.assertTrue(self.Gun.chamber_is_empty())
        self.Gun.add_bullet()
        self.Gun.shoot()
        self.assertTrue(self.Gun.chamber_is_empty())

    def test_that_i_addThreeBullet_shootTwice(self):
        self.assertTrue(self.Gun.chamber_is_empty())
        self.Gun.add_bullet()
        self.Gun.add_bullet()
        self.Gun.add_bullet()
        self.Gun.shoot()
        self.Gun.shoot()
        self.assertFalse(self.Gun.chamber_is_empty())

    def test_that_i_Cannot_shoot_when_no_bullet(self):
        self.assertTrue(self.Gun.chamber_is_empty())
        self.Gun.shoot()
        self.assertTrue(self.Gun.chamber_is_empty())

    def test_that_i_can_load_the_chamber(self):
        self.assertTrue(self.Gun.chamber_is_empty())
        self.Gun.load_bullet()
        self.assertFalse(self.Gun.chamber_is_empty())



