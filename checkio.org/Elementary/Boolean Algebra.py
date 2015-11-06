#!/usr/bin/env python3

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation=="conjunction":
        return 1 if (x==1 and y==1) else 0
    if operation=="disjunction":
        return 1 if (x==1 or y==1) else 0
    if operation=="implication":
        return 0 if (x==1 and y==0) else 1
    if operation=="exclusive":
        return 1 if ((x==1 and y==0)or(x==0 and y==1)) else 0
    if operation=="equivalence":
        return 1 if x==y else 0



    return 1 or 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Progr Begin')
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('Progr End')

"""
В математике и математической логике, Булева алгебра это подраздел алгебры в котором значения переменных истинны или ложны и обычно обозначенны 0 или 1 соответственно. В отличии от простой алгебры где значение переменных это числа и основные операции это сложение и умножение, основные операции Булевой алегбры это конъюнкция (обозначенная ∧), дизъюнкция (обозначенная ∨) и отрицание (обозначенное ¬).
В этой миссии вам нужно реализовать несколько булевых операций:
- "конъюнкция" ("conjunction") обозначенная x ∧ y, удовлетворяющая условиям x ∧ y = 1 если x = y = 1 и  ∧ y = 0 иначе.
- "дизъюнкция" ("disjunction") обозначенная x ∨ y, удовлетворяющая условиям x ∨ y = 0 если x = y = 0 и x ∨ y = 1 иначе.
- "импликация" ("implication") (прямая импликация) обозначенная x→y и описанная как ¬ x ∨ y. Если x это истина, тогда значение x → y берется такое как у y. Но если x ложь, тогда значение y может быть игнорированно.
- "исключение" ("exclusive") (исключающее ИЛИ) обозначенное x ⊕ y и описанное как (x ∨ y)∧ ¬ (x ∧ y). Это исключает вероятность обоих x и y. В терминах арифметики, это сложение по модулю 2, где 1 + 1 = 0.
- "эквивалентность" ("equivalence") обозначенная x ≡ y и описанная как ¬ (x ⊕ y). Это истина, когда x и y имеют одинаковые значения.
Здесь вы можете увидеть таблицу истинности для данных операций:
 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
Даны два булевых значения x и y как 1 или 0 и дано имя операции, как описано ранее. Вы должны вычислить значение и вернуть его как 1 или 0.
Входные значения: Три аргумента. X и Y как 0 или 1. Имя операции, как строка.
Выходное значение: Результат как 1 или 0.
Предусловие: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
"""