import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Test Heading
"""
        heading = extract_title(md)
        self.assertEqual(heading, "Test Heading")
    
    def test_extract_title_error(self):
        md = """
## Test Heading
"""
        try:
            extract_title(md)
        except Exception as e:
            # Check if the correct exception was raised with the correct message
            self.assertEqual(str(e), "file missing <h1> header")
        else:
            # If no exception was raised, fail the test
            self.fail("Expected exception not raised")

    def test_extract_title_many(self):
        md = """
# Test Heading

# Another Heading

# A Third Heading
"""
        heading = extract_title(md)
        self.assertEqual(heading, "Test Heading")