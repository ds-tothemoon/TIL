def solution(phone_book):
    phone_book_sorted = sorted(phone_book)
    answer = True
    for i in range(len(phone_book_sorted)-1):
        tmp1 = phone_book_sorted[i]
        tmp2 = phone_book_sorted[i+1]
        if tmp1 == tmp2[:len(tmp1)]:
            answer = False
    return answer

import unittest
import inspect
class TestCase(unittest.TestCase):
    def test_solution(self):
        assert solution([12,123,112,1235,567,88]) == False
        assert solution([123,456,789]) == True
        print(f'{inspect.stack()[0][3]}() is pass')

if '__name__'=='__main__':
    print('test')
    unittest.main()
