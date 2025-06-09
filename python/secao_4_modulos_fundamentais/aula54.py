# DEQUE

from collections import deque

fila_correta: deque[int] = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(0)
fila_correta.appendleft(1)
fila_correta.appendleft(2)
print(fila_correta)
fila_correta.pop()
fila_correta.popleft()
print(fila_correta)
print(fila_correta[3])