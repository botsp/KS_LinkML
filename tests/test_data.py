import os
import glob
import unittest
import yaml

from ks_linkml.datamodel.ks_linkml import Person

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            try:
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)
                entries = data.get('entries', [])
                for entry in entries:
                    person = Person(**entry)
                    assert person
            except ValueError as e:
                print(f"Error loading {path}: {e}")
                raise
            except Exception as e:
                print(f"Unexpected error loading {path}: {e}")
                raise

if __name__ == '__main__':
    unittest.main()