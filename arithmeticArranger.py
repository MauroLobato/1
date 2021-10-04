def arithmetic_arranger(problems,viewResults = False):
    if (len(problems)> 5):
        return "Error: Too many problems."
    
    arranged_problems = []
    str_list = []
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
        
        operator = termino[1]
        res = 0
        if operator == "+":
            res = n1+n2
        else:
            res = n1-n2

        arranged_problems.append(res)
        ns1 = str(n1)
        ns2 = str(n2)
        
        resultado = ""
        statment = ""
        if (viewResults):
            resultado = res
            statment = (f"""
                {str(n1).rjust((max(len(ns1),len(ns2))+2)," ")}
                {operator} {str(n2).rjust((max(len(ns1),len(ns2)))," ")}
                {"-"*(max(len(ns1),len(ns2))+2)}
                {str(resultado).rjust((max(len(ns1),len(ns2))+2)," ")}
                """)
            
        else:
            statment = (f"""
                {str(n1).rjust((max(len(ns1),len(ns2))+2)," ")}
                {operator} {str(n2).rjust((max(len(ns1),len(ns2)))," ")}
                {"-"*(max(len(ns1),len(ns2))+2)}
                """)
            
        str_list.append(statment)
        
    print(str_list)    
    for stat in str_list:
        print(stat,end="")    

    return arranged_problems
arithmetic_arranger(['24 + 852', '3801 - 2', '45 + 43', '123 + 49'])