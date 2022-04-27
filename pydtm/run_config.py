from collections import namedtuple
import yaml
from .dict_utils import nested_dict_to_namedtuple


# class YamlLoader:
#     """_summary_

#     Returns:
#         _type_: _description_
#     """

#     @staticmethod
def from_file(file_path: str) -> namedtuple:
    """
    Returns a run config as a NamedTuples. Which allows for the use of dot
    notation in accessing properties.
    NOTE: For now assuming never multiple documents, and will only ever
    return the first run_conf.

    Args:
        file_path (str): Filesystem path of YAML file.

    Returns:
        tuple: The loaded run_conf as a named tuple.
    """
    with open(file_path, 'r', encoding='utf8') as src_file:
        run_conf = yaml.safe_load(src_file)
        return nested_dict_to_namedtuple(run_conf)

    # @staticmethod
def to_file(run_conf: dict, file_path: str) -> None:
    """
    Persists a run_conf to file. Replacing any existing content.

    Args:
        tuple: The loaded run_conf as a named tuple.
        file_path (str): Filesystem path of YAML file.
    """
    with open(file_path, 'w', encoding='utf8') as dest_file:
        yaml.safe_dump(run_conf, dest_file)
        # yaml.dump(run_conf, destFile)
