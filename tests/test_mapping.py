import pytest
from pydtm import mapping
# from pydtm.plugins.data_asserts import DataAssert
from pydtm.utils.generate_metadata import GenMetadata

def test_load():
    """test
    """
    data_mapping = mapping.load_from_file(
        R'C:\Users\scott\dev\pydtm-lib\tests\resources\test_mapping.yaml')
    print(data_mapping.metadata.name, 'is a', data_mapping.api_version,
          data_mapping.kind)


@pytest.mark.skip
def test_assert():
    """test
    """
    GenMetadata()
    # td = DataAssert()
    # td.to_do('test')
