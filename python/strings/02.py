Q- String Split and Join
def split_and_join(line):
    # write your code here
    split_line = line.split(" ")
    answer = "-".join(split_line)
    return answer

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
