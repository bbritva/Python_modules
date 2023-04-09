from termcolor import cprint


class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or \
                not isinstance(words, list) or \
                len(coefs) != len(words):
            return -1
        result = 0
        arr = zip(coefs, words)
        for tupl in arr:
            if not isinstance(tupl[0], float) or \
                    not isinstance(tupl[1], str):
                return -1
            result += tupl[0] * len(tupl[1])
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or \
                not isinstance(words, list) or \
                len(coefs) != len(words):
            return -1
        result = 0
        for i, word in enumerate(words):
            if not isinstance(coefs[i], float) or \
                    not isinstance(word, str):
                return -1
            result += coefs[i] * len(word)
        return result



def test(coefs, words):
    """A function to test the Evaluator class"""
    cprint("Test case:", "green")
    print("words =", words)
    print("coefs =", coefs)
    cprint("Results:", "green")
    print("zip result :      ", Evaluator().zip_evaluate(coefs, words)) # call from instance
    print("enumerate result :", Evaluator.zip_evaluate(coefs, words)) # call without instance
    print()


if __name__ == '__main__':
    test([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"])
    test([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem",
         "Ipsum", "n'", "est", "pas", "simple"])
    test([1.0, 2.0, "1.0", 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"])
    test([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", 44, "est", "simple"])
    test([1.0, 2.0, 1.0, 4.0, 0.5, 11.0], [
         "Le", "Lorem", "Ipsum", "est", "tres", "simple"])
    test([1.0], ["simple"])
    test([1.0, 2.0], ["tres", "simple"])
