"""
    Title: Eotvos Lorand University PROBLEM 1 Assignment solution.
    Author: Esteban Hernandez Ramirez.
    Date: April 2023.
    GitHub repository:
        HTTPS: https://github.com/estebanhramirez/Eotvos-Lorand-University.git
        SSH: git@github.com:estebanhramirez/Eotvos-Lorand-University.git
"""


def interface(path='./', file='input.txt'):
    """
    Input:
        path: string variable specifying the path towards the file.
        file: string variable specifying the name of the file.
    Output:
        lines: list of strings corresponding to each raw line in the input file.
    Complexity:
        time: O(n), where n is the number of flights.
        space: O(n), where n is the number of flights.

    Explanation:
        since the input file, 'input.txt', contains structured data, such that each line of
        the file aims to store information about a different outbound flight from Budapest,
        each line is made of two strings and an integer number, separated by whitespaces, that
        describe the given flight...

        the file is splitted by the '\n' -new line- character, by processig the file once and 
        saving a new line when the '\n' character is found at the end of a line...
        the raw lines of the input file are imported into Python as a list of composed strings,
        'lines'. This way we preserve the structure of the data by having each entry in the
        'lines' list corresponding to the description of a different flight, furthermore,
        this approach preserves the relative order of the file.

        * the size of the file is proportional to the number of flights registered in it *
    """

    with open(path+file, 'r', encoding="utf-8") as doc:
        lines = doc.readlines()
    return lines


def split_lines(lines):
    """
    Input:
        lines: list of strings corresponding to each raw line in the input file.
    Output:
        airls: list of strings corresponding to the airline name of each flight.
        dests: list of strings corresponding to the destinations of each flight.
        pssgs: list of ints corresponding to the number of passengers of each flight.
    Complexity:
        time: O(n), where n is the number of flights.
        space: O(n), where n is the number of flights.

    Explanation:
        since the airline and destination names do not contain space characters,
        neither does the number of passengers, we split each line of the file by
        white-space characters, to retrieve a tuple made of three items:
            - name of airline that operates the given flight (string variable)
            - destination of the given flight (string variable)
            - number of passengers transported by the given flight (int variable)

        * we parse the number of passengers to 'int' type * ...

        we traverse the list of lines once, while appending each splitted line's
        items to their corresponding lists, 'airls', 'dests' or 'pssgs', in the
        same order as the lines were read from the file. This way, we preserve the
        ascending alphabetical order of the flights by airline name.
    """

    airls = []
    dests = []
    pssgs = []
    for line in lines:
        airl, dest, pssg = line.split()
        airls.append(airl)
        dests.append(dest)
        pssgs.append(int(pssg))
    return airls, dests, pssgs


def exercise1(dests):
    """
    Input:
        dests: list of strings corresponding to the destinations of each flight.
    Output:
        cntr: number of flights with destination "Frankfurt".
    Complexity:
        time: O(n), where n is the number of flights.
        space: O(n), where n is the number of flights.

    Explanation:
        since the flights are ordered by airline name, instead of destination name, we
        cannot simply sum up consecutive occurrences of the destination "Frankfurt" in
        some binary search fashion, with, on average, O(log n) operations, and
        reordering the list by 'destination' would take at worst O(n log n) operations,
        thus, a linear time implementation is prefered...

        since the destination name "Frankfurt" could appear anywhere in the list, in the best
        linear implementation, we have to visit all elements in the list once, in order to
        know whether to count them or not: access every entry in the list once, to check if
        its value equals the string "Frankfurt"; if it does, update a counter of the number
        of times the destination "Frankfurt" appeared, increasing it by one unit.
    """

    cntr = 0
    for dest in dests:
        if dest == "Frankfurt":
            cntr += 1

    return cntr


def exercise2(pssgs):
    """
    Input:
        pssgs: list of ints abstracting number of passengers per each flight.
    Output:
        indx: list index of the corresponding flight with maximum number of passengers.
    Complexity:
        time: O(n), where n is the number of flights.
        space: O(n), where n is the number of flights.

    Explanation:
        since the flights are ordered by airline name, instead of number of passengers
        per flight, the flights with minimum and maximum number of passengers do not
        correspond to the first and last elements in the list, respectively, and
        reordering the list by 'destination' would take at worst O(n log n) operations,
        thus, a linear time implementation is prefered...

        since the maximum could appear anywhere in the list, we have to keep record
        of a local maximum variable and its index, then do a linear scan through every
        element in the list, so that if the element is greater than the current maximum,
        it is updated with this element and the current index is reset.
    """

    indx = -1
    maxi = 0
    for i, pssg in enumerate(pssgs):
        if pssg > maxi:
            indx = i
            maxi = pssg
    return indx


def exercise3(pssgs):
    """
    Input:
        pssgs: list of ints abstracting number of passengers per each flight.
    Output:
        indx: list index of corresponding first flight with < 100 passengers.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        loop through the list until the first flight with < 100 passengers is
        found or the iterable index exceeds the list's size.
    """

    indx = 0
    while indx < len(pssgs) and pssgs[indx] >= 100:
        indx += 1
    if indx >= len(pssgs)-1:
        return -1
    else:
        return indx


def exercise4(airls, pssgs):
    """
    Input:
        airls: list of strings abstracting airlines' names.
        pssgs: list of ints abstracting number of passengers per each flight.
    Output:
        indx: list index corresponding to airline with most total num of passengers.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        take advantage of the fact that the file is sorted by airline in
        ascending alphabetical order, so it is a matter of fact that all
        flights supported by a same airline are contiguous. This way, we
        can sum consecutive entries, until next entry corresponds to the
        next airline, in alphabetic order, then we compare if the current
        sum is grater than the greatest sum yet, stored in a temp variable.
    """

    indx = -1
    most = 0
    cntr = 0
    for i in range(0, len(airls)-1):
        cntr += pssgs[i]
        if airls[i] != airls[i+1]:
            if cntr > most:
                indx = i
                most = cntr
            cntr = 0

        if i == len(airls)-2:
            cntr += pssgs[-1]

    if cntr > most:
        indx = len(airls)-1
        most = cntr

    return indx, most


def solution(verbose=True):
    """
    Input:
        verbose: string indicating to print out in console the flow.
    Output:
        cntr1: int variable, solution to exercise 1
        indx2: int variable, solution to exercise 2
        indx3: int variable, solution to exercise 3
        indx4: int variable, solution to exercise 4
        most4: int variable, solution to exercise 4
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        invoked by main() function only.
    """

    path='./'
    file='input.txt'
    lines = interface(path, file)

    airls, dests, pssgs = split_lines(lines)

    cntr1 = exercise1(dests)
    indx2 = exercise2(pssgs)
    indx3 = exercise3(pssgs)
    indx4, most4 = exercise4(airls, pssgs)

    if verbose:
        print(cntr1)
        if indx2 == -1:
            print("The file is empty!")
        else:
            print(airls[indx2], dests[indx2], pssgs[indx2])
        if indx3 == -1:
            print("There is no flight with passengers less than 100.")
        else:
            print(airls[indx3], dests[indx3], pssgs[indx3])
        if indx4 == -1:
            print("The file is empty!")
        else:
            print(airls[indx4], most4)

    return cntr1, indx2, indx3, indx4, most4


def main():
    """
    Input:
        None.
    Output:
        None.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        Execute this function first.
    """

    solution()


main()