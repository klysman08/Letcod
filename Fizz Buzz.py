class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lista = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                lista.append("FizzBuzz")
            elif i % 3 == 0:
                lista.append("Fizz")
            elif i % 5 == 0:
                lista.append("Buzz")
            else:
                lista.append(str(i))
        return lista

#test for n = 15
n = 15
fizzbuzz = Solution()
print(fizzbuzz.fizzBuzz(n))

