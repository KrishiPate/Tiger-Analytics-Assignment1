class Helper:
    def is_valid_psswd(self, password):
        psswd_length = len(password)
        if psswd_length < 6 or psswd_length > 12:
            return False
        
        lower_alphabet = False
        upper_alphabet = False
        number = False
        special_char = False

        special_string = "#$@"

        for i in password:
            if i.isalpha() and i.islower():
                lower_alphabet = True
            elif i.isalpha() and i.isupper():
                upper_alphabet = True
            elif i.isdigit():
                number = True
            elif i in special_string:
                special_char = True

        return lower_alphabet and upper_alphabet and number and special_char
    def pattern_a(self, rows):
        num = 1
        for i in range(1, rows+1):
            for j in range(i):
                if j > 0:
                    print("*", end=" ")
                print(num, end=" ")
                num += 1
            print()

    # Pattern b
    def pattern_b(self, rows):
        for i in range(1, rows+1):
            print(" " * (rows-i) + "* " * i)
        for i in range(rows-1, 0, -1):
            print(" " * (rows-i) + "* " * i)

    # Pattern c
    def pattern_c(self, rows):
        num = 1
        # First half
        for i in range(1, rows+1):
            for j in range(i):
                if j > 0:
                    print("*", end=" ")
                print(num, end=" ")
                num += 1
            print()
        
        # Second half
        start = num - rows
        for i in range(rows-1, 0, -1):
            num = start
            for j in range(i):
                if j > 0:
                    print("*", end=" ")
                print(num, end=" ")
                num += 1
            start -= i
            print()

    # Pattern d (for the letter 'G')
    def pattern_d(self, rows):
        for i in range(rows):
            if i == 0:
                print("***")
            elif i < rows//2:
                print("*")
            elif i == rows//2:
                print("* ***")
            else:
                print("*    *" if i != rows-1 else "* * *")

    # Pattern e
    def pattern_e(self, rows):
        for i in range(rows):
            if i == 0 or i == rows-1:
                print("1 " * rows)
            else:
                print("0 " * (rows//2) + "1 " + "0 " * (rows//2))