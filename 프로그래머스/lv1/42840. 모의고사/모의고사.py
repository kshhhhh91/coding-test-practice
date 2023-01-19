def solution(answers):
  answer= []
  ans1 = [1, 2, 3, 4, 5] * 2000
  ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
  ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

  cor1 = []
  cor2 = []
  cor3 = []

  for i in range(len(answers)):
    if answers[i] == ans1[i]:
      cor1.append(ans1[i])
    if answers[i] == ans2[i]:
      cor2.append(ans2[i])
    if answers[i] == ans3[i]:
      cor3.append(ans3[i])

  if len(cor1)>=len(cor2) and len(cor1)>=len(cor3):
    answer.append(1)
  if len(cor2)>=len(cor1) and len(cor2)>=len(cor3):
    answer.append(2)
  if len(cor3)>=len(cor1) and len(cor3)>=len(cor2):
    answer.append(3)


  return answer