## hybrid inheritance

class Upper:
    @staticmethod
    def upper():
        up_char = ''
        for i in range(ord('A') , ord('Z')+1):
            up_char += chr(i)
        return up_char

class Alpha(Upper):
    @staticmethod   
    def lower():
        low_char =''
        for i in range(ord('a') , ord('z')+1):
            low_char += chr(i)
        return low_char
    @staticmethod
    def lower():
        low_char= ''
        for i in range(ord('a') , ord('z')+1):
            low_char += chr(i)
        return low_char
    
class Number:
    @staticmethod
    def number():
        number =''
        for i in range(0,10):
            number += str(i)
        return number
    
class Characters(Alpha, Number):
    @staticmethod
    def sp_char():
        special_char = ''
        for i in range(32, 127):
            if not(chr(i)).isalnum():
                special_char += chr(i)
            return special_char
        

ob1 = Characters()
print(ob1.lower())
print(ob1.upper())
print(ob1.number())
print(ob1.sp_char())
