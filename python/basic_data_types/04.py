Q- Nested Lists
if __name__ == '__main__':
    score_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    second_highest = sorted(list(set([marks for name, marks in score_list])))[1]
    print('\n'.join([name for name,score in sorted(score_list) if score == second_highest]))
