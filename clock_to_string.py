

# def time_in_words(h,m):
#     if h < 0 or h > 12:
#         return "Invalid hour"
#     if m < 0 or m >= 60:
#         return "Invalid minute"
#     nums = {
#         0:'twelve',1:'one', 2:'two', 3:'three', 4:'four',
#         5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',  
#         }
    
#     specials = { 
#         10:'ten', 11:'eleven', 12:'twelve',
#         13:'thirteen',15:'quarter',
#     }

#     dec = {
#        1:'teen', 2:'twenty',3:'thirty',4:'forty',5:'fifty'
#     }
    
#     def hour_to_text(hour):
#         if hour in specials:
#             return specials[hour]
#         return nums[hour]

#     def minutes_to_text(minutes):
#         tens = minutes // 10
#         units = minutes - tens*10

#         if tens == 0:
#             return nums[minutes]
        
#         elif tens == 1:
#             if minutes in specials:
#                 return specials[minutes]
#             return nums[units] + dec[tens]
        
#         else:
#             return dec[tens] + " " + nums[units]
    
    
#     min_text = "minute" if m == 1 else "minutes"
#     if m == 0:
#         return f'{hour_to_text(h)} o\' clock'
#     elif m == 15:
#         return f'quarter past {hour_to_text(h)}'
#     elif m == 30:
#         return f'half past {hour_to_text(h)}'
#     elif m < 30:
#         return f'{minutes_to_text(m)} {min_text} past {hour_to_text(h)}'
#     elif m==45:
#         return f'quarter to {hour_to_text(h+1)}'
#     else:
#         return f'{minutes_to_text(60-m)} {min_text} to {hour_to_text(h+1)}'  

# h = 11
# m = 60





class TimeInWords:
    nums = {
        0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    }
    specials = {
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 15: 'quarter',
    }
    tens = {
        1: 'teen', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty'
    }
    
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def _validate_input(self):
        if self.h < 0 or self.h > 12:
            return False
        if self.m < 0 or self.m >= 60:
            return False
        return True

    def _hour_to_text(self, hour):
        if hour in TimeInWords.specials:
            return TimeInWords.specials[hour] 
        return TimeInWords.nums[hour]

    def _minutes_to_text(self, minutes):
        
        tens = minutes // 10
        units = minutes - tens * 10
        if tens == 0:
            return TimeInWords.nums[minutes]
        elif tens == 1:
            if minutes < 20:
                return TimeInWords.specials[minutes]
            return TimeInWords.nums[units] + " " + TimeInWords.tens[tens]
        else:
            return TimeInWords.tens[tens] + " " + TimeInWords.nums[units]

    def convert(self):
        if not self._validate_input():
            return "Invalid input"
        min_text = "minute" if self.m == 1 else "minutes"
        if self.m == 0:
            return f"{self._hour_to_text(self.h)} o' clock"
        elif self.m == 15:
            return f"quarter past {self._hour_to_text(self.h)}"
        elif self.m == 30:
            return f"half past {self._hour_to_text(self.h)}"
        elif self.m < 30:
            return f"{self._minutes_to_text(self.m)} {min_text} past {self._hour_to_text(self.h)}"
        elif self.m == 45:
            return f"quarter to {self._hour_to_text(self.h + 1)}"
        else:
            return f"{self._minutes_to_text(60 - self.m)} {min_text} to {self._hour_to_text(self.h + 1)}"

h=11
m = 13 
clock1 = TimeInWords(h,m)
print(clock1.convert())










