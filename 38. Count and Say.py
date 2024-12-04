class Solution:
    def countAndSay(self, n: int) -> str:
        # base cases
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        # check everything till the last character
        string = "11"
        for i in range(3, n+1):
            # initialisations
            output = ""
            count = 1 # we have atleast 1 char

            # add a character to make traversal easy to the last character
            string += "$"
            for j in range(1, len(string)):
                if string[j] == string[j-1]:
                    count += 1
                else:
                    output += str(count) + string[j-1]
                    count = 1 # reset count for the next sequence
                
            # set string to this output for the next iteration
            string = output
        return output