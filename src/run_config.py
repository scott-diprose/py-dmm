import yaml
from collections import namedtuple


class YamlLoader:
    @staticmethod
    def __nested_dict_to_namedtuple(src_dict: dict) -> tuple:
        recursed_dict: dict = {}
        for key, value in src_dict.items():
            if isinstance(value, dict):
                recursed_dict[key] = YamlLoader.__nested_dict_to_namedtuple(
                    value)
            else:
                recursed_dict[key] = value
        return namedtuple('tuple',
                          recursed_dict.keys())(*recursed_dict.values())

    def from_file(file_path: str) -> tuple:
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
        with open(file_path, 'r', encoding="utf8") as srcFile:
            run_conf = yaml.safe_load(srcFile)
            return YamlLoader.__nested_dict_to_namedtuple(run_conf)

    def to_file(run_conf: dict, file_path: str) -> None:
        """
        Persists a run_conf to file. Replacing any existing content.

        Args:
            tuple: The loaded run_conf as a named tuple.
            file_path (str): Filesystem path of YAML file.
        """
        with open(file_path, 'w', encoding="utf8") as destFile:
            yaml.safe_dump(run_conf, destFile)
            # yaml.dump(run_conf, destFile)
