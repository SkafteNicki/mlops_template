import hydra


class Trainer:
    @hydra.main(config_path = "../configs", config_name = "config")
    def __init__(self, cfg):
        self.config = cfg.train_config
        raise NotImplementedError