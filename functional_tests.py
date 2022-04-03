import unittest

import pytest
from playwright.sync_api import Page


class NewVisitorTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        self.page = page

    def test_can_start_a_list_and_retrieve_it_late(self):
        self.page.goto('http://localhost:8000')
        self.assertIn('To-Do', self.page.title())
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')