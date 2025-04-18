import unittest
from unittest.mock import patch
import os
from music21 import *
from .music import musicxml_writer, create_musicxml
from . import ver1, ver2, ver4
from pathlib import Path

class TestMusicXMLWriter(unittest.TestCase):
    def setUp(self):
        # Setup any test prerequisites
        self.test_output = "test_output.xml"
        self.input_text = "test"
        
    def tearDown(self):
        # Cleanup after tests
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    @patch('builtins.input', side_effect=['N', 'N'])  
    def test_basic_output_creation(self, mock_input):
        """Test that output file is created"""
        musicxml_writer(self.input_text)
        self.assertTrue(os.path.exists("output.xml"))

    @patch('builtins.input', side_effect=['N', 'N'])
    def test_ver1_integration(self, mock_input):
        """Test integration with version 1"""
        test_input = "ABC"
        p, r = ver1.version_1(test_input)
        musicxml_writer(test_input)
        self.assertTrue(os.path.exists("output.xml"))
        
    @patch('builtins.input', side_effect=['N', 'N'])
    def test_ver2_integration(self, mock_input):
        """Test integration with version 2"""
        test_input = "ABC" 
        p, r = ver2.version_2(test_input)
        musicxml_writer(test_input)
        self.assertTrue(os.path.exists("output.xml"))

    @patch('builtins.input', side_effect=['N', 'N'])
    def test_ver4_integration(self, mock_input):
        """Test integration with version 4"""
        test_input = "ABC"
        p, r = ver4.version_4(test_input)
        musicxml_writer(test_input)
        self.assertTrue(os.path.exists("output.xml"))

    @patch('builtins.input', side_effect=['N', 'N'])
    def test_output_format(self, mock_input):
        """Test output file format validity"""
        musicxml_writer(self.input_text)
        
        # Try parsing output with music21
        try:
            score = converter.parse("output.xml")
            self.assertIsInstance(score, stream.Score)
        except Exception as e:
            self.fail(f"Failed to parse output file: {e}")

    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_reader_yes_path(self, mock_input):
        """Test behavior when user has reader"""
        with patch('music21.stream.Score.show') as mock_show:
            musicxml_writer(self.input_text)
            mock_show.assert_called_once()

    @patch('builtins.input', side_effect=['N', 'N'])
    def test_reader_no_path(self, mock_input):
        """Test behavior when user has no reader"""
        with patch('music21.stream.Score.show') as mock_show:
            musicxml_writer(self.input_text)
            mock_show.assert_not_called()

    def test_create_musicxml_rhythm_mapping(self):
        """Test rhythm mapping in create_musicxml"""
        test_pitches = "C4 D4 E4"
        test_rhythms = "q h w"
        with patch('builtins.input', side_effect=['N', 'N']):
            create_musicxml(test_pitches, test_rhythms, self.test_output)
            score = converter.parse(self.test_output)
            notes = list(score.flatten().getElementsByClass('Note'))
            self.assertEqual(len(notes), 3)
            self.assertEqual(notes[0].quarterLength, 1.0)  # quarter note
            self.assertEqual(notes[1].quarterLength, 2.0)  # half note
            self.assertEqual(notes[2].quarterLength, 4.0)  # whole note

    def test_verbose_output(self):
        """Test verbose output option"""
        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=['N', 'N']):
                musicxml_writer(self.input_text, verbose=True)
                mock_print.assert_any_call("MusicXML file created: output.xml")

if __name__ == '__main__':
    unittest.main()