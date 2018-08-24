from functools import reduce

print(*reduce(lambda x, y:
             map(lambda x, y: int(x) ^ int(y), x, y),
                 (map(lambda x:
                      input().split(),
                      range(int(input()))
                      )
                  )
                 )
             )
