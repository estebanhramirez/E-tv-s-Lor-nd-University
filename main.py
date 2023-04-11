def exercise1(dest):
    """
    Input:
        dest: list of strings abstracting flights' destinations.
    Output:
        cntr: num of flights with destination "Frankfurt".
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        loop through the list once, so every time the destination
        "Frankfurt" is found update the count of the number of
        times it appears in the list.
    """

    #print("solving exercise 1..")
    cntr = 0
    for destination in dest:
        if destination == "Frankfurt":
            cntr += 1

    return cntr


def exercise2(pssg):
    """
    Input:
        pssg: list of ints abstracting number of passengers per each flight.
    Output:
        indx: list index of the corresponding flight with max # of passengers.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        Compare all elements in the list once with and update a max variable
        every time.
    """

    #print("solving exercise 2..")
    indx = 0
    maxi = 0
    for i, n_passenger in enumerate(pssg):
        if n_passenger > maxi:
            indx = i
            maxi = n_passenger
    return indx


def exercise3(pssg):
    """
    Input:
        pssg: list of ints abstracting number of passengers per each flight.
    Output:
        indx: list index of corresponding first flight with < 100 passengers.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        loop through the list until the first flight with < 100 passengers is
        found or the iterable index exceeds the list's size.
    """

    #print("solving exercise 3..")
    indx = 0
    while pssg[indx] >= 100 and indx < len(pssg):
        indx += 1
    if indx == len(pssg)-1:
        return -1
    return indx


def exercise4(airs, pssg):
    """
    Input:
        airs: list of strings abstracting airlines' names.
        pssg: list of ints abstracting number of passengers per each flight.
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

    #print("solving exercise 4..")
    indx = 0
    most = 0
    cntr = pssg[0]
    for i in range(1, len(airs)):
        if airs[i-1] != airs[i]:
            if cntr > most:
                indx = i
                most = cntr
            cntr = 0
        cntr += pssg[i]

    if cntr > most:
        indx = len(airs)-1
        most = cntr
    return indx, most


def main():
    #print("beggining of execution..")
    airs = ["Alitalia", "Alitalia", "Germanwings", "Germanwings", "NorwegianAir", "Wizzair", "Wizzair", "Wizzair"]
    dest = ["Rome", "Pisa", "Munich", "Frankfurt", "Bergen", "London", "Frankfurt", "Lisbon"]
    pssg = [180, 82, 96, 163, 202, 184, 83, 198]

    cntr1 = exercise1(dest)
    indx2 = exercise2(pssg)
    indx3 = exercise3(pssg)
    indx4, most4 = exercise4(airs, pssg)

    print(cntr1)
    print(airs[indx2], dest[indx2], pssg[indx2])
    print(airs[indx3], dest[indx3], pssg[indx3])
    print(airs[indx4], most4)


main()