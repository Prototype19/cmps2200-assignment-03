import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-ur-ra', 'kooky-bi-rd--'), ('-ele-phant', 'relev--ant'), ('AAAGAATTCA', 'AAA---T-CA')]
def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def med_top_down(S, T, MED={}):
    ## look up the memory
    if (S, T) in MED:
        return MED[(S, T)]
    ## base cases
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    ## recursive cases
    if S[0] == T[0]:  # If first characters are the same, move to the next
        MED[(S, T)] = med_top_down(S[1:], T[1:], MED)
    else:
        insert = med_top_down(S, T[1:], MED) + 1  # Insert a character
        delete = med_top_down(S[1:], T, MED) + 1  # Delete a character
        MED[(S, T)] = min(insert, delete)
    
    return MED[(S, T)]
    
def fast_MED(S, T):
    # initialize TxS table
    S_len = len(S) + 1
    T_len = len(T) + 1
    OPT = [[0 for _ in range(T_len)] for _ in range(S_len)]

    for i in range(S_len):
        OPT[i][0] += i
    for k in range(T_len):
        OPT[0][k] += k

    # Loop through each row its elements and apply optimal substructure property
    for i in range(1, S_len):
        for k in range(1, T_len):
            if S[i-1] == T[k-1]:
                OPT[i][k] = OPT[i-1][k-1]
            else:
                OPT[i][k] = 1 + min(OPT[i-1][k], OPT[i][k-1])
    for j in OPT:
        print(j)
    # Return bottom right element
    return OPT[-1][-1]


def fast_align_MED(S, T):
    # initialize TxS table
    S_len = len(S) + 1
    T_len = len(T) + 1
    OPT = [[0 for _ in range(T_len)] for _ in range(S_len)]

    # Base Cases
    for i in range(S_len):
        OPT[i][0] += i
    for k in range(T_len):
        OPT[0][k] += k

    # Loop through each row its elements and apply optimal substructure property
    for i in range(1, S_len):
        for k in range(1, T_len):
            if S[i - 1] == T[k - 1]:
                OPT[i][k] = OPT[i - 1][k - 1]
            else:
                OPT[i][k] = 1 + min(OPT[i - 1][k], OPT[i][k - 1])

    # Construct aligned S and T
    alignment_S = []
    alignment_T = []

    i, k = S_len - 1, T_len - 1
    while i > 0 or k > 0:
        y = OPT[i - 1][k]
        z = OPT[i][k - 1]
        # match: move diagonal
        if i > 0 and k > 0 and S[i - 1] == T[k - 1] and OPT[i - 1][k] == OPT[i][k - 1]:
            alignment_S.append(S[i - 1])
            alignment_T.append(T[k - 1])
            i -= 1
            k -= 1
        # insert: move up
        elif i > 0 and y <= z:
            alignment_S.append(S[i - 1])
            alignment_T.append('-')
            i -= 1
        # delete: move left
        elif k > 0 and y > z:
            alignment_S.append('-')
            alignment_T.append(T[k - 1])
            k -= 1
        # edge handling
        else:
            if i > 0 and k > 0:
                alignment_S.append(S[i - 1])
                alignment_T.append(T[k - 1])
                i -= 1
                k -= 1
            elif i > 0:
                alignment_S.append(S[i - 1])
                alignment_T.append('-')
                i -= 1
            else:
                alignment_S.append('-')
                alignment_T.append(T[k - 1])
                k -= 1


    alignment_S = ''.join(reversed(alignment_S))
    alignment_T = ''.join(reversed(alignment_T))
    return alignment_S, alignment_T

