"""
    Title: Eotvos Lorand University PROBLEM 1 Assignment solution.
    Author: Esteban Hernandez Ramirez.
    Date: April 2023.
    GitHub repository:
        HTTPS: https://github.com/estebanhramirez/Eotvos-Lorand-University.git
        SSH: git@github.com:estebanhramirez/Eotvos-Lorand-University.git
"""


def import_flights(path='./', file='input.txt'):
    """
    Input:
        path: [str] string variable specifying the path towards the file
        file: [str] string variable specifying the name of the file
    Output:
        lines: [str array] list of raw lines of the input file
    Complexity:
        time: O(n)
        space: O(n)
    Explanation:
        Since the input file, 'input.txt', contains structured data, such
        that each line is made of two strings and an integer number, separated
        by whitespaces, describing the given flight, and so that the order
        matters, the file can be splitted by the new-line ('\n') character,
        by processig the file once, character-by-character, appending a new
        line into list 'lines' each time the '\n' character is found at the
        end of a line.
        This way we preserve the structure of the data by having each entry
        in the 'lines' list corresponding to the description of a different
        flight. Furthermore, this approach preserves the relative order of
        the file. The size of the file is proportional to the number of flights
        registered in it, therefore this algorithm has a linear complexity,
        on the number of flights, both in time and storage.
    """

    with open(path+file, 'r', encoding="utf-8") as doc:
        lines = doc.readlines()
    return lines


def split_lines(lines):
    """
    Input:
        lines: [str array] list of raw lines of the input file
    Output:
        airls: [str array] list of airlines for each flight
        dests: [str array] list of destinations for each flight
        pssgs: [int array] list of number of passengers for each flight
    Complexity:
        time: O(n)
        space: O(n)
    Explanation:
        Since the airline and destination names do not contain space characters,
        neither does the number of passengers, we split each line of the file by
        white-space characters, to retrieve a tuple made of three items:

            - name of the airline that operates the flight (string variable)
            - destination of the flight (string variable)
            - number of passengers transported by the flight (int variable)

        We traverse the list of lines once, while appending each splitted
        line's items to their corresponding lists, 'airls', 'dests' or 'pssgs',
        in the same order as the lines were imported from the file. This way,
        we preserve the ascending alphabetical order of the flights by airline
        name and garantee a linear complexity in the implementation, on the
        number of flights, both in time and storage.
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


def count_to_frankfurt_flights(dests):
    """
    Input:
        dests: [str array] list of destinations for each flight
    Output:
        cntr: [int] number of flights with destination "Frankfurt"
    Complexity:
        time: O(n)
        space: O(n)
    Explanation:
        Since the flights are ordered by airline name, instead of destination name, we
        cannot simply sum up consecutive occurrences of the destination "Frankfurt" in
        some binary search fashion, with, on average, O(log n) operations. Furthermore,
        reordering the list by 'destination' would take at worst O(n log n) operations.

        Thus, a linear time implementation is prefered: since the destination name
        "Frankfurt" could appear anywhere in the list, in the best linear implementation,
        we have to visit all elements in the list once, in order to know whether to count
        them or not i.e access every entry in the list once, to check if its value equals
        the string "Frankfurt"; if it does, update a counter of the number
        of times the destination "Frankfurt" appeared, increasing it by one unit.
    """

    cntr = 0
    for dest in dests:
        if dest == "Frankfurt":
            cntr += 1

    return cntr


def find_max_passengers_flight(pssgs):
    """
    Input:
        pssgs: [int array] list of number of passengers for each flight
    Output:
        indx: [int] list index of flight with the most number of passengers
    Complexity:
        time: O(n)
        space: O(n)
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


def find_first_less_100_flight(pssgs):
    """
    Input:
        pssgs: [int array] list of number of passengers for each flight
    Output:
        indx: [int] list index of first flight with less than 100 passengers
    Complexity:
        time: O(n)
        space: O(n)
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


def find_max_passengers_airline(airls, pssgs):
    """
    Input:
        airls: [str array] list of airlines for each flight
        pssgs: [int array] list of number of passengers for each flight
    Output:
        indx: [int] list index of airline with most total number of passengers
    Complexity:
        time: O(n)
        space: O(n)
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


def solve_problem_1():
    """
    Input:
        verbose: string indicating to print out in console the flow.
    Output:
        ans_exe_1: [int] number of flights with destination "Frankfurt"
        ans_exe_2: [str] flight with the most number of passengers
        ans_exe_3: [str] first flight with less than 100 passengers
        ans_exe_4: [tuple] airline with most total number of passengers
    Complexity:
        time: O(n).
        storage: O(n).
    Explanation:
        Invoked by main() function only.
    """

    path='./'
    file='input.txt'

    lines = import_flights(path, file)

    airls, dests, pssgs = split_lines(lines)

    cntr_to_frankfurt_flights = count_to_frankfurt_flights(dests)
    idx_max_passengers_flight = find_max_passengers_flight(pssgs)
    idx_first_less_100_flight = find_first_less_100_flight(pssgs)
    idx_max_passenger_airline, cnt = find_max_passengers_airline(airls, pssgs)

    ans_exe_1 = cntr_to_frankfurt_flights
    ans_exe_2 = ""
    ans_exe_3 = ""
    ans_exe_4 = None
    if idx_max_passengers_flight == -1:
        ans_exe_2 += "The file is empty!"
    else:
        ans_exe_2 += airls[idx_max_passengers_flight] + ' '
        ans_exe_2 += dests[idx_max_passengers_flight] + ' '
        ans_exe_2 += str(pssgs[idx_max_passengers_flight])

    if idx_first_less_100_flight == -1:
        ans_exe_3 += "There is no flight with passengers less than 100."
    else:
        ans_exe_3 += airls[idx_first_less_100_flight] + ' '
        ans_exe_3 += dests[idx_first_less_100_flight] + ' '
        ans_exe_3 += str(pssgs[idx_first_less_100_flight])

    if idx_max_passenger_airline == -1:
        ans_exe_4 = "The file is empty!"
    else:
        ans_exe_4 = (airls[idx_max_passenger_airline], cnt)

    return (ans_exe_1, ans_exe_2, ans_exe_3, ans_exe_4)


def main():
    """
    Input:
        None
    Output:
        None
    Complexity:
        time: O(n)
        space: O(n)
    Explanation:
        Execute this function first.
    """

    ans_exe_1, ans_exe_2, ans_exe_3, ans_exe_4 = solve_problem_1()

    print(ans_exe_1)
    print(ans_exe_2)
    print(ans_exe_3)
    print(ans_exe_4[0], ans_exe_4[1])

    return 0


#BEGINNING OF EXECUTION
main()
