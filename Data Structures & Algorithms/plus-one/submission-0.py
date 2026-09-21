import copy
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # do elementary arithmetic on reversed list 

        digits_r = copy.deepcopy(digits)
        digits_r.reverse()
        carry = 0
        dig_sum = 0
        ans = []
        for i in range(len(digits_r)):
            if i == 0: 
                dig_sum = digits_r[i] + 1
            else: 
                dig_sum = digits_r[i] + carry
            
            #print(f"dig_sum: {dig_sum} for {i}th iteration")
            dig_q = dig_sum % 10
            carry = dig_sum // 10
            # print(f"dig_sum: {dig_sum}, dig_q: {dig_q}, carry: {carry} for {i}th iteration")
            ans.append(dig_q)
        
        if carry: 
            ans.append(carry)
        
        ans.reverse()

        return ans