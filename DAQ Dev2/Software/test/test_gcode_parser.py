import os
import sys
import unittest
import tempfile

# Add the scripts directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from gcode_parser import gcode_parser

class TestGCodeParser(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to simulate GCODE folder
        self.test_dir = tempfile.mkdtemp()

        # Temporarily modify the GCODE folder path for testing
        self.original_gcode_folder = os.path.join(os.path.dirname(__file__), '..', 'GCODE')
        os.makedirs(self.original_gcode_folder, exist_ok=True)

    def test_gcode_parser_with_comments_and_valid_commands(self):
        # Test content to write to the test GCODE file
        test_content = """G0 X10 Y10
                        M400
                        ;This is a comment
                        G0 X10 Y15"""

        # Create a test GCODE file
        test_filename = "test_gcode_file.gcode"
        test_filepath = os.path.join(self.original_gcode_folder, test_filename)
        
        try:
            with open(test_filepath, 'w') as f:
                f.write(test_content)

            # Call the gcode_parser function
            result = gcode_parser(test_filename)

            # Expected result
            expected_result = ["G0 X10 Y10", "M400", "G0 X10 Y15"]

            # Assert the parsed result matches expected result
            self.assertEqual(result, expected_result, 
                            "Parsed GCODE does not match expected output")

        finally:
            # Clean up the test file
            if os.path.exists(test_filepath):
                os.unlink(test_filepath)

    def test_gcode_parser_with_only_comments(self):
        # Test content with only comments
        test_content = """;First comment
        ;Second comment
        ;Third comment"""

        # Create a test GCODE file
        test_filename = "comments_only.gcode"
        test_filepath = os.path.join(self.original_gcode_folder, test_filename)
        
        try:
            with open(test_filepath, 'w') as f:
                f.write(test_content)

            # Call the gcode_parser function
            result = gcode_parser(test_filename)

            # Expected result should be an empty list
            self.assertEqual(result, [], 
                            "Parser should return an empty list for file with only comments")

        finally:
            # Clean up the test file
            if os.path.exists(test_filepath):
                os.unlink(test_filepath)

    def test_gcode_parser_empty_file(self):
        # Test with an empty file
        test_filename = "empty_file.gcode"
        test_filepath = os.path.join(self.original_gcode_folder, test_filename)
        
        try:
            # Create an empty file
            open(test_filepath, 'w').close()

            # Call the gcode_parser function
            result = gcode_parser(test_filename)

            # Expected result should be an empty list
            self.assertEqual(result, [], 
                            "Parser should return an empty list for empty file")

        finally:
            # Clean up the test file
            if os.path.exists(test_filepath):
                os.unlink(test_filepath)

    def test_gcode_parser_nonexistent_file(self):
        # Test with a nonexistent file
        test_filename = "nonexistent_file.gcode"

        # Call the gcode_parser function and expect None
        result = gcode_parser(test_filename)

        # Assert that the result is None
        self.assertIsNone(result, 
                        "Parser should return None for nonexistent file")

    def tearDown(self):
        # Remove the temporary GCODE directory if it exists
        if os.path.exists(self.original_gcode_folder):
            try:
                os.rmdir(self.original_gcode_folder)
            except OSError:
                # If directory is not empty or can't be removed, ignore
                pass
        
        # Clean up the temporary test directory
        if os.path.exists(self.test_dir):
            try:
                os.rmdir(self.test_dir)
            except OSError:
                pass

if __name__ == '__main__':
    unittest.main()