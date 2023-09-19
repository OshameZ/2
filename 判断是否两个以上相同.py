S = input('输入一个字符串：')
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        print('Yes')