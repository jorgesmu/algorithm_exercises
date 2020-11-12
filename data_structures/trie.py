class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        single = [1, 8]
        opposites = {
            1: 1,
            8: 8,
            6: 9,
            9: 6
        }
        def make_tail(number):
          
        def make_front(n, odd, curr, singles, opposites, fronts):
            if len(curr) == ((n+1)//2):
                fronts.append(curr)
            if odd and n == 1:
                coll = signles
            else:
                coll = opposites
            for opp in coll:
                make_front(n-1, curr, singles, opposites, fronts):
                
        fronts = []
        make_front(n, n%2==1, curr, single, opposites, fronts)  
        print(fronts)