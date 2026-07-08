def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    # ... Your code here ...
    try:
        iterator = iter(iterable)
        
        result = next(iterator)
        
        for item in iterator:
            result = function_to_apply(result, item)
            
        return result
        
    except (StopIteration, TypeError):
        return None