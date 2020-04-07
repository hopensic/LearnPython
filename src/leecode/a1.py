if __name__ == '__main__':
    student_marks = {}
    for _ in range(1):
        name, *line = "aa 12 34 55".split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = 'aa'
    lst = student_marks[query_name]
    print("%.2f" % (sum(lst)/len(lst)))