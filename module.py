import numpy as np

"""
Question 1)
Find the element-sum of the product of 2 (512 x 512 x 512) matrices
- numpy default_rng must be used
- must seed default_rng with argument seed
"""
def answer1(s: int) -> float:
    rng = np.random.default_rng(seed=s)
    mat_A = rng.random((512, 512, 512))
    mat_B = rng.random((512, 512, 512))
    mat_C = mat_A @ mat_B
    return(mat_C.sum())

def answer2(n: int) -> np.ndarray:
    return(np.ones((512, 512, 512, n), dtype=np.uint16))

def answer3(n: int) -> np.ndarray:
    return(np.ones((256, 256, 256, n), dtype=np.uint16))