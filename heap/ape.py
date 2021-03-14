from heapq import nlargest

def first_recurring_char(st):
    s = list(st)
    dic = {s[i]:0 for i in range(0,len(s))}
    for i in range(0, len(s)):
        dic[s[i]] += 1

    if len(s) <= len(set(s)):
        return None
    else:
        return nlargest(1, dic, key = dic.get)[0]
    

if __name__ == "__main__":
    
    # ABCA -> A
    # BCABA -> B
    # DBCABA -> B
    # ABC -> None
    print(first_recurring_char("DBCABA"))