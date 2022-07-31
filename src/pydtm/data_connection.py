"""
Loads details for connecting to known data stores.
"""
from collections import namedtuple
# from contextlib import contextmanager
# import json
import yaml
from pydtm.file_loader import nested_dict_to_namedtuple


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
#             with open(file_path, 'r', encoding="utf8") as srcFile:
#                 srcObj = json.load(srcFile,
#                                    object_hook=JsonLoader.__metadata_encoder)

#         except Exception:
#             raise

#         return srcObj[0]


# class YamlLoader:
#     """_summary_

#     Returns:
#         _type_: _description_
#     """

    # @staticmethod
def load_from_file(file_path: str) -> namedtuple:
    """
    Extracts the YAML formatted contents of a metadata file to a dictionary
    of NamedTuples. Allowing for the use of dot notation in accessing
    properties.
    NOTE: There can be multiple documents/connections in the loaded YAML
    file. Each is added as a keyed entry in the returned object. Using the
    key from the serialised connection object as the key in the
    NamedTuple.

    Args:
        file_path (str): Filesystem path of YAML file.

    Returns:
        namedtuple:
    """
    result_dict: dict = {}
    with open(file_path, 'r', encoding='utf8') as src_file:
        src_obj = yaml.safe_load_all(src_file)
        for conn in src_obj:
            n_tuple = nested_dict_to_namedtuple(conn)
            result_dict[n_tuple.metadata.name] = n_tuple
    return result_dict




# @contextmanager
# def data_connections_open(file_path):
#     f = open(file_path, 'r', encoding="utf8")
#     try:
#         yield f
#     finally:
#         f.close()

# # example usage
# with data_connections_open('file') as f:
#     contents = f.read()
