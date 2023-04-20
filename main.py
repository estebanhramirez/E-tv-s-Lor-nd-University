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
        path: [str] path towards the file
        file: [str] name of the file
    Output:
        lines: [str array] lines of the input file
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        The aim of this algorithm is to preserve the
        structured  meaning  of  the  data by making
        each entry in the 'lines' list correspond to
        the description of a different flight. To do
        so,  the  file  is splitted  by the new-line
        character ('\n'). Furthermore, this approach
        preserves  the  relative  order of the file,
        as  each flight is read in the same order as
        it was written in the file (top-to-bottom).

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage, since the file is read once and the
        size  of  the  file  is  proportional to the
        number of flights  written  in it,  and only
        one list 'lines' is allocated in memory.
    """

    direct = path+file

    with open(direct, 'r', encoding="utf-8") as doc:
        lines = doc.readlines()

    return lines


def split_lines(lines):
    """
    Input:
        lines: [str array] lines of the input file
    Output:
        airls: [str array] list of airlines
        dests: [str array] list of destinations
        pssgs: [int array] list of passngers numbers
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        The  aim  of  this  algorithm is to separate
        each of the columns: 'airline','destination'
        and 'number of passengers', while preserving
        the  ascending  alphabetical  order  of  the
        flights by 'airline' column. Since 'airline'
        and  'destination'  values  do  not  contain
        space-characters,  neither does  the integer
        'number of passengers',  we split  each line
        of the file  by  white-space  characters, in
        the same order  as  the lines were  imported
        from  the  file, to retrieve a tuple made of
        three items:
                    1. name of the airline [str]
                    2. destination [str]
                    3. number of passengers [int]

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage,  since we traverse the list 'lines'
        once,  while appending  each of the splitted
        line's  tuple  items  to their corresponding
        separated lists,'airls','dests' and 'pssgs',
        whereas  each  of  these  lists have as many
        entries as flights in the file.
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
        dests: [str array] list of destinations
    Output:
        cntr: [int] number of flights to "Frankfurt"
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        The aim  of  this algorithm is to  count the
        number  of  flights  with  destination value
        equal to "Frankfurt".  Now,  the flights are
        ordered with respect to the 'airline' column
        instead of  the 'destination' column,  so we
        cannot simply sum up consecutive occurrences
        of  destination  "Frankfurt"  in some binary
        search fashion, with, on  average, less than
        O(log n)  operations.  Any  sub-linear  time
        complexity  implementation  is   unfeasible,
        since, reordering the list by  'destination'
        column  will  take,  on average,  O(n log n)
        operations. Thus,  a linear  time-complexity
        implementation is prefered: notice the value
        "Frankfurt"  could  appear  anywhere  in the
        list 'dests', then, even in  the best linear
        implementation,  we  will  have to visit all
        elements in the list once, in order to  know
        whether to count them  or not   i.e   access
        every entry  in the list once,  to check  if
        its value  equals  "Frankfurt";  if it does,
        then update a counter of the number of times
        the destination "Frankfurt" appeared in  the
        list, increasing it by one unit.

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage,  since we traverse the list 'dests'
        only once, while this function allocates the
        storage for only one copy of list 'dests'.
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
        storage: O(n)
    Explanation:
        The aim  of  this algorithm is to  count the
        number  of  flights  with  destination value
        equal to "Frankfurt".  Now,  the flights are
        ordered with respect to the 'airline' column
        instead of the 'number of passngers' column,
        so the flights with the  minimum and maximum
        number  of  passengers  do  not  necessarily
        correspond to the first and last elements in
        the list,  respectively, and
        reordering the list by 'destination' would take  at worst
        O(n log n) operations. Thus, a linear time implementation
        is prefered:    considering that the maximum could appear
        anywhere in the list,   we have to keep record of a local
        maximum variable and its index, then do a linear scan through
        every element in the list,  so that if the element is greater
        than the current maximum, then it's updated with this element
        and the current index is reset.  Thus this implementation has
        a linear time and storage complexity on the number of flights.
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
        storage: O(n)
    Idea:
        Since  the flights are  ordered  by airline name,  instead of number
        of passengers  per flight, then  the first flight with less than 100
        passengers  can occur anywhere  in the list  and its position cannot
        be deduced  from its  surrounding entries.  Therefore,  we must loop
        through 'pssgs' until the first flight with less than 100 passengers
        is  found  or  the iterable index  exceeds the number of flights. In
        the worst case,  this element can be last of the list,  or can never
        occur  in the list.  Thus the best possible implementation must be a
        linear,  in time and  storage,  complexity algorithm,  on the number
        of flights.
    """

    indx = 0

    while indx < len(pssgs) and pssgs[indx] >= 100:
        indx += 1

    if indx >= len(pssgs):
        return -1

    if pssgs[indx] < 100:
        return indx

    return -1


def find_max_passengers_airline(airls, pssgs):
    """
    Input:
        airls: [str array] list of airlines for each flight
        pssgs: [int array] list of number of passengers for each flight
    Output:
        indx: [int] list index of airline with most total number of passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Idea:
        Since the flights are ordered by airline name, we can take advantage
        of the fact that that  all flights supported by the same airline are
        contiguous in the list. This way,  we sum consecutive entries, until
        the next entry corresponds to  a different airline, then we check if
        the  current sum is greater than  the greatest sum yet, stored  in a
        temp variable; if it does we reset the temp variable with the sum of
        the current airline. Thus, this implementation has a linear time and
        storage complexity on the number of flights.
    """

    if len(airls) == 1:
        return 0, pssgs[0]

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
        ans_exe_4: [tuple] airline with/and most total number of passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        This functions  implements the solution of the  problem_1
        assignment,  following  the convention and  format stated
        in the statement. This function is intented to be invoked
        from the main() function only, so that it can be modified
        without too much harm on the overall functionality.
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
        ans_exe_4 = ("The file is empty!", '')
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
        storage: O(n)
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
