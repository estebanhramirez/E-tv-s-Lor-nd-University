def interface(path='./', file='input.txt'):
    """
    Input:
        path: string specifying the path towards the file.
        file: string specifying the name of the file.
    Output:
        lines: list of strings corresponding to each raw line in the input file.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        given a file called "file", by default "input.txt", at the
        current directory, i.e path = "./", read each line in the
        file once, while storing their content into a list of strings.
    """

    #print("uploading external file..")
    with open(path+file, 'r', encoding="utf-8") as doc:
        lines = doc.readlines()
    return lines


def sanitize_input(lines):
    """
    Input:
        lines: list of strings corresponding to each raw line in the input file.
    Output:
        airls: list of strings corresponding to the airline name of each flight.
        dests: list of strings corresponding to the destinations of each flight.
        pssgs: list of ints corresponding to the number of passengers of each flight.
    Complexity:
        time: O(n).
        space: O(n).
    Idea:
        read each line in the file once, while storing it content
        into a list of strings.
    """

    #print("sanitizing input lines..")
    airls = []
    dests = []
    pssgs = []
    for line in lines:
        airl, dest, pssg = line.split(' ')
        airls.append(airl)
        dests.append(dest)
        pssgs.append(int(pssg))
    return airls, dests, pssgs


def exercise1(dests):
    """
    Input:
        dests: list of strings abstracting flights' destinations.
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
    for dest in dests:
        if dest == "Frankfurt":
            cntr += 1

    return cntr


def exercise2(pssgs):
    """
    Input:
        pssgs: list of ints abstracting number of passengers per each flight.
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

    #print("solving exercise 3..")
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

    #print("solving exercise 4..")
    indx = -1
    most = 0
    cntr = pssgs[0]
    for i in range(1, len(airls)):
        if airls[i-1] != airls[i]:
            if cntr > most:
                indx = i
                most = cntr
            cntr = 0
        cntr += pssgs[i]

    if cntr > most:
        indx = len(airls)-1
        most = cntr
    return indx, most


def solution(verbose=True):
    print()
    lines = interface()
    airls, dests, pssgs = sanitize_input(lines)

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


def main():
    #print("beggining of execution..")
    solution()


main()