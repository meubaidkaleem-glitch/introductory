import unittest

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from introductory import build_message


class BuildMessageTests(unittest.TestCase):
    def test_default_message_has_project_mission(self):
        message = build_message()
        self.assertIn("INTRODUCTORY.exe", message)
        self.assertIn("well-organized repository", message)

    def test_custom_name_is_used(self):
        self.assertTrue(build_message("Tiny Chaos").startswith("Tiny Chaos"))


if __name__ == "__main__":
    unittest.main()
