def combiner(*agrs, unique=False):

    """
    combiner(*agrs,unique=False):
    if unique is true then it must return unique instances without duplicates
    
    """
    result = ""
    for arg in agrs:
        if isinstance(str,int):
            result+=str(arg)
        elif isinstance(arg,str):
            result +=arg

    if unique:
        new_result=set(result)
        result="".join(new_result)

        return result



output=combiner('This','is',1,2,'string!' , unique=True)
print(output)

