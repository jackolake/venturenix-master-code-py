import numpy as np

def answer1(n: int) -> np.ndarray:
    return(np.random.randint(1, 9999, size=(512, 512, 512), dtype=np.uint16))

def answer2(n: int) -> np.ndarray:
    return(np.ones((512, 512, 512, n), dtype=np.uint16))

def answer3(n: int) -> np.ndarray:
    return(np.ones((256, 256, 256, n), dtype=np.uint16))