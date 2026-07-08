# >>
# >> words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# >> coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# >> Evaluator.zip_evaluate(coefs, words)
# 32.0
# >> words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
# >> coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# >> Evaluator.enumerate_evaluate(coefs, words)
# -1

class Evaluator:
    def __init__(self):
        return

    def zip_evaluate(coefs, words):
        total = 0
        table = zip(words, coefs)
        for element in table:
            total += (len(element[0]) * element[1])
        return total
        
    def enumerate_evaluate(coefs, words):
        total = 0
        table = list(enumerate(words))
        for index, word in enumerate(words):
            total += len(word) * coefs[index]
        return total