import numpy as np
import random

def set_seed(seed: int) -> None:
    """
    Sets the random seed
    
    Parameters
    ----------
    seed: int
        The seed to set
    """
    np.random.seed(seed)
    random.seed(seed)
    
    # try:
    # torch.manual_seed(seed)
    # except
    
