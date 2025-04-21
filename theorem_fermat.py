import math

def verify_fermat(limit=100, n=3):
    """
    Verifies Fermat's Last Theorem for values of a, b, c up to a given limit and exponent n > 2.
    Prints any counterexamples found (none should be found).
    
    Parameters:
        limit (int): Upper limit for values of a and b.
        n (int): Exponent to test (must be greater than 2).
    """
    if n <= 2:
        print("⚠️ Fermat's Last Theorem only applies to n > 2.")
        return

    print(f"🔍 Testing Fermat's Last Theorem for n = {n} and values up to {limit}...")

    found_counterexample = False

    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c_power = a**n + b**n
            c = round(c_power ** (1 / n))

            if c**n == c_power:
                print(f"❗ Counterexample found: {a}^{n} + {b}^{n} = {c}^{n}")
                found_counterexample = True

    if not found_counterexample:
        print("✅ No counterexamples found. Fermat's Last Theorem holds for this range.")

if __name__ == "__main__":
    # Run with default parameters
    verify_fermat(limit=100, n=3)
