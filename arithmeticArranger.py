def arithmetic_arranger(problems,viewResults = False):
    if (len(problems)> 5):
        return "Error: Too many problems."
    
    arranged_problems = []
    
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 = ""
    #aca arranco con las comprobaciones
    #---------------------------////-----------------------------------------------------------------
    for problem in problems:
        termino = problem.split(" ")
        
        if termino[1] != "+" and termino[1] != "-":
            return "Error: Operator must be '+' or '-'."
        
        if len(termino[0])>4 or len(termino[-1])>4:
                return "Error: Numbers cannot be more than four digits."
            
        try:
            n1 = int(termino[0])
            n2 = int(termino[-1])
        except:
            return "Error: Numbers must only contain digits."
        
    # termino las comprobaciones y empiezo a asjuntar al string
    #--------------------------------*/////----------------------------------------------------------------
        operator = termino[1]
        res = 0
        if operator == "+":
            res = n1+n2
        else:
            res = n1-n2


        arranged_problems.append(res)
        ns1 = str(n1)
        ns2 = str(n2)
        maxlen = max(len(ns1),len(ns2))
        
        if (problem != problems[-1]):
            linea1 += ns1.rjust(maxlen+2," ") + "    "
            linea2 += operator + " "+ns2.rjust(maxlen," ")+ "    "
            linea3 += f"{'-'* ((maxlen)+2) }" + "    "
            if viewResults:
                linea4 += f"{str(res).rjust((maxlen)+2)}" + "    "
        else:
            linea1 += ns1.rjust(maxlen+2," ")
            linea2 += operator + " "+ ns2.rjust(maxlen," ")
            linea3 += f"{'-'* ((maxlen)+2) }"
            if viewResults:
                linea4 += f"{str(res).rjust((maxlen)+2)}"
    
    
    string = ""
    if viewResults:
        string+=linea1 + "\n" + linea2+ "\n" + linea3+ "\n" + linea4
    else:
        string+=linea1 + "\n" + linea2+ "\n" + linea3
        
    
    return string
print(arithmetic_arranger(['24 + 852', '3801 - 2', '45 + 43', '123 + 49'],True))