import numpy as np

def input_matrix(name):
    print(f"\nEnter dimensions for {name} (rows cols): ", end="")
    rows, cols = map(int, input().split())
    print(f"Enter {rows}x{cols} matrix row by row (space separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} numbers. Try again.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

def main():
    while True:
        print("\n" + "="*40)
        print("MATRIX OPERATIONS TOOL")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '6':
            print("Exiting...")
            break

        if choice in ('1', '2', '3'):
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if choice == '1':
                try:
                    print("\nResult (A + B):\n", A + B)
                except ValueError:
                    print("Error: Matrices must have same dimensions for addition.")
            elif choice == '2':
                try:
                    print("\nResult (A - B):\n", A - B)
                except ValueError:
                    print("Error: Matrices must have same dimensions for subtraction.")
            elif choice == '3':
                try:
                    print("\nResult (A @ B):\n", np.dot(A, B))
                except ValueError:
                    print("Error: Number of columns of A must equal rows of B for multiplication.")

        elif choice == '4':
            A = input_matrix("Matrix")
            print("\nTranspose:\n", np.transpose(A))

        elif choice == '5':
            A = input_matrix("Matrix")
            if A.shape[0] != A.shape[1]:
                print("Error: Determinant only defined for square matrices.")
            else:
                det = np.linalg.det(A)
                print(f"\nDeterminant: {det:.4f}")

        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()