class Solution:
    def whichweekday(self,day):
        match day:
            case 1:
                print("monday")
                
            case 2:
                print("tuesday")
                
            case 3:
                print("wensday")
                
            case 4:
                print("thursday")
                
            case 5:
                print("friday")
                
            case 6:
                print("saturday")
                
            case 7:
                print("sunday")
              
            case _:
                print("invalid")
day=int(input("enter day number: "))                
s1=Solution()
s1.whichweekday(day)