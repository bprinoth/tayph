def nantest(var,varname=''):
    """This function tests for the presence of NaNs and infinites.

    Parameters
    ----------
    var : int, float or array-like
        The variable that needs to be tested.

    varname : str, optional
        Name or description of the variable to assist in debugging.

    """
    import numpy as np
    if np.isnan(var).any()  == True:
        raise Exception("NaN error: Variable %s contains NaNs but is not allowed to." % varname)
    if np.isinf(var).any()  == True:
        raise Exception("Finite error: Variable %s contains in-finite values but is not allowed to." % varname)




def postest(a,varname=''):
    """This function tests that all elements in the input variable are strictly positive.

    Parameters
    ----------
    var : int, float or array-like
        The variable that needs to be tested.

    varname : str, optional
        Name or description of the variable to assist in debugging.

    """
    import numpy as np
    if np.min(a) <= 0:
        raise Exception('Value error: Variable %s is only allowed to be strictly positive (%s).' % (varname,np.min(a)))



def notnegativetest(a,varname=''):
    """This function tests that all elements in the input variable are zero or positive.

    Parameters
    ----------
    var : int, float or array-like
        The variable that needs to be tested.

    varname : str, optional
        Name or description of the variable to assist in debugging.
    """
    import numpy as np
    if np.min(a) < 0:
        raise Exception('Value error: Variable %s is not allowed to be negative (%s).' % (varname,np.min(a)))





def typetest(var,vartype,varname=''):
    """This function tests the type of var against a requested variable type and raises an exception if either varname is not a string,
    or if type(var) is not equal to vartype. A list of vartypes can be supplied to test whether the type is any of a provided set (i.e. OR logic).

    Parameters
    ----------
    var : any variable
        The variable that needs to be tested.

    vartype : type, list
        A python class that would be identified with type(); or a list of classes.

    varname : str, optional
        Name or description of the variable to assist in debugging.
    """
    if isinstance(varname,str) != True:
        raise Exception("Input error in typetest: varname should be of type string.")

    if type(vartype) == list:
        trigger = 0
        for t in vartype:
            trigger+=isinstance(var,t)
        if trigger == 0:
            errormsg="Type error: Variable %s should be equal to any of " % varname
            for t in vartype:
                errormsg+=('%s,'%t)
            errormsg=errormsg[0:-1]+(' (%s)'%type(var))
            raise Exception(errormsg)
    else:
        if isinstance(var,vartype) != True:
            raise Exception("Type error: Variable %s should be equal to %s (%s)." % (varname,vartype,type(var)))



def typetest_array(var,vartype,varname=''):
    """This function tests the types of the elements in the array or list var against a requested variable type and raises an exception if either
    varname is not a string, type(var) is not equal to numpy.array or list, or the elements of
    var are not ALL of a type equal to vartype. A list of vartypes can be supplied to test whether the type is any of a provided set (i.e. OR logic)..

    Parameters
    ----------
    var : list, np.array
        A list of variables each of which will be tested against vartype.

    vartype : type, list
        A python class that would be identified with type(); or a list of classes.

    varname : str, optional
        Name or description of the variable to assist in debugging.
    """
    import numpy as np
    if isinstance(varname,str) != True:
        raise Exception("Input error in typetest: varname should be of type string.")
    typetest(var,[list,tuple,np.ndarray])
    # if (isinstance(var,list) != True) and (isinstance(var,np.ndarray) != True):
    #     raise Exception("Input error in typetest_array: %s should be of class list or numpy array." % varname)
    for i in range(0,len(var)):
        typetest(var[i],vartype,varname='element %s of %s' % (i,varname))





def dimtest(var,sizes,varname=''):
    """
    This function tests the dimensions and shape of the input array var.
    Sizes is the number of elements on each axis.

    Parameters
    ----------
    var : list, np.ndarray, array-like
        An array with certain dimensions.

    sizes : list, tuple, np.ndarray
        A list of dimensions (integers) to check var against.

    varname : str, optional
        Name or description of the variable to assist in debugging.

    Example
    -------
    >>>import numpy as np
    >>>a=[[1,2,3],[4,3,9]]
    >>>b=np.array(a)
    >>>dimtest(a,2,[2,3])
    >>>dimtest(a,2,[3,10])
    """
    import numpy as np
    typetest(sizes,[list,tuple,np.ndarray])
    typetest_array(sizes,[int,np.int64],varname='sizes in dimtest')
    typetest(varname,str)

    ndim=len(sizes)

    dimerror=0.0
    sizeerror=0.0
    if np.ndim(var) != ndim:
        raise Exception("Dimension error in %s:  ndim = %s but was required to be %s." % (varname,np.ndim(var),ndim))

    sizes_var=np.shape(var)

    for i in range(0,len(sizes)):
        if sizes[i] < 0:
            raise Exception("Input error in %s: Sizes was not set correctly. It contains negative values. (%s)" % (varname,sizes(i)))
        if sizes[i] > 0:
            if sizes[i] != sizes_var[i]:
                raise Exception("Dimension error in %s: Axis %s contains %s elements, but %s were required." % (varname,i,sizes_var[i],sizes[i]))