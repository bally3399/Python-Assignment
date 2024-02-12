class Test:
    def __init__(self):
        pass


    def generate_integer_list(self):
        return list(range(1, 16))
        pass

    def duplicate_list(self):
        list1 = list(range(1, 16))
        duplicated_list = []
        for x in list1:
            duplicated_list.append(x)
        return duplicated_list

    def remove_duplicates(self, lst):
        return list(set(lst))

    def add_every_third_element(self,lst):
        self.total = 0
        for idx in range(2, len(lst), 3):
            self.total += lst[idx]
        return self.total

    def sum_first_middle_last(self,array):
        middle_index = len(array) // 2
        self.total = array[0] + array[middle_index] + array[-1]
        return self.total

    def collect_elements(self, elements_list):
        elements = set(elements_list)
        self.unique_elements = set()
        for element in elements:
            self.unique_elements.add(element)
            if len(self.unique_elements) == 10:
                break
        return self.unique_elements

    def sum_elements(self, elements_list):
        elements = set(elements_list)
        self.unique_elements = elements
        self.total = 0
        for element in elements:
            self.total += element

        return self.total

    def remove_item(self, input_set, number):
        if number in input_set:
            input_set.remove(number)
            return number
        else:
            return None

    def find_intersection(self, set1, set2):
        intersection_set = set1.intersection(set2)
        return intersection_set



