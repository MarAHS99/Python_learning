def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []

    def record():
        moves.append(f"{source} {auxiliary} {target}")

    def move(n, src, aux, tgt):
        if n == 1:
            tgt.append(src.pop())
            record()
            return
        move(n - 1, src, tgt, aux)
        tgt.append(src.pop())
        record()
        move(n - 1, aux, src, tgt)

    record()
    move(n, source, auxiliary, target)

    return "\n".join(moves)
