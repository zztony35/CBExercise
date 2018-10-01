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
            raise TypeError("Invalid argument type, list argument expected")
        # Condition: when any of values in `content` is None
        elif not all(content):
            raise ValueError("All values in the list cannot be None")

        else:
            self.Dtype = dtype
            self.type = "CBArray"

            if not content:  # Condition: if `content` is empty
                self.content = []
                if dtype is None:
                    self.Dtype = int

            elif all(isinstance(item, int) for item in content):
                self.content = content
                if dtype is None:
                    self.Dtype = int
                elif dtype != int and dtype != float:
                    raise ValueError("Incorrect dtype input")

            elif not all(isinstance(item, int) for item in content) and all(
                    isinstance(item, (int, float)) for item in content):
                self.content = content
                if dtype is None:
                    self.Dtype = float
                elif dtype != float:
                    raise ValueError("Incorrect dtype input")

            elif all(isinstance(item, str) for item in content):
                self.content = content
                if dtype is None:
                    self.Dtype = str
                elif dtype != str:
                    raise ValueError("Incorrect dtype input")

            else:
                raise ValueError("Invalid argument type")

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
        if not self.content:  # Content is empty
            if type(value) == self.Dtype:
                self.content.append(value)
            else:
                raise TypeError("Incorrect data type, {} argument expected".format(self.Dtype))
        else:  # Content is not empty
            if type(value) == self.Dtype:
                self.content.append(value)
            elif (type(value) == int and self.Dtype == float) or (type(value) == float and self.Dtype == int):
                self.content.append(value)
                self.Dtype == float
            else:
                raise TypeError("Incorrect data type, {} argument expected".format(self.Dtype))

    def insert(self, idx, value):
        """
        Insert value at idx.
        :param idx: Index to insert value at.
        :param value: Element to insert.
        """
        if type(value) == self.Dtype:
            if type(idx) is int:  # Only support idx to be a non-negative integer
                if 0 <= idx <= len(self.content):
                    self.content.insert(idx, value)
                else:
                    raise ValueError("Index exceeds the expected range")
            else:
                raise TypeError("Integer argument expected for index")
        elif type(value) == int and self.Dtype == float:  # Special Case: Can only insert int to a float list
            if type(idx) is int:
                if 0 <= idx <= len(self.content):
                    self.content.insert(idx, value)
                else:
                    raise ValueError("Index exceeds the expected range")
            else:
                raise TypeError("Integer argument expected for index")
        else:
            raise TypeError("Invalid argument type, {} argument expected".format(self.Dtype))

    def remove(self, value):
        """
        Remove the first value in the array that is equal to `value`.
        :param value: Value to remove.
        """
        if type(value) == self.Dtype:
            if value not in self.content:
                pass
            else:
                self.content.remove(value)
        elif type(value) == int and self.Dtype == float:  # Special Case: Can only remove int from a float list
            if value not in self.content:
                pass
            else:
                self.content.remove(value)
        else:
            raise TypeError("Invalid argument type")

    def remove_all(self, value):
        """
        Remove all values in the array that is equal to `value`.
        :param value: Value to remove.
        """
        if type(value) == self.Dtype:
            if value not in self.content:
                pass
            else:
                self.content = [item for item in self.content if item != value]
        elif type(value) == int and self.Dtype == float:  # Special Case: Can only remove int from a float list
            if value not in self.content:
                pass
            else:
                self.content = [item for item in self.content if item != value]
        else:
            raise TypeError("Invalid argument type")

    def __add__(self, another_CBArray):
        """
        # Implement appropriate methods so that CBArray also supports concatenation like Python list does:
        # arr1 = CBArray([1, 2, 3])
        # arr2 = CBArray([4, 5, 6])
        # arr3 = arr1 + arr2  # arr3 is CBArray([1, 2, 3, 4, 5, 6])
        # Note: Concatenating two CBArrays with dtype int and float should result in a CBArray with dtype float.
        """
        if another_CBArray.type == "CBArray":
            if self.Dtype == another_CBArray.Dtype:
                total_content = []
                total_content.extend(self.content)
                total_content.extend(another_CBArray.content)
                return CBArray(total_content, self.Dtype)
            elif (self.Dtype == int and another_CBArray.Dtype == float) or (self.Dtype == float and another_CBArray.Dtype == int):
                total_content = []
                total_content.extend(self.content)
                total_content.extend(another_CBArray.content)
                return CBArray(total_content, float)
            else:
                raise TypeError("Str CBArray cannot be concat with numeric CBArray")
        else:
            raise TypeError("Invalid argument type, CBArray argument expected")

    def __getitem__(self, key):
        """
        # Implement appropriate methods so that CBArray also supports subscripting syntax like Python list does:
        # arr = CBArray([1, 2, 3])
        # arr[0]  # 1
        # arr[-1]  # 3
        # arr[-1:]  # CBArray([2, 3])
        # ??? arr[-1:] -> CBArray([3])
        # You do NOT need to support subscripting setters (i.e. arr[0] = 3)
        """
        if isinstance(key, slice):
            # slice.indices method. Given the length of your sequence, it returns a tuple of start, stop, step:
            sliced_content = [self.content[ii] for ii in range(*key.indices(len(self.content)))]
            return CBArray(sliced_content, self.Dtype)
        elif isinstance(key, int):
            if key < 0:  # Handle negative indices
                key += len(self.content)
            if key < 0 or key >= len(self.content):
                raise IndexError("The index {} is out of range".format(key))
            return self.content[key]  # Get the data from content
        else:
            raise TypeError("Invalid argument type")

