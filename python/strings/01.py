Q- Swap Cases
def swap_case(s):
    answer = ""
    for letter in s:
        if letter.islower():
            answer += letter.upper()
        elif letter.isupper():
            answer += letter.lower()
        else:
            answer += letter
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
