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
    # return (mat_A @ mat_B).sum()
    return np.sum(np.matmul(mat_A, mat_B))
    

"""
Question 2)
Convert the double-width numbers (i.e. 0-9) in the given Japanese text and return:
- Count of double-width numbers
- Sum of the numbers
Reference implementation is not given.
"""
def answer2(t: str) -> tuple[int, int]:
    count_dw_numbers: int = 32
    sum_dw_numbers: int = 5632
    import re
    u_list = re.findall('[０-９]+', t.decode('utf-8'))
    num_list = [int(''.join([str(ord(digit)-ord('０')) for digit in digits]))
                for digits in u_list]
    count_dw_numbers, sum_dw_numbers = len(num_list), sum(num_list)
    return((count_dw_numbers, sum_dw_numbers))

"""
Question 3)
From the given URL, extract keywords under 熱門搜尋, then return it as a set
Reference implementation is not given.
"""
def answer3(url: str) -> set[str]:
    import requests
    from bs4 import BeautifulSoup
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    search_tag = soup.find('div', {'class': 'hotSearch'})
    # return(set(['管制即棄塑膠', '公屋富戶', '垃圾收費', '財政預算案']))
    return set([tag.text for tag in search_tag.find_all('a')])