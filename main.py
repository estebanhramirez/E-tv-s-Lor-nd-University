"""
    Title: PROBLEM 1 Assignment solution.
    Author: Esteban Hernandez Ramirez.
    Date: April 2023.
    GitHub repository:
        HTTPS: https://github.com/estebanhramirez/Eotvos-Lorand-University.git
        SSH: git@github.com:estebanhramirez/Eotvos-Lorand-University.git
"""


def import_flights(path='./', file='input.txt'):
    """
    Input:
        path: [str] path towards the input file
        file: [str] name of the input file
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
        character ('\n'), to get the list of rows in
        the file i.e flights. Moreover this approach
        preserves the relative order of the file, as
        each row in it is read in the same order  as
        it was written in the file (top-to-bottom).

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage, since the file is read once and the
        size  of  the  file  is  proportional to the
        number of rows  (i.e flights)  in  the file,
        while  only storage for one list 'lines'  is
        allocated in memory,   whereas this list has
        as many entries as rows (i.e flights) in the
        file. "row" or "line" is used interchangibly
    """

    direct = path+file
    lines = []

    try:
        with open(direct, 'r', encoding="utf-8") as doc:
            lines = doc.readlines()
    except FileNotFoundError:
        print("¡FILE NOT FOUND! please, change the 'path' variable in main()")

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
        try:
            airl, dest, pssg = line.split()
        except ValueError:
            pass
        else:
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
        pssgs: [int array] list of passngers numbers
    Output:
        indx: [int] list index  of  the  flight with
                    the most number of passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        The aim  of  this algorithm is  to find  the
        index, in  the  list, of the flight with the
        most number of passengers. Now,  flights are
        ordered with respect to the 'airline' column
        instead of the 'number of passngers' column,
        so the flights with the  minimum and maximum
        number  of  passengers  do  not  necessarily
        correspond to the first and last elements in
        the list, respectively,  so we cannot simply
        take  the  last  element  as  the  number of
        passengers corresponding to  the flight with
        most number of passengers, in  O(1) time. As
        a matter of fact,  for an unsorted list  any
        sub-linear time complexity implementation is
        unfeasible, since reordering the list by the
        'number of passngers'  column will take,  on
        average,  O(n log n)  operations.   Thus,  a
        linear  time  complexity  implementation  is
        prefered:  notice that  the maximum of  list
        'pssgs'  can occur anywhere in the list,  so
        we keep track of  a  local maximum  variable
        and its index,  then a  linear scan  through
        the list garantees that once the entire list
        has  been  traversed,  the  local maximum is
        the global maximum. So every  element in the
        list is checked  and  if it is the case that
        a element is greater than the local maximum,
        then  it's updated with this element and the
        current index is reset to its index.

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage,  since we traverse the list 'pssgs'
        only once, while this function allocates the
        storage for only one copy of list 'pssgs'.
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
        pssgs: [int array] list of passngers numbers
    Output:
        indx: [int] list index of first flight  with
                    less than 100 passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Idea:
        The aim  of  this algorithm is  to find  the
        index,  in  the  list  'pssgs', of the first
        flight  with  less than 100 passengers. Now,
        flights  are  ordered  with  respect  to the
        'airline' column instead of  the  'number of
        passengers' column, so the first flight with
        less than 100 passengers  can occur anywhere
        in  the  list  and  its  position  cannot be
        deduced from its surrounding entries i.e the
        position of a flight  is  not  determined by
        its number of passengers. In the worst case,
        this element can be last of the list, or can
        never  occur  in the list at all. Therefore,
        the  best  possible  implementation  must be
        linear, since  we  must loop through 'pssgs'
        until  the  first  flight with less than 100
        passengers is found  or  the iterable  index
        exceeds the number of flights.

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage,  since we traverse the list 'pssgs'
        at most once,  while this function allocates
        storage for only one copy of list 'pssgs'.
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
        airls: [str array] list of airlines
        pssgs: [int array] list of passngers numbers
    Output:
        indx: [int] list index  of  the airline with
                    most total number  of passengers
        most: [int] most total number  of passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Idea:
        The aim of this algorithm is to find a index
        for  the  airline with the most total number
        of passengers. Since, the flights are sorted
        with respect to the 'airline' column, we can
        take  advantage  of  the  fact that that all
        flights  supported  by  the same airline are
        contiguous in  the lists.  This way,  we can
        sum consecutive entries of the list 'pssgs',
        until  the next entry  of  the  list 'airls'
        corresponds to a different airline,  then we
        check if the current sum is greater than the
        greatest sum yet, stored in a temp variable;
        if it is, we  reset  the  temp variable with
        the sum of the current airline and  reset an
        auxiliar variable, storing the  index of the
        last entry added to the sum.

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage, since we,  simultaniously, traverse
        the lists 'airls'  and  'pssgs' once,  while
        this function  allocates  storage  for  only
        one  copy  of  list 'airls' and one copy  of
        list 'pssgs'.
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


def solve_problem_1(path, file):
    """
    Input:
        path: [str] path towards the input file
        file: [str] name of the input file
    Output:
        ans_ex_1: [int] number of flights to the
                        destination "Frankfurt"
        ans_ex_2: [str] flight with  the most number
                        of passengers
        ans_ex_3: [str] first flight  with less than
                        100 passengers
        ans_ex_4: [str,int] airline with most  total
                            number of passengers and
                            the number of passengers
    Complexity:
        time: O(n)
        storage: O(n)
    Explanation:
        This  function  implements  the  solution of
        the  problem  1  assignment,  following  the
        convention and  format stated in the problem
        statement.  This function  is intented to be
        invoked from the main function only, so that
        it  can be modified without too much harm on
        the overall functionality.

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage,  inherited from  the functions that
        are invoked inside this function:

            1. count_to_frankfurt_flights [O(n)] 
            2. find_max_passengers_flight [O(n)]
            3. find_first_less_100_flight [O(n)]
            4. find_max_passengers_airline [O(n)]
    """

    lines = import_flights(path, file)

    airls, dests, pssgs = split_lines(lines)

    cntr_to_frankfurt_flights = count_to_frankfurt_flights(dests)
    idx_max_passengers_flight = find_max_passengers_flight(pssgs)
    idx_first_less_100_flight = find_first_less_100_flight(pssgs)
    idx_max_passenger_airline, cnt = find_max_passengers_airline(airls, pssgs)

    ans_ex_1 = cntr_to_frankfurt_flights
    ans_ex_2 = ""
    ans_ex_3 = ""
    ans_ex_4 = None

    if idx_max_passengers_flight == -1:
        ans_ex_2 += "The file is empty!"
    else:
        ans_ex_2 += airls[idx_max_passengers_flight] + ' '
        ans_ex_2 += dests[idx_max_passengers_flight] + ' '
        ans_ex_2 += str(pssgs[idx_max_passengers_flight])

    if idx_first_less_100_flight == -1:
        ans_ex_3 += "There is no flight with passengers less than 100."
    else:
        ans_ex_3 += airls[idx_first_less_100_flight] + ' '
        ans_ex_3 += dests[idx_first_less_100_flight] + ' '
        ans_ex_3 += str(pssgs[idx_first_less_100_flight])

    if idx_max_passenger_airline == -1:
        ans_ex_4 = ("The file is empty!", '')
    else:
        ans_ex_4 = (airls[idx_max_passenger_airline], cnt)

    return (ans_ex_1, ans_ex_2, ans_ex_3, ans_ex_4)


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

        This  algorithm  has a  linear complexity on
        the  number of flights,  both  in time   and
        storage, inherited from the function that is
        invoked inside this function:

            1. solve_problem_1 [O(n)]
    """

    path='./'
    file='input.txt'

    ans_ex_1, ans_ex_2, ans_ex_3, ans_ex_4 = solve_problem_1(path, file)

    print(ans_ex_1)
    print(ans_ex_2)
    print(ans_ex_3)
    print(ans_ex_4[0], ans_ex_4[1])

    return 0


#BEGINNING OF EXECUTION
main()
