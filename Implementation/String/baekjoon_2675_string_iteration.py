t = int(input())
cmd = [input() for i in range(t)]   # 코딩 테스트 시 불필요한 문장
for i in range(t):
    r, s = cmd[i].split()
    for j in range(len(s)):
        print(s[j]*int(r), end='')
    print('')

# 코딩 테스트에서는 Input 은 그냥 주어진다.
# 따라서 cmd = [~~]와 같이 input 을 저장해놓을 필요는 없다.
