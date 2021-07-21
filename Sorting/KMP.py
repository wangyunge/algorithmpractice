def search(pat, txt):
    for i in range(len(txt)):
        for j in range(len(pat)):
            if pat[j] != txt[i+j]:
                break
            if j == len(pat)-1:
                return True
    return False
