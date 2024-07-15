from fractions import Fraction
import itertools

def primes():
    """ Generate an infinite sequence of prime numbers. """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def fibonacci():
    """ Generate an infinite sequence of Fibonacci numbers. """
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

class SequenceGenerator:
    def __init__(self, start, rule, length=10):
        self.start = start
        self.rule = rule
        self.length = length
        self.sequence = []
        self.generate_sequence()

    def generate_sequence(self):
        if self.rule == 'add_primes':
            self.sequence = self._add_primes()
        elif self.rule == 'geometric_diff':
            self.sequence = self._geometric_diff()
        elif self.rule == 'increasing_difference':
            self.sequence = self._increasing_difference()
        elif self.rule == 'skip_primes':
            self.sequence = self._skip_primes()
        elif self.rule == 'fibonacci_diff':
            self.sequence = self._fibonacci_diff()
        elif self.rule == 'recurrence_relation':
            self.sequence = self._recurrence_relation()
        elif self.rule == 'fraction_pattern':
            self.sequence = self._fraction_pattern()
        elif self.rule == 'integer_fraction_pattern':
            self.sequence = self._integer_fraction_pattern()
        elif self.rule == 'fibonacci_fractions':
            self.sequence = self._fibonacci_fractions()
        elif self.rule == 'separate_patterns':
            self.sequence = self._separate_patterns()
        else:
            raise ValueError(f"Unknown rule: {self.rule}")

    def _add_primes(self):
        prime_gen = primes()
        sequence = [self.start]
        next(prime_gen)  # Skip the first prime number 2 if starting with 6
        for _ in range(1, self.length):
            next_val = sequence[-1] + next(prime_gen)
            sequence.append(next_val)
        return sequence

    def _geometric_diff(self):
        sequence = [self.start]
        diff = 11
        for _ in range(1, self.length):
            next_val = sequence[-1] + diff
            sequence.append(next_val)
            diff *= 3
        return sequence

    def _increasing_difference(self):
        sequence = [self.start]
        diff = 19
        for _ in range(1, self.length):
            next_val = sequence[-1] + diff
            sequence.append(next_val)
            diff += 6
        return sequence

    def _skip_primes(self):
        prime_gen = primes()
        primes_list = [p for p, _ in zip(prime_gen, range(self.length * 2))]
        sequence = [primes_list[i] for i in range(len(primes_list)) if i % 2 == 0]
        return sequence[:self.length]

    def _fibonacci_diff(self):
        fib_gen = fibonacci()
        diffs = [next(fib_gen) for _ in range(self.length)]
        sequence = [self.start]
        for diff in diffs:
            sequence.append(sequence[-1] + diff)
        return sequence

    def _recurrence_relation(self):
        sequence = [5, 10]
        for _ in range(2, self.length):
            next_val = 5 * sequence[-1] + sequence[-2]
            sequence.append(next_val)
        return sequence

    def _fraction_pattern(self):
        numerators = [1, 7, 9, 11, 15, 19]
        denominators = [7, 9, 11, 15, 19, 27]
        sequence = [f"{n}/{d}" for n, d in zip(numerators, denominators)]
        return sequence[:self.length]

    def _integer_fraction_pattern(self):
        sequence = [1, '2', '24/12', '3', '36/12', '21/7']
        return sequence[:self.length]

    def _fibonacci_fractions(self):
        fib_gen = fibonacci()
        numerators = [next(fib_gen) for _ in range(self.length)]
        denominators = [next(fib_gen) for _ in range(self.length)]
        sequence = [f"{n}/{d}" for n, d in zip(numerators, denominators)]
        return sequence

    def _separate_patterns(self):
        sequence = []
        numerator = 5
        denominator = 6
        for _ in range(self.length):
            sequence.append(f"{numerator}/{denominator}")
            numerator += 9
            denominator += 1 if len(sequence) % 2 == 0 else 2
        return sequence

    def get_sequence(self):
        return self.sequence


if __name__ == "__main__":
    # Example usage:
    seq_gen = SequenceGenerator('5/6', 'separate_patterns', length=7)
    print(seq_gen.get_sequence())

    seq_gen2 = SequenceGenerator(6, 'add_primes', length=10)
    print(seq_gen2.get_sequence())
