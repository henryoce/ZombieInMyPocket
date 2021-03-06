import doctest

from cards.card_tests.card_tests import CardTestCases
from game_tests.game_tests import GameTestCases
from items.item_tests.item_tests import ItemTestCases
from pickle_manager_tests.pickle_manager_tests import PickleManagerTestCases
from tiles.tile_tests.tile_tests import TileTestCases
from level.level_tests.level_tests import LevelTestCases

if __name__ == '__main__':
    CardTestCases()
    ItemTestCases()
    TileTestCases()
    LevelTestCases()
    GameTestCases()
    PickleManagerTestCases()
    doctest.testmod()
