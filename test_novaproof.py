# test_novaproof.py
"""
Tests for NovaProof module.
"""

import unittest
from novaproof import NovaProof

class TestNovaProof(unittest.TestCase):
    """Test cases for NovaProof class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaProof()
        self.assertIsInstance(instance, NovaProof)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaProof()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
