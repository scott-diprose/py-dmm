from pydtm import mapping

data_mapping = mapping.load_from_file(R'C:\Users\scott\dev\pydtm-lib\tests\resources\mapping.yaml')
print(data_mapping.metadata.name)
