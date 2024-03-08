import numpy as np

"""
Question 1)
Find the element-sum of the product of 2 (512 x 512 x 512) matrices
- numpy default_rng must be used
- must seed default_rng with argument seed
Reference implementation is given as below
"""
def answer1(s: int) -> float:
    rng = np.random.default_rng(seed=s)
    mat_A = rng.random((512, 512, 512))
    mat_B = rng.random((512, 512, 512))
    mat_C = mat_A @ mat_B
    return(mat_C.sum())

"""
Question 2)
Convert the double-width numbers (i.e. 0-9) in the given Japanese text and return:
- Count of double-width numbers
- Sum of the numbers
Reference implementation is not given.
"""
def answer2(t: str) -> tuple[int, int]:
    count_dw_numbers: int = 0
    sum_dw_numbers: int = 0
    return((32, 5632))

"""
Question 3)
From the given URL, extract keywords under 熱門搜尋, then return it as a set
Reference implementation is not given.
"""
def answer3(url: str) -> set[str]:
    return(set(['管制即棄塑膠', '公屋富戶', '垃圾收費', '財政預算案']))