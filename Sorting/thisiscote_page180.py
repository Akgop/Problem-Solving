import sys


def solution(students):
    students.sort(key=lambda x: x[1])
    answer = ''
    for student in students:
        answer += student[0]
        answer += ' '
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list()
    for _ in range(N):
        name, score = sys.stdin.readline().rstrip().split()
        li.append([name, int(score)])
    print(solution(li))
