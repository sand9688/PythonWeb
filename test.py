

number = "1231234"
k = 3

answer = sorted(number)
print(answer)
answer.sort(reverse=True)
print(answer)
answer = answer[0:len(number)-k]
print(answer)