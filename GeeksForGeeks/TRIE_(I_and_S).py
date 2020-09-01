
'''
class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
'''
def createNode():
    return TrieNode()
def insert(root,key):
    '''
    root: root of trie tree
    key:  key to be inserted
    '''
    pCrawl = root 
    length = len(key) 
    for level in range(length):
        index = ord(key[level])-ord('a') 
        if not pCrawl.children[index]:
            pCrawl.children[index] = createNode() 
        pCrawl = pCrawl.children[index] 

    # mark last node as leaf 
    pCrawl.isEndOfWord = True


def search(root, key):
    pCrawl=root
    length = len(key)
    for level in range(length):
        index = ord(key[level])-ord('a') 
        if not pCrawl.children[index]: 
            return False
        pCrawl = pCrawl.children[index] 
    return pCrawl != None and pCrawl.isEndOfWord 
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        if search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends