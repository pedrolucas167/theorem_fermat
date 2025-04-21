# 🔢 Fermat's Last Theorem Verifier

This project is a simple Python implementation to **empirically verify Fermat's Last Theorem**, one of the most famous problems in the history of mathematics.

> **What does the theorem say?**  
> For `n > 2`, **there are no positive integers** `a`, `b`, and `c` that satisfy the equation:  
> **aⁿ + bⁿ = cⁿ**

Although it was proven by Andrew Wiles in 1994, this project performs a computational validation for educational and exploratory purposes.

---

## Features

- Checks if any combination of `a`, `b`, and `c` satisfies `aⁿ + bⁿ = cⁿ`, with `n > 2`.
- Optimized brute-force approach to avoid redundant checks.
- Estimates `c` using the n-th root of the sum `aⁿ + bⁿ` to improve performance.
- Informative progress and result messages.

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/fermat-verifier.git
cd fermat-verifier
