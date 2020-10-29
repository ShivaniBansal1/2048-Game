import random;

class Logics:
    def start_game():
        mat = []
        for i in range(4):
            mat.append([0]*4)

        r = random.randint(0,3)
        c = random.randint(0,3)
        
        mat[r][c] = 2
        return mat

    def insert_random_2(mat):
        r = random.randint(0,3)
        c = random.randint(0,3)
        
        while mat[r][c] != 0:
            r = random.randint(0,3)
            c = random.randint(0,3)
            
        mat[r][c] = 2
        return mat

    def current_state(mat):
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 2048:
                    return "WON"
                
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 0:
                    return "GAME NOT OVER"
                
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 2048:
                    return "WON"
                
        for i in range(4):
            for j in range(4):
                if j!=3:
                    if mat[i][j] == mat[i][j+1]:
                            return "GAME NOT OVER"
                if i != 3:
                    if mat[i][j] == mat[i+1][j] :
                        return "GAME NOT OVER"
                
        return "LOST"

    def areSame(A,B): 
        
        for i in range(N): 
            for j in range(N): 
                if (A[i][j] != B[i][j]): 
                    return True
        return False

    #compress function - returns a new compressed matrix

        
    def compress_matrix(mat):
        isChanged = False
        new_mat = []
        for i in range(4):
            new_mat.append([0]*4)
            
        for i in range(4):
            pos = 0
            for j in range(4):
                if mat[i][j] != 0:
                    new_mat[i][pos] = mat[i][j]
                    if j!= pos:
                        isChanged = True
                    pos += 1
        
    #     isChanged = areSame(mat, new_mat)
        return new_mat, isChanged
                

    # merge function - after compression, it merges cosecutive similar numbers, returns new matrix

    def merge_matrix(mat):
        isChanged = False
        new_mat = []
        for i in range(4):
            new_mat.append([0]*4)
            
        for i in range(4):
            pos = 0
            j=0
            while j<4:
                if j!=3 and (mat[i][j] == mat[i][j+1]) and mat[i][j] !=0 :
                    new_mat[i][j] = mat[i][j]*2
                    isChanged = True
                    j += 1
                else :
                    new_mat[i][j] = mat[i][j]
                j += 1 
        
    #     isChanged = areSame(mat, new_mat)
        return new_mat, isChanged

    # reverse a matrix

    def reverse_matrix(mat):
        new_mat = []
        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(mat[i][4-j-1])
        
        return new_mat

    # transpose a matrix
    def transpose_matrix(mat):
        new_mat = []
        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(mat[j][i])
        
        return new_mat

    #move left

    def move_left(mat):
        mat_1, changed_1 = compress_matrix(mat)
        mat_2, changed_2 = merge_matrix(mat_1)
        mat_3, temp = compress_matrix(mat_2)
        isChanged = changed_1 or changed_2
        return mat_3, isChanged
        
    # move right

    def move_right(mat):
        mat_1 = reverse_matrix(mat)
        mat_2, isChanged = move_left(mat_1)
        mat_3 = reverse_matrix(mat_2)
        return mat_3, isChanged

    # move up

    def move_up(mat):
        mat_1 = transpose_matrix(mat)
        mat_2, isChanged = move_left(mat_1)
        mat_3 = transpose_matrix(mat_2)
        return mat_3, isChanged

    # move down

    def move_down(mat):
        mat_1 = transpose_matrix(mat)
        mat_2, isChanged = move_right(mat_1)
        mat_3 = transpose_matrix(mat_2)
        return mat_3, isChanged


