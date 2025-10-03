        a, b = zero_filler(a,b)

        
        for i in range(len(a) - 1, -1, -1):
        result = []
        carry = 0
        
            return s1, s2
                s2 = "0" * (len(s1) - len(s2)) + s2
            elif len(s2) < len(s1):
            total = int(a[i]) + int(b[i]) + carry
            result.append(str(total % 2))
            carry = total // 2
        
        if carry:
            result.append("1")
        
        return "".join(reversed(result))
