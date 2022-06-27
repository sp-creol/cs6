# Problem Set 4A

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence
    else:
        thisPerms = []
        for perm in get_permutations(sequence[1:]):
            for i in range(len(sequence)):
                thisPerms.append(perm[0:i] + sequence[0] + perm[i:])
        uniquePerms = []
        for perm in thisPerms:
            if not perm in uniquePerms:
                uniquePerms.append(perm)
        return uniquePerms


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
    for input in ["abc","hjkl","hippo"]:
        print("Input:",input)
        print("Output:",get_permutations(input))
