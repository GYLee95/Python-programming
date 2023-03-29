"""
@author: gangylee

Description : 
    # Given a string, find the first non-repeating character in it and return its index. 
    # If it doesn't exist, return -1. 
    # Note: all the input strings are already lowercase.
"""

def solution(s):
    for i in range(len(s)):
      found = True
      for j in range(i+1, len(s)):
        if s[i]==s[j]:
          found = False
          break
      if found==True:
        return i
    return -1

def main():
    print(solution('alphabet'))
    print(solution('barbados'))
    print(solution('crunchy'))

if __name__ == '__main__':
    main()
