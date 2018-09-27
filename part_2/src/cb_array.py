"""
CBArray class implementation.
"""

# ------------------------------------- Please do NOT use extra import statements --------------------------------------


class CBArray:
    """
    Array that contains elements with only one data type.
    """

    def __init__(self, content, dtype=None):
        """
        Initialize an array with a list of values.
        :param content: List of all values to initialize this array with. All values in the list should be of the same
        data type, otherwise it should throw an exception. Values cannot be None.
        :param dtype: Data type of array. If this argument is None, datatype will be inferred from values in `content`
        list (default `dtype` should be `int` if `content` is empty); if not, all values will be casted to specified
        type. CBArray should support the following data types: int, float, and str.
        """
        pass  # TODO: implementation

    @property
    def dtype(self):
        """
        :return: Data type of elements in the array.
        """
        pass  # TODO: implementation

    @property
    def size(self):
        """
        :return: Size of this array.
        """
        pass  # TODO: implementation 

    def append(self, value):
        """
        Append a value to the end of the list.
        :param value: Value of new element.
        """
        pass  # TODO: implementation

    def insert(self, idx, value):
        """
        Insert value at idx.
        :param idx: Index to insert value at.
        :param value: Element to insert.
        """
        pass  # TODO: implementation

    def remove(self, value):
        """
        Remove the first value in the array that is equal to `value`.
        :param value: Value to remove.
        """
        pass  # TODO: implementation

    def remove_all(self, value):
        """
        Remove all values in the array that is equal to `value`.
        :param value: Value to remove.
        """
        pass  # TODO: implementation

    # TODO: Implement appropriate methods so that CBArray also supports concatenation like Python list does:
    # arr1 = CBArray([1, 2, 3])
    # arr2 = CBArray([4, 5, 6])
    # arr3 = arr1 + arr2  # arr3 is CBArray([1, 2, 3, 4, 5, 6])
    # Note: Concatenating two CBArrays with dtype int and float should result in a CBArray with dtype float.

    # TODO: Implement appropriate methods so that CBArray also supports subscripting syntax like Python list does:
    # arr = CBArray([1, 2, 3])
    # arr[0]  # 1
    # arr[-1]  # 3
    # arr[-1:]  # CBArray([2, 3])
    # You do NOT need to support subscripting setters (i.e. arr[0] = 3)
