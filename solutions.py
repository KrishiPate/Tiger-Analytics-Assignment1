from helper import Helper
import math
import re
class Solution:
    def __init__(self) -> None:
        self.helper = Helper()

    def q1(self):
        X, Y = [int(x) for x in input().split(',')]
        ans = [[i*j for j in range(Y)] for i in range(X)]
        return ans
    
    def q2(self):
        x = input().split(',')
        x.sort()
        return ",".join(x)
    
    def q3(self):
        x = input().split(' ')
        x = list(set(x))
        x.sort()
        return " ".join(x)
    
    def q4(self):
        ans = list()
        for i in range(1000, 3001):
            if all(int(j)%2 == 0 for j in str(i)): # new "all" keyword checks whether all the values in the list are true
                ans.append(str(i))
        return ','.join(ans)
    
    def q5(self):
        x = input()
        letter = 0
        digit = 0
        for i in x:
            if i.isalpha():
                letter += 1
            elif i.isdigit():
                digit += 1
        return {"LETTER": letter, "DIGIT": digit}

    def q6(self):
        s = input()
        upper = 0
        lower = 0
        for i in s:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
        return {"UPPER": upper, "LOWER": lower}
    
    def q7(self):
        final_amount = 0
        while True:
            try:
                transaction = input()
                amount = int(transaction[2:])
                if "D" in transaction:
                    final_amount += amount
                elif amount <= final_amount:
                    final_amount -= amount
                else:
                    return {final_amount: "Can't withdraw amount more than the current account balance"}
            except EOFError:
                return final_amount
    
    def q8(self):
        passwords = input().split(',')
        valid_passwords = list()
        for password in passwords:
            if self.helper.is_valid_psswd(password):
                valid_passwords.append(password)
        return ','.join(valid_passwords)

    def q9(self):
        data = []
        while True:
            line = input()
            if not line:
                break
            name, age, height = line.split(',')
            data.append((name, int(age), int(height)))
        
        data.sort(key=lambda x: (x[0], x[1], x[2]))

        return data
    
    def q10(self):
        final_cordinates = [0, 0]
        while True:
            line = input()
            if not line:
                break
            movement = line.split(' ')
            if "LEFT" in movement:
                final_cordinates[0] -= int(movement[1])
            elif "RIGHT" in movement:
                final_cordinates[0] += int(movement[1])
            elif "UP" in movement:
                final_cordinates[1] += int(movement[1])
            else:
                final_cordinates[1] -= int(movement[1])
        return round(math.sqrt(final_cordinates[0]**2 + final_cordinates[1]**2))
    
    def q11(self):
        result = ""

        s = input().lower()
        
        current_char = s[0]
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result += current_char + str(count)
                current_char = s[i]
                count = 1
        
        result += current_char + str(count)
        
        return result
    
    def q12(self):
        s = input()
        n = len(s)
        result_char = list()
        for i, char in enumerate(s):
            if not s[i].isalpha():
                continue
            digit_sum = 0
            for j in range(i+1, n):
                if s[j].isdigit():
                    digit_sum += int(s[j])
                elif s[j].isalpha() and digit_sum == 9:
                    result_char.append((char, s[j]))
        return result_char

    def q13(self):
        binary_string = input()
        ones_positions = [i for i, bit in enumerate(binary_string) if bit == '1']
            
        n = len(ones_positions)
        
        return (n * (n - 1)) // 2

    
    def q14(self):
        x = [int(i) for i in input().split(',')]
        money = x[-1]
        denominations = x[:-1]
        denominations.sort(reverse=True)
        ans = dict()
        for i, e in enumerate(denominations):
            if(money > 0 and e <= money):
                ans[e] = money//e
                money = money % e
        return ans
    
    def q15(self):
        n, p = [int(i) for i in input().split(',')]
        num = 1
        dem = 1
        s = p
    
        while p != 1:
            dem *= p
            p-=1
        
        t = n - s + 1
        while t != (n-2 * s + 1):
            num *= t
            t-=1
        if (n - s + 1) >= s:
            return int(num/dem)
        else:
            return -1
    
    def q16(self):
        player_a = input().lower()
        player_b = input().lower()
        
        if player_a == player_b:
            return "DRAW"
        elif (player_a == "stone" and player_b == "scissor") or \
            (player_a == "scissor" and player_b == "paper") or \
            (player_a == "paper" and player_b == "stone"):
            return "Player A wins"
        else:
            return "Player B wins"
    def q17(self):
        email = input()
        pattern = r'^[a-z0-9._]+@[a-z0-9]+\.[a-z]+$'

        if re.fullmatch(pattern, email):
            return True
        else:
            return False
    
    # QUESTION 18
    def q18_a(self):
        row = input()
        return Helper.pattern_a(row)
    def q18_b(self):
        row = input()
        return Helper.pattern_b(row)
    def q18_c(self):
        row = input()
        return Helper.pattern_c(row)
    def q18_d(self):
        row = input()
        return Helper.pattern_d(row)
    def q18_e(self):
        row = input()
        return Helper.pattern_e(row)
    
    def q19(self):
        x = input().split(',')
        case = int(x[0])
        times = int(x[2])
        s = x[1]
        ans = list()
        if case == 1:
            for _ in range(times):
                s = s[1:] + s[0]  # Move the first character to the end
                ans.append(s)
            return ans
        
        elif case == 2:
            for _ in range(times):
                s = s[-1] + s[:-1]  # Move the last character to the start
                ans.append(s)
            return ans
        
    def q20(self):
        number_str = input()
        digits = [int(digit) for digit in number_str]
        num_digits = len(digits)
        armstrong_sum = sum(digit ** num_digits for digit in digits)
        return armstrong_sum == int(number_str)
    
    def q22(self):
        number = input()
        ans = ""
        if ( number == 0 ):
            return 0
        while ( number ):
            ans += str(number&1)
            number = number >> 1
        
        ans = ans[::-1]

        return ans 
    
    def q23(self):
        n = int(input())
        divisors = [i for i in range(1, n) if n % i == 0]
        
        divisor_sum = sum(divisors)
        
        if divisor_sum == n:
            return "Perfect number"
        else:
            return "Not a perfect number"
obj = Solution()
print(obj.q23())
# 21