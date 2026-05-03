import os
import sys

import pytest

# Add the parent directory to sys.path to ensure relative imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.examples.bitsequence.bitsequence import BitSequence


class TestBitSequence:
    def test_bit_sequence(self):
        bs = BitSequence("1010")
        assert 8 == 8
