"""
CBDataFrame class implementation.
"""

from src.cb_array import CBArray

# ------------------------------------- Please do NOT use extra import statements --------------------------------------


class CBArrayEasyMin(CBArray):
    """
    A subclass of `CBArray` that's capable of returning the minimal element in the array in constant run-time. Please
    make this implementation as efficient as possible, assuming that insertion, deletion and update happens in
    relatively lower frequency, but `get_min` method is called at a much higher frequency.
    """

    def __init__(self, content, dtype=None):
        super(CBArrayEasyMin, self).__init__(content, dtype)

        self.min = []

        if not self.content:
            pass
        else:
            for x in self.content:
                if not self.min or x <= self.get_min():
                    self.min.append(x)
                else:
                    self.min.insert(0, x)

    def get_min(self):
        """
        Get the min element of this array. If array is empty, return None.
        Run-time complexity must be O(1), space complexity must be less than or equal to O(n).
        :return: Min element in the array.
        """
        # implementation (do not use Python `min` function, since we assume its run-time complexity is O(n))
        if not self.min:
            return None
        else:
            return self.min[-1]

    # You can override any method you think necessary (please make them as time efficient as possible)
    def append(self, value):
        """
        Append a value to the end of the list.
        :param value: Value of new element.
        """
        # Check the data type of new element
        if not self.content:  # Content is empty
            if type(value) == self.Dtype:
                self.content.append(value)
                if not self.min or value <= self.get_min():
                    self.min.append(value)
                else:
                    self.min.insert(0, value)
            else:
                raise TypeError("Incorrect data type, {} argument expected".format(self.Dtype))
        else:  # Content is not empty
            if type(value) == self.Dtype:
                self.content.append(value)
                if not self.min or value <= self.get_min():
                    self.min.append(value)
            elif (type(value) == int and self.Dtype == float) or (type(value) == float and self.Dtype == int):
                self.content.append(value)
                if not self.min or value <= self.get_min():
                    self.min.append(value)
                else:
                    self.min.insert(0, value)
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
                    if not self.min or value <= self.get_min():
                        self.min.append(value)
                    else:
                        self.min.insert(0, value)
                else:
                    raise ValueError("Index exceeds the expected range")
            else:
                raise TypeError("Integer argument expected for index")
        elif type(value) == int and self.Dtype == float:  # Special Case: Can only insert int to a float list
            if type(idx) is int:
                if 0 <= idx <= len(self.content):
                    self.content.insert(idx, value)
                    if not self.min or value <= self.get_min():
                        self.min.append(value)
                    else:
                        self.min.insert(0, value)
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
                self.min.remove(value)

        elif type(value) == int and self.Dtype == float:  # Special Case: Can only remove int from a float list
            if value not in self.content:
                pass
            else:
                self.content.remove(value)
                self.min.remove(value)
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
                self.min = [item for item in self.min if item != value]
        elif type(value) == int and self.Dtype == float:  # Special Case: Can only remove int from a float list
            if value not in self.content:
                pass
            else:
                self.content = [item for item in self.content if item != value]
                self.min = [item for item in self.min if item != value]
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
            elif (self.Dtype == int and another_CBArray.Dtype == float) or (
                    self.Dtype == float and another_CBArray.Dtype == int):
                total_content = []
                total_content.extend(self.content)
                total_content.extend(another_CBArray.content)
                return CBArray(total_content, float)
            else:
                raise TypeError("Str CBArray cannot be concat with numeric CBArray")
        else:
            raise TypeError("Invalid argument type, CBArray argument expected")
