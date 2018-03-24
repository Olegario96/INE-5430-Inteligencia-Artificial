import pytest

from gomoku.model import Piece
from gomoku.model import Player
from gomoku.model import Position
from random import randrange

@pytest.fixture(scope='session')
def position():
  position = Position(randrange(15), randrange(15))
  return position

def test_get_row(position):
  i = position.get_row()
  if 0 <= i <= 14:
    assert True
  else:
    assert False

def test_get_column(position):
  j = position.get_column()
  if 0 <= j <= 14:
    assert True
  else:
    assert False

def test_initialize_piece(position):
  assert position.piece == None

def test_is_empty(position):
  assert position.is_empty

def test_get_player_without_piece(position):
  assert position.get_player_from_position() == None

def test_set_piece(position):
  player = Player('X')
  piece = Piece(player, position)
  position.set_piece(piece)
  assert position.piece == piece

def test_get_player_with_piece(position):
  player = Player('X')
  piece = Piece(player, position)
  position.set_piece(piece)
  assert position.get_player_from_position() == player

def test_clear(position):
  position.clear()
  assert position.piece == None

if __name__ == '__main__':
  import doctest
  doctest.testmod()

