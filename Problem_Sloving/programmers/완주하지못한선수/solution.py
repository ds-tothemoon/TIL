def solution(participant, completion):
    participant_sorted = sorted(participant)
    completion_sorted = sorted(completion)
    result = ""
    for i in range(len(completion_sorted)):
        if completion_sorted[i] != participant_sorted[i]:
            result = participant_sorted[i]    
            break

    if result == "":
        result = participant_sorted[len(participant_sorted)-1]
    
    return result


import unittest
import inspect
class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_solution(self):
        assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
        assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"
        
        print(f'{inspect.stack()[0][3]}() is pass')

if __name__ == "__main__":
    unittest.main()