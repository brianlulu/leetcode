'''

    Input: word -> str, abbr -> str
    Output: whether the word can be abbreviated to abbr -> bool
    
    Given a string word and an abberviation abbr, return the word can be abbreviated to abbr
    
        Abbr condition:
            a string can be abbr to the length of the substring, but the abbr substrings should be 
                non-adjacent
                    valid: 
                        adjancent => "adj" + a + "ncent" => 3a5
                    non-valid:
                        a24t => a + "dj" + "ncen" + t => 24 are adjancet
                non-empty
                    the substring cannot be length 0
    
    constraints:
        empty string for word? => no
        abbr.length >= 1
        lowercase and digit
    
    adjancent:
        a + substring -> length > 0 + substring -> str
        1 + d + substring -> length > 0 + substring -> str
    
    abbr:
     word = adjancent; abbr = 3a5
     
     word = a abbr= a
     
     check the length of abbr and word match up and also that the current index character match up or not
     
     two pointer for each string
     
     
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    
        w = a = 0
        
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit():
                cur = 0
                while a < len(abbr) and abbr[a].isdigit():
                    cur = cur * 10 + int(abbr[a])
                    if cur == 0 and abbr[a] == "0":
                        return False
                    a += 1
                
                w += cur 
            
            else:
                if word[w] != abbr[a]:
                    return False
                
                w += 1
                a += 1
        
        return w == len(word) and a == len(abbr)
        
        
        
        
        
        
        
        