from collections import deque

def fPalinCheck(dataset, max_len):
    strPalin = deque(maxlen=max_len)
    strPalin.extend(dataset)
    chkPalin = True
    while len(strPalin) > 1:
        if strPalin.pop() != strPalin.popleft():
            chkPalin = False
    return chkPalin

def main():
    max_len = 7
    dataset = ["t","a","c","o","c","a","a"]
    print(fPalinCheck(dataset, max_len))
    return
if __name__ == "__main__":
    main()