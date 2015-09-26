import unittest
from battleline.model.Formation import Formation, FormationInvalidError
class TestFormation(unittest.TestCase):



    def test_formation_with_less_than_three_cards_is_considered_invalid(self):
        self.assertRaisesRegexp(FormationInvalidError, "Formation must have 3 cards", Formation, [(1, "R"), (2, "Y")])

    def test_formation_with_more_than_three_cards_is_considered_invalid(self):
        self.assertRaisesRegexp(FormationInvalidError, "Formation must have 3 cards", Formation, [(1, "R"), (2, "Y"), (3, "R"), (5, "G")])

    def test_can_get_formation_numbers_in_sorted_fashion(self):
        formation = Formation([(1, "R"), (3, "Y"), (2, "R")])
        self.assertEquals((1,2,3), formation.get_numbers())

        formation = Formation([(10, "R"), (9, "Y"), (8, "R")])
        self.assertEquals((8,9,10), formation.get_numbers())

    def test_can_get_formation_colors_in_sorted_fashion(self):
        formation = Formation([(1, "R"), (3, "Y"), (2, "R")])
        self.assertEquals(("R", "Y", "R"), formation.get_colors())

        formation = Formation([(10, "G"), (9, "Y"), (8, "R")])
        self.assertEquals(("G", "Y", "R"), formation.get_colors())

    def test_can_get_max_number(self):
        formation = Formation([(1, "R"), (3, "Y"), (2, "R")])
        self.assertEquals(3, formation.get_max_number())

        formation = Formation([(10, "G"), (9, "Y"), (8, "R")])
        self.assertEquals(10, formation.get_max_number())


    def test_can_check_for_wedge(self):
        formation = Formation([(1, "R"), (2, "R"), (3, "R")])
        self.assertTrue(formation.is_wedge())

        formation = Formation([(10, "G"), (9, "G"), (8, "G")])
        self.assertTrue(formation.is_wedge())

    def test_missing_number_is_not_wedge(self):
        formation = Formation([(1, "R"), (4, "R"), (3, "R")])
        self.assertFalse(formation.is_wedge())

    def test_missing_color_is_not_wedge(self):
        formation = Formation([(1, "R"), (2, "R"), (3, "G")])
        self.assertFalse(formation.is_wedge())
