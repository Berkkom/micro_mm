
import numpy as np

def main():
    rng = np.random.default_rng(0)
    x = rng.normal(size=5)
    print("It works! Sample:", x)

if __name__ == "__main__":
    main()
