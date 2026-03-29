# %%
import json

grid = [] # global variable grid representing the word puzzle, soon to become a 2D array/list

# BEGIN SEARCH -------------------------------------------------------------------|
def search(word):
    """
    Searches for 'word' in the word puzzle by searching in
    the directions forward, reverse, up, and down.
    """
    # ---------------------------------------------------
    def search_forward():
        """
        Search for the word in a left-to-right direction.
        """
        for row in range(len(grid)):
            for col in range(len(grid[row]) - len(word) + 1): # slide across row for length of word, starting at col
                
                match = True
                for i in range(len(word)):
                    if grid[row][col + i] != word[i]:
                        match = False # if no match found, break and search for word starting at next letter in row
                        break
                
                if match: # if match found, store start and end coordinates
                    start = [row, col]
                    end = [row, col + len(word) - 1] # calculate col based on length of word
                    return {'direction': 'forward', 'start': start, 'end': end} # return dictionary containing direction & coordinates
                    
        return None # no matches found
    # ---------------------------------------------------
    def search_reverse():
        """
        Search for the word in a right-to-left direction.
        """
        for row in range(len(grid)):
            for col in range(len(grid[row]) - len(word) + 1):
                
                match = True
                for i in range(len(word)):
                    if grid[row][col + i] != word[len(word) - 1 - i]: # match letter in word from right to left
                        match = False
                        break
                
                if match:
                    start = [row, col + len(word) - 1] # calculate col for start coordinates
                    end = [row, col]
                    return {'direction': 'reverse', 'start': start, 'end': end}
    
        return None  # no matches found
    # ---------------------------------------------------
    def search_up(): 
        """
        Search for the word in an upward direction.
        """
        # search downward in the grid & compare it with the reversed letters of given word
        for row in range(len(grid) - len(word) + 1):
            for col in range(len(grid[row])):
                
                match = True
                for i in range(len(word)):
                    if grid[row + i][col] != word[len(word) - 1 - i]:
                        match = False
                        break
                
                if match:
                    start = [row + len(word) - 1, col]
                    end = [row, col]                    
                    return {'direction': 'up', 'start': start, 'end': end}
    
        return None  # no matches found
    # ---------------------------------------------------
    def search_down():
        """
        Search for the word in a downward direction.
        """
        for row in range(len(grid) - len(word) + 1):
            for col in range(len(grid[row])):
                
                match = True
                for i in range(len(word)):
                    if grid[row + i][col] != word[i]: # compare each letter going down the column
                        match = False
                        break
                
                if match:
                    start = [row, col]                     
                    end = [row + len(word) - 1, col]       
                    return {'direction': 'down', 'start': start, 'end': end}
    
        return None  # no matches found
    # ---------------------------------------------------
    # Identify direction the word was found in
    result = ""
    if search_forward() != None:
        result = search_forward()
    elif search_reverse() != None:
        result = search_reverse()
    elif search_up() != None:
        result = search_up()
    elif search_down() != None:
        result = search_down()

    dictionary = {'found_in': [result]} # store result (direction + coordinates found)

    return {f'{word}': dictionary} # output of parent search() function

# END OF SEARCH -------------------------------------------------------------------|

# BEGIN MAIN ----------------------------------------------------------------------|

def main():
    """
    Reads puzzle and word bank files, searches for words, 
    and exports results to JSON.
    """

    # Parse wordpuzzle.txt into a 2D list
    with open('wordpuzzle.txt', 'r') as f:
        row = 0
        while True:
            string = f.readline() # read one line (row) in wordpuzzle
            if len(string) == 0:
                break
            else:
                grid.append([])   # append row (list) to global variable grid to make grid a 2D list
                for c in string: 
                    if c != '\n':
                        grid[row].append(c) # append letter to the given row
            row += 1
    
    # Display the puzzle grid
    print(" --- Word Puzzle --- ")
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], " ", end="")
        print()
    
    print()
    
    # Parse wordbank.txt
    with open('wordbank.txt', 'r') as f:
        content = f.read()
        print(" --- Word Bank --- ")
        wordbank = content.split() # print as a list
    print(wordbank, '\n')

    # Build the final results dictionary
    print(" --- Final Dictionary --- ")
    final_dict = {} 
    for word in wordbank:
        final_dict.update(search(word))

    print(final_dict)
    print()

    # Write the dictionary to a JSON file
    with open("word_search_results.json", "w") as json_file:
        json.dump(final_dict, json_file, indent=4)
    
    print("Results saved to word_search_results.json")
                          
# end of main --------------------------------------------------------------------

main() # call main


