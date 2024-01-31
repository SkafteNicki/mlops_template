import hydra
from omegaconf import DictConfig

def get_config(config_name: str, config_folder: str = "") -> DictConfig:
    """
    Loads a config file from the configs folder.

    Args:
        config_name (str): Name of the config file to load.
        config_folder (str): Name of the folder where the config file is located. Relative to the configs folder.

    Returns:
        OmegaConf: The loaded config file.
    """
    # with hydra.initialize(version_base=None, config_path="../../configs/pytest_config"):
    #     cfg = hydra.compose(config_name="test_values.yaml")

    with hydra.initialize(version_base=None, config_path=f"../../configs/{config_folder}"):
        cfg = hydra.compose(config_name=config_name)
    return cfg