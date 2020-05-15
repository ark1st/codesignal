def commonCharacterCount(s1, s2):
    answer = 0
    for i in set(s1):
        if i in set(s2):
            num_s1 = s1.count(i)
            num_s2 = s2.count(i)           
            answer += min(num_s1,num_s2)

    return answer