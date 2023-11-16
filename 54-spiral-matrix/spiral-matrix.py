class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        while len(matrix)>0:
            if len(matrix) == 0:
                break
            else:
                #move forward
                for i in range(0, len(matrix[0])):
                    if len(matrix[0]) == 0:
                        break
                    else:
                        #traversing through the first array
                        spiral.append(matrix[0][0])
                        #after adding each element remove the element.
                        matrix[0].remove(matrix[0][0])
                #after moving forward, definitely we have to remove the list.
                matrix.remove(matrix[0]) #Hopefully, this is an empty list.

            if len(matrix) == 0:
                break
            else:
                #move downward
                for i in range(0, len(matrix)):
                    if len(matrix[i]) == 0:
                        break
                    else:
                        spiral.append(matrix[i][-1])
                        #remove from the list
                        matrix[i].remove(matrix[i][-1])
            
            if len(matrix) == 0:
                break
            else:
                #move backward
                for i in range(0, len(matrix[-1])):
                    if len(matrix[-1]) == 0:
                        break
                    else:
                        spiral.append(matrix[-1][-1])
                        #remove element
                        matrix[-1].remove(matrix[-1][-1])
                #after traversing backward, the list is definitely empty
                matrix.remove(matrix[-1]) #Removes the last list

            if len(matrix) == 0:
                break
            else:
            #move upward
                for i in range(1, len(matrix)+1):
                    if len(matrix[-i]) == 0:
                        break
                    else:
                        spiral.append(matrix[-i][0])
                        #remove element
                        matrix[-i].remove(matrix[-i][0])

        return spiral