import numpy as np
import random

def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
    
    # try:
    torch.manual_seed(seed)
    # except
    
