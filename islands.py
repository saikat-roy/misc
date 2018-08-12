class Solution(object):
	'''
	Designed to solve the number of Islands problem on LeetCode
	https://leetcode.com/problems/number-of-islands/description/
	
	Does not have a driver method but you could write one easily 
	'''
    
    def island_merge(self,md, b, i1, j1, i2, j2):
	'''
	Driver for recursive merging of island memberships
    
    Parameters
    -----------
    md: Dict[int,List[int]]
    key represents island number, val is a list containing
    all other islands merged with 'key' island 
    
    b: List[List[int]]
    Island location Matrix without merging
    
    i1, j1, i2, j2: int
    x,y coordinates of points being compared. Only points
    compared in this code are top and left points to center.
    (See call from bottom of numIslands)
    '''
        self.rec_merge(md, b[i1][j1], b[i2][j2])
        self.rec_merge(md, b[i2][j2], b[i1][j1])

        return md

    def rec_merge(self,md,loc,val):
        '''
        Recursively adds the val to list in the particular location
        in the dictionary
        '''
        if val in md[loc]: return   # Cycle Guard
        else: 
            md[loc].append(val)

        for isl_no in md[loc]:
            if isl_no != val: # Infinite loop guard
                self.rec_merge(md,isl_no,val)
                md[isl_no].append(val)
    
    
    def numIslands(self, grid):
        """
        Populates an island discovery list of lists 'b' and uses a
        dictionary to merge the 
        
        :type grid: List[List[str]]
        :rtype: int
        """
        
        b = [[0]*len(grid[0]) for i in range(len(grid))]
        merge_dict = dict()
        isl = 1
        count = 0
        
        # Island generation without merging
        for i in range(len(grid)):     
            for j in range(len(grid[0])):
                c=0
                if grid[i][j]=='1':
                    if grid[i-1][j]=='1' and i!=0:
                        b[i][j]=b[i-1][j]
                        c=1
                    if grid[i][j-1]=='1' and j!=0:
                        b[i][j]=b[i][j-1]
                        c=1
                    if c!=1:
                        merge_dict[isl]=[]
                        b[i][j]=isl
                        isl+=1
        
        # Island merging. 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    # Searches top and processes if the clusters
                    # have not already been merged
                    if grid[i-1][j]=='1' and b[i-1][j]!=b[i][j] and i!=0 and \
                        b[i-1][j] not in merge_dict[b[i][j]] and \
                        b[i][j] not in merge_dict[b[i-1][j]]:
                        isl-=1
                        merge_dict = self.island_merge(merge_dict,b,i-1,j,i,j)
                     
                    # Searches left and processes if the clusters
                    # have not already been merged
                    if grid[i][j-1]=='1' and b[i][j-1]!=b[i][j] and j!=0 and \
                        b[i][j-1] not in merge_dict[b[i][j]] and \
                        b[i][j] not in merge_dict[b[i][j-1]]:
                        isl-=1
                        merge_dict = self.island_merge(merge_dict,b,i,j-1,i,j)
        return isl-1

