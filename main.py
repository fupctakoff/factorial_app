import threading

class Fact:
    # Переменные для сохранения результата выолненных тредов
    res_of_fact1 = 0
    res_of_fact2 = 0
    
    def fact_validator(func):
        def inner(self, n):
            """Валидация вхродящих и выходящих данных"""
            if not isinstance(n, int):
                return 'Вам необходимо ввести цифру или целое число'
            elif n >= 1559 or n <= -1559:
                return 'Слишком большое число'
            elif n == -1:
                result = -1
            elif n > 1000 or n < -1000:
                result = f"Первые 5 цифр полученного числа: {str(abs(func(self, n)))[:5]}"
            else:
                result = func(self, n)
            return result
        return inner

    
    def fact1(self, n: int) -> int:
        """Нахождение первой половины факториала для треда"""
        pr = 1
        for i in range(1, abs(n)//2+1):
            pr *=i
        self.res_of_fact1 = pr

    def fact2(self, n: int) -> int:
        """Нахождение второй половины факториала для треда"""
        pr = 1
        for i in range(abs(n)//2+1, abs(n)+1):
            pr *=i
        self.res_of_fact2 = pr
    
    
    @fact_validator
    def calc_factorial(self, n: int) -> int | str:
        """Основная исполняемая функция, в которой создаются треды и формируется окончательный ответ"""
        thread1 = threading.Thread(target=self.fact1, args=(abs(n), ))
        thread2 = threading.Thread(target=self.fact2, args=(abs(n), ))
        thread1.start()
        thread2.start()
        if n % 2 != 0 and n < 0:
            return self.res_of_fact1 * self.res_of_fact2 * -1
        return self.res_of_fact1 * self.res_of_fact2

ex = Fact()

print(
    ex.calc_factorial(1558)
)