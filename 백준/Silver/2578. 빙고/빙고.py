bingo_board = []
for _ in range(10):
    line = input().split()
    line = list(map(int, line))
    bingo_board.append(line)

# 5x5 형식의 빙고판을 1차원 리스트로 변환합니다.
numbers = [num for row in bingo_board for num in row]

result = [False] * 25

if len(numbers) != 50:
    print("50개의 숫자를 정확히 입력해주세요.")
else:
    ARR_1 = numbers[:25]
    ARR_2 = numbers[25:]


DICT = {}
for i in range(25):
  DICT[ARR_1[i]] = i

def func(arr):
  total = 0

  # 가로줄 체크
  for i in range(5):
      row_bingo = True
      for j in range(5):
          if arr[i * 5 + j] == False:
              row_bingo = False
              break
      if row_bingo:
          total += 1

  # 세로줄 체크
  for i in range(5):
      col_bingo = True
      for j in range(5):
          if arr[i + 5 * j] == False:
              col_bingo = False
              break
      if col_bingo:
          total += 1
  #대각선 체크
  dae_1_bingo = True
  for i in range(5):
    if arr[i + 5 * i] == False:
      dae_1_bingo = False
      break
  if dae_1_bingo:
    total += 1

  dae_2_bingo = True
  for i in range(4,21,4):
    if arr[i] == False:
      dae_2_bingo = False
      break
  if dae_2_bingo:
    total += 1

  return total

for i in range(25):
  result[DICT[ARR_2[i]]] = True

  if (func(result) >=3):
    print(i + 1)
    break
