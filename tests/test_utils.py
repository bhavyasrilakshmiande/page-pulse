import unittest
from utils import (
    parse_html,
    get_page_title,
    get_meta_description,
    count_h1_tags,
    count_images_missing_alt,
    count_visible_words,
)


class TestParsingLogic(unittest.TestCase):

    # Happy Path
    def test_valid_html(self):
        html = """
        <html>
            <head>
                <title>Test Page</title>
                <meta name="description" content="Sample Description">
            </head>
            <body>
                <h1>Heading 1</h1>
                <img src="image1.jpg">
                <img src="image2.jpg" alt="Sample Image">
                <p>Hello World from Page Pulse</p>
            </body>
        </html>
        """

        soup = parse_html(html)

        self.assertEqual(get_page_title(soup), "Test Page")
        self.assertEqual(get_meta_description(soup), "Sample Description")
        self.assertEqual(count_h1_tags(soup), 1)
        self.assertEqual(count_images_missing_alt(soup), 1)
        self.assertGreater(count_visible_words(soup), 0)

    # Failure Case 1
    def test_empty_html(self):
        soup = parse_html("")

        self.assertIsNone(get_page_title(soup))
        self.assertIsNone(get_meta_description(soup))
        self.assertEqual(count_h1_tags(soup), 0)
        self.assertEqual(count_images_missing_alt(soup), 0)
        self.assertEqual(count_visible_words(soup), 0)

    # Failure Case 2
    def test_html_without_meta_and_h1(self):
        html = """
        <html>
            <body>
                <p>Only paragraph exists.</p>
            </body>
        </html>
        """

        soup = parse_html(html)

        self.assertIsNone(get_meta_description(soup))
        self.assertEqual(count_h1_tags(soup), 0)
        self.assertEqual(count_images_missing_alt(soup), 0)


if __name__ == "__main__":
    unittest.main()