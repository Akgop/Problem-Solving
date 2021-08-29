def solution(table, languages, preference):
    jobs = dict()
    score = [0] * 5
    points = [dict() for _ in range(5)]
    for i in range(len(table)):
        job, lang1, lang2, lang3, lang4, lang5 = table[i].split()
        jobs[i] = job
        points[i][lang1] = 5
        points[i][lang2] = 4
        points[i][lang3] = 3
        points[i][lang4] = 2
        points[i][lang5] = 1
    for i in range(len(languages)):
        for j in range(5):
            if languages[i] in points[j]:
                score[j] += preference[i]*points[j][languages[i]]
    answer = jobs[0]
    MAX = score[0]
    for i in range(len(score)):
        if score[i] == MAX:
            answer = min(jobs[i], answer)
        elif score[i] > MAX:
            MAX = score[i]
            answer = jobs[i]
    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5],
               )
      )

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"],
               [7, 5],
               )
      )