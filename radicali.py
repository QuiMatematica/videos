import math

if __name__ == "__main__":
    a = [False] * 100
    for s in range(100):
        studente = s + 1
        for i in range(100):
            armadietto = i + 1
            if armadietto % studente == 0:
                a[i] = not a[i]
    for i in range(100):
        if a[i]:
            print(f"i={i+1}\tstato={a[i]}")
