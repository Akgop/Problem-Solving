import sys


def get_l1_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def recur(dist, depth, customers, max_depth, home, visited, cur):
    global answers
    if depth == max_depth - 1:
        new_dist = dist + get_l1_distance(customers[cur][0], home[0], customers[cur][1], home[1])
        answers.append(new_dist)
        return
    for i in range(max_depth):
        if not visited[i]:
            visited[i] = True
            new_dist = dist + get_l1_distance(customers[cur][0], customers[i][0], customers[cur][1], customers[i][1])
            recur(new_dist, depth+1, customers, max_depth, home, visited, i)
            visited[i] = False


def solution(n):
    company, home, tmp = coord[0:2], coord[2:4], coord[4:]
    customers = []
    for i in range(0, len(tmp), 2):
        customers.append(tmp[i:i+2])
    visited = [False] * (len(customers))
    dist = 0
    global answers
    for i in range(len(customers)):
        visited[i] = True
        new_dist = dist + get_l1_distance(company[0], customers[i][0], company[1], customers[i][1])
        recur(new_dist, 0, customers, n, home, visited, i)
        visited[i] = False


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for test_case in range(T):
        answers = []
        N = int(sys.stdin.readline().rstrip())
        coord = list(map(int, sys.stdin.readline().rstrip().split()))
        solution(N)
        print("#{t} {result}".format(t=test_case, result=min(answers)))
