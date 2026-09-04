# test_vibeomen.py
"""
Tests for VibeOmen module.
"""

import unittest
from vibeomen import VibeOmen

class TestVibeOmen(unittest.TestCase):
    """Test cases for VibeOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VibeOmen()
        self.assertIsInstance(instance, VibeOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VibeOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
