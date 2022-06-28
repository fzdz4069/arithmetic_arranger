def arithmetic_arranger(problems, display=False):
    no_errors = None
    for problem in problems:
        a = problem.split()[0]
        op = problem.split()[1]
        b = problem.split()[2]
        if len(problems) > 5:
            print("Error: Too many problems.")
            no_errors = False
            break
        elif op != "+" and op != "-":
            print("Error: Operator must be '+' or '-'.")
            no_errors = False
            break
        elif not a.isnumeric() or not b.isnumeric():
            print("Error: Numbers must only contain digits.")
            no_errors = False
            break
        elif len(a) > 4 or len(b) > 4:
            print("Error: Numbers cannot be more than four digits.")
            no_errors = False
            break
        else:
            no_errors = True
    if no_errors:
        a = list()
        op = list()
        b = list()
        lines = list()
        args_a = list()
        args_b = list()
        for problem in problems:
            args_a.append(problem.split()[0])
        for problem in problems:
            op.append(problem.split()[1])
        for problem in problems:
            args_b.append(problem.split()[2])
        n = 0
        for problem in problems:
            spl = problem.split()
            if max(len(spl[0]), len(spl[2])) == 4:
                prt1 = "{:>6}"
                prt2 = op[n] + "{:>5}"
                line = "------"
                a.append(prt1)
                b.append(prt2)
                lines.append(line)
            elif max(len(spl[0]), len(spl[2])) == 3:
                prt1 = "{:>5}"
                prt2 = op[n] + "{:>4}"
                line = "-----"
                a.append(prt1)
                b.append(prt2)
                lines.append(line)
            elif max(len(spl[0]), len(spl[2])) == 2:
                prt1 = "{:>4}"
                prt2 = op[n] + "{:>3}"
                line = "----"
                a.append(prt1)
                b.append(prt2)
                lines.append(line)
            elif max(len(spl[0]), len(spl[2])) == 1:
                prt1 = "{:>3}"
                prt2 = op[n] + "{:>2}"
                line = "---"
                a.append(prt1)
                b.append(prt2)
                lines.append(line)
            n += 1
        m = 0
        for arg in a:
            print(arg.format(args_a[m]), end="    ")
            m += 1
        print("")

        k = 0
        for arg in b:
            print(arg.format(args_b[k]), end="    ")
            k += 1
        print("")

        for line in lines:
            print(line, end="    ")
        print("")
        if display:
            d = 0
            while d < len(problems):
                if op[d] == "+":
                    x = max(len(args_a[d]), len(args_b[d])) + 2
                    res = "{:>" + str(x) + "}"
                    print(res.format(str(int(args_a[d]) + int(args_b[d]))), end="    ")
                elif op[d] == "-":
                    x = max(len(args_a[d]), len(args_b[d])) + 2
                    res = "{:>" + str(x) + "}"
                    print(res.format(str(int(args_a[d]) - int(args_b[d]))), end="    ")
                d += 1
