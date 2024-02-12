info = {
  'one' : 1,
  'two' : 2,
  'three': 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9,
  'zero' : 0
 }

def solution(s):
    word_list = ''
    num_list = ''
    for i in s: # o, n, e, 4, s, e, v, e, n, ~~~
        if i.isalpha():
            word_list += i 
            if word_list in info:
                num_list += str(info[word_list])
                word_list = ''
        else:
            num_list += i
    return int(num_list)
print(solution("one4seveneight"))