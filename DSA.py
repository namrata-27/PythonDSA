
def findUnique(arr):
    """
    This function finds the unique elements in a list.
    Set is used to remove duplicates.
    It converts the list to a set and then back to a list.
    :param arr: List of elements
    :return: List of unique elements
    """
    return list(set(arr))

def findDuplicates(arr):    
    """
    This function finds the duplicate elements in a list.
    
    :param arr: List of elements
    :return: List of duplicate elements
    """
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def findIntersection(arr1, arr2):
    """
    This function finds the intersection of two lists.
    & It uses set intersection operation to find common elements.
    It converts both lists to sets and finds the common elements.
    :param arr1: First list of elements
    :param arr2: Second list of elements
    :return: List of elements that are in both lists
    """
    return list(set(arr1) & set(arr2))      

def findUnion(arr1, arr2):
    """
    This function finds the union of two lists.
    | It combines both lists and removes duplicates.
    It uses set union operation to find unique elements in both lists.
    :param arr1: First list of elements
    :param arr2: Second list of elements
    :return: List of elements that are in either list
    """
    return list(set(arr1) | set(arr2))

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]    
if __name__ == "__main__":
    print("Unique elements:", findUnique(array1 + array2))
    print("Duplicate elements:", findDuplicates(array1 + array2))
    print("Intersection:", findIntersection(array1, array2))
    print("Union:", findUnion(array1, array2))