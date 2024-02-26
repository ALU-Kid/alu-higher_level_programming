def test_code():
    word = "Holberton"
    word_first_3 = word[:3]
    word_last_2 = word[-2:]
    middle_word = word[1:-1]
    
    assert word_first_3 == "Hol"
    assert word_last_2 == "on"
    assert middle_word == "olberto"
    
    print("All test cases passed!")

test_code()