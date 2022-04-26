# import json
import yaml
from collections import namedtuple


# class JsonLoader:
#     @staticmethod
#     def __metadata_encoder(src_dict: dict) -> namedtuple:
#         object_name = str.replace(next(iter(src_dict.keys())), 'mappingName',
#                                   'MappedDataSet')
#         return namedtuple(object_name, src_dict.keys())(*src_dict.values())

#     def load_from_file(file_path: str) -> namedtuple:
#         """
#         Extracts the JSON formatted contents of a metadata file to a NamedTuple.
#         Allowing for the use of dot notation in accessing properties.
#         NOTE: Assumes top level is a list. However also assumes there is only one.
#         That is, only returns the first one.

#         Args:
#             file_path (str): Filesystem path of JSON file.

#         Returns:
#             namedtuple:
#         """
#         try:
#             with open(file_path, 'r') as srcFile:
#                 srcObj = json.load(srcFile,
#                                    object_hook=JsonLoader.__metadata_encoder)

#         except Exception:
#             raise

#         return srcObj[0]


class YamlLoader:
    @staticmethod
    def __nested_dict_to_namedtuple(src_dict: dict) -> namedtuple:
        recursed_dict: dict = {}
        for key, value in src_dict.items():
            if isinstance(value, dict):
                recursed_dict[key] = YamlLoader.__nested_dict_to_namedtuple(
                    value)
            else:
                recursed_dict[key] = value
        return namedtuple('tuple',
                          recursed_dict.keys())(*recursed_dict.values())

    def load_from_file(file_path: str) -> namedtuple:
        """
        A generator which yields individual glossary entry contained within
        a YAML formatted glossary file, as a NamedTuple. Allowing for the use
        of dot notation in accessing properties.

        Args:
            file_path (str): Filesystem path of YAML file.

        Returns:
            namedtuple:
        """
        try:
            with open(file_path, 'r') as srcFile:
                srcObj = yaml.safe_load_all(srcFile)
                for glossary_entry in srcObj:
                    yield YamlLoader.__nested_dict_to_namedtuple(
                        glossary_entry)

        except Exception:
            raise
