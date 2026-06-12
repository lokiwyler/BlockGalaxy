# test_blockgalaxy.py
"""
Tests for BlockGalaxy module.
"""

import unittest
from blockgalaxy import BlockGalaxy

class TestBlockGalaxy(unittest.TestCase):
    """Test cases for BlockGalaxy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockGalaxy()
        self.assertIsInstance(instance, BlockGalaxy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockGalaxy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
