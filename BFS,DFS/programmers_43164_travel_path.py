answer = []


def dfs(ticket_dict, cur, depth, max_depth, path):
    global answer
    if depth == max_depth:
        answer = path
        return True

    if cur not in ticket_dict:
        return False

    for i in range(len(ticket_dict[cur])):
        nxt, visited = ticket_dict[cur][i]
        if visited:
            continue
        ticket_dict[cur][i][1] = 1
        path.append(nxt)
        if dfs(ticket_dict, nxt, depth + 1, max_depth, path):
            return True
        ticket_dict[cur][i][1] = 0
        path.pop()
    return False


def solution(tickets):
    ticket_dict = dict()
    for frm, to in tickets:
        if frm in ticket_dict:
            ticket_dict[frm].append([to, 0])
        else:
            ticket_dict[frm] = [[to, 0]]
    for _, value in ticket_dict.items():
        value.sort()

    path = []
    path.append("ICN")
    dfs(ticket_dict, "ICN", 0, len(tickets), path)

    return answer