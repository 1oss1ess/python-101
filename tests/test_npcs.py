import unittest
from python101.dungeons_and_python.players import Player, Hero


class TestSoldiers(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(name='Ivan', title='Dr.', health=250, mana=100, mana_regeneration_rate=2)
        self.test_soldier = Player(health=200, mana=100)

    def test_create_instance_invalid_input_should_type_error_error(self):
        with self.assertRaises(TypeError):
            Player(health='asd', mana=100)

    def test_create_instance_negative_health_should_rasise_value_error(self):
        with self.assertRaises(ValueError):
            Player(health=-20, mana=20)

    def test_crevte_instance_negative_mana_should_rasise_value_error(self):
        with self.assertRaises(ValueError):
            Player(health=20, mana=-20)

    def test_take_damage_int(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(20)
        self.assertEqual(npc.health, 180)

    def test_take_damage_float(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(10.5)
        self.assertEqual(npc.health, 189.5)

    def test_take_damage_more_damage_than_hp_should_return_0(self):
        npc = Player(health=20, mana=50)
        npc.take_damage(30)
        self.assertEqual(npc.get_health(), 0)

    def test_take_damage_should_raise_type_error_invalid_input(self):
        self.setUp()
        with self.assertRaises(TypeError):
            npc = self.test_soldier
            npc.take_damage('asd')

    def test_take_healing_should_not_get_over_max_hp(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(20)
        npc.take_healing(30)
        self.assertEqual(npc.get_health(), 200)

    # def test_take_mana_should_not_get_over_max_mana(self):


if __name__ == '__main__':
    unittest.main()
