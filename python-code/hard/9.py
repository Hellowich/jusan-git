n = int(input())

def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Диск {n} с башни {source} переложить в башню {target}")
        hanoi(n - 1, auxiliary, target, source)

hanoi(n, 1, 3, 2)
