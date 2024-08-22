import unittest
from iterator_example import WordsCollection

class TestIterator(unittest.TestCase):

  def setUp(self):
    self.collection = WordsCollection(['A', 'B', 'C', 'D', 'E', 'F'])
  
  def test_simple_join(self):
    simple_collection = ''.join(self.collection)
    self.assertEqual(simple_collection, 'ABCDEF')
  
  def test_reverse_join(self):
    reverse_collection = ''.join(self.collection.get_custom_iterator(-1))
    self.assertEqual(reverse_collection, 'FEDCBA')
  
  def test_custom_join(self):
    custom_collection = ''.join(self.collection.get_custom_iterator(2))
    self.assertEqual(custom_collection, 'ACE')
  
  def test_custom_reverse_join(self):
    custom_reverse_collection = ''.join(self.collection.get_custom_iterator(-2))
    self.assertEqual(custom_reverse_collection, 'ECA')


if __name__ == "__main__":
  unittest.main()