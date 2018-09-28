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
        # Condition: when type of argument `content` is not list
        if not isinstance(content, list):
            raise TypeError("List argument expected")
        # Condition: when any of values in `content` is None
        elif not all(content):
            raise ValueError("All values in the list cannot be None")
        else:
            self.type = "CBArray"
            self.content = content
            # Condition: if `dtype` argument is None
            if dtype is None:
                # Condition: if `content` is empty
                if not content:
                    self.Dtype = int
                elif all(isinstance(item, int) for item in content):
                    self.Dtype = int
                elif all(isinstance(item, float) for item in content):
                    self.Dtype = float
                elif all(isinstance(item, str) for item in content):
                    self.Dtype = str
            else:
                self.Dtype = dtype


    @property
    def dtype(self):
        """
        :return: Data type of elements in the array.
        """
        return self.Dtype

    @property
    def size(self):
        """
        :return: Size of this array.
        """
        return len(self.content)

    def append(self, value):
        """
        Append a value to the end of the list.
        :param value: Value of new element.
        """
        # Check the data type of new element
        if type(value) == self.Dtype:
            self.content.append(value)
        else:
            raise TypeError("Incorrect data type, {} argument expected".format(self.Dtype))

    def insert(self, idx, value):
        """
        Insert value at idx.
        :param idx: Index to insert value at.
        :param value: Element to insert.
        """
        if type(value) == self.Dtype:
            if type(idx) is int:
                self.content.insert(idx, value)
            else:
                raise TypeError("Integer argument expected for index")
        else:
            raise TypeError("Incorrect data type, {} argument expected".format(self.Dtype))

    def remove(self, value):
        """
        Remove the first value in the array that is equal to `value`.
        :param value: Value to remove.
        """
        self.content.remove(value)

    def remove_all(self, value):
        """
        Remove all values in the array that is equal to `value`.
        :param value: Value to remove.
        """
        self.content = [item for item in self.content if item != value]

    def __add__(self, another_CBArray):
        """
        # TODO: Implement appropriate methods so that CBArray also supports concatenation like Python list does:
        # arr1 = CBArray([1, 2, 3])
        # arr2 = CBArray([4, 5, 6])
        # arr3 = arr1 + arr2  # arr3 is CBArray([1, 2, 3, 4, 5, 6])
        # Note: Concatenating two CBArrays with dtype int and float should result in a CBArray with dtype float.
        """
        if another_CBArray.type == "CBArray":
            if self.Dtype == another_CBArray.Dtype:
                self.content.extend(another_CBArray.content)
        else:
            raise TypeError("Incorrect data type, CBArray argument expected")

    # TODO: Implement appropriate methods so that CBArray also supports subscripting syntax like Python list does:
    # arr = CBArray([1, 2, 3])
    # arr[0]  # 1
    # arr[-1]  # 3
    # arr[-1:]  # CBArray([2, 3])
    # You do NOT need to support subscripting setters (i.e. arr[0] = 3)
