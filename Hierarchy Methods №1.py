#!/usr/bin/env python
# coding: utf-8

# In[107]:


#Analytic Hierarchy Process - AHP
#version 0.0.1

class AHP():
    
    def __init__(self):
        self.size = 0
        self.value = [[ 1, 1/3, 1/2], [ 3, 1, 3], [2, 1/3, 1]]
        self.table_of_the_size = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.4, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
        
    def multiplying_arrays(self, array_first, array_second):
        multiplied_array = []
        for tmp_i in range(0, len(array_first), 1):
            multiplied_element = []
            for tmp_j in range(0, len(array_second[0]), 1):
                multiply = 0
                for tmp_k in range(0, len(array_first[0]), 1):
                    multiply += array_first[tmp_i][tmp_k] * array_second[tmp_k][tmp_j]
                multiplied_element.append(multiply)
            multiplied_array.append(multiplied_element)
        return multiplied_array
    
    def developing_vector_from_array(self, array_to_vector):
        vector_for_values = []
        for tmp_list in array_to_vector:
            tmp_variable = 0
            for tmp_element in tmp_list:
                tmp_variable += tmp_element
            vector_for_values.append(tmp_variable)
        value_to_normalize = 0
        for tmp in vector_for_values:
            value_to_normalize += tmp
        value_list_normalized = []
        for tmp_element in vector_for_values:
                value_list_normalized.append([tmp_element/value_to_normalize])
        print("a: ", value_list_normalized)
        return value_list_normalized
        
    def developing_an_array(self, array):
        self.size = len(self.value)
        value_list_normalized = self.developing_vector_from_array(self.value)
        first_multiplier = self.multiplying_arrays([[1,1,1]], self.value)
        lambda_max = self.multiplying_arrays(first_multiplier, value_list_normalized)
        return lambda_max[0][0]
        
    def finding_characteristics_of_the_task(self):
        lambda_max = round(self.developing_an_array(self.value), 2)
        consistency_index = round((lambda_max - self.size)/(self.size - 1),2)
        consistency_ratio = round(consistency_index/self.table_of_the_size[self.size - 1],2)
        return lambda_max, consistency_index, consistency_ratio
    
    def checking_indexes(self):
        lambda_max, consistency_index, consistency_ratio = self.finding_characteristics_of_the_task()
        size_checker = { 3 : 0.05, 4: 0.08, 5: 0.1}
        for key, value in size_checker.items():
            if self.size == key and consistency_index <= value:
                print('All values fit into this conception very well, current values are:\n lambda = ', 
                      lambda_max,'\n','CI = ', consistency_index,'\n', 'CR = ', consistency_ratio)
                return True
            elif (self.size >5 and consistency_index <= size_checker[5]) or (self.size < 3 and consistency_index <= size_checker[3]):
                print("That's not so bad data usagecurrent values are:\n lambda = ", 
                      lambda_max,'\n','CI = ', consistency_index,'\n', 'CR = ', consistency_ratio)
                return True
            else:
                return False
            

class Hierarchy_level(AHP):
    
    def __init__(self, m, p):
        self.m = m
        self.p = p
        self.tables_first =  [[[1, 6, 4], 
                               [1/6, 1, 3], 
                               [1/4, 1/3, 1]]]
        
        self.tables_second = [[[ 1, 6, 6, 3], 
                               [1/6, 1, 4, 3], 
                               [1/6, 1/4, 1, 1/2],
                               [1/3, 1/3, 2, 1]], 
                              [[ 1, 6, 6, 3], 
                               [1/6, 1, 4, 3], 
                               [1/6, 1/4, 1, 1/2],
                               [1/3, 1/3, 2, 1]],
                              [[ 1, 1/5, 1/3, 1], 
                               [5, 1, 4, 1/5], 
                               [3, 1/4, 1, 1/4],
                               [1, 5, 4, 1]]]
        
        self.tables_third = [[[ 1, 9, 4],
                              [1/9, 1, 8],
                              [ 1/4, 1/8, 1]], 
                             [[ 1, 1, 1],
                              [ 1, 1, 1], 
                              [ 1, 1, 1]], 
                             [[ 1, 9, 6], 
                              [1/9, 1, 1/4], 
                              [1/6, 4, 1]], 
                             [[ 1, 5, 5],
                              [1/5, 1, 1/3], 
                              [ 1/5, 3, 1]]]
        
        self.tables_usage = [self.tables_first, self.tables_second, self.tables_third]

    def transforming_array(self, array_to_transform):
        return [list(x) for x in zip(*array_to_transform)]
        
    def developing_vector_from_array(self, array_to_make_as_vector):
        final_result = []
        array_of_summs = []
        for tmp_arrays in array_to_make_as_vector:
            array_of_insight = []
            for tmp_rows in tmp_arrays:
                tmp_value = 0
                length = 0
                for tmp_elements in tmp_rows:
                    tmp_value += tmp_elements
                array_of_insight.append(tmp_value)
                for tmp in array_of_insight:
                    length += tmp
            array_of_summs.append(length)
        list_of_vectors = []
        for tmp_arrays in range(0, len(array_to_make_as_vector)):
            list_of_current_vector = []
            for tmp_rows in array_to_make_as_vector[tmp_arrays]:
                tmp_iterator = 0
                for tmp_elements in tmp_rows:
                    tmp_iterator += tmp_elements
                list_of_current_vector.append(tmp_iterator/array_of_summs[tmp_arrays])
            list_of_vectors.append(list_of_current_vector)
        final_result = self.transforming_array(list_of_vectors)
        return final_result
    
    def developing_arrays_to_multiply(self):
        array_with_result = []
        for tmp in self.tables_usage:
            variable_to_multiply = self.developing_vector_from_array(tmp)
            array_with_result.append(variable_to_multiply)
        result = self.multiplying_arrays(array_with_result[len(array_with_result) - 1], array_with_result[len(array_with_result) - 2])
        for tmp_iterable in range( len(array_with_result) - 2, 0, -2):
            result = self.multiplying_arrays(result, array_with_result[tmp_iterable - 1])
        return result

if __name__ == "__main__":
    list_of_result = Hierarchy_level(3, [1,3,4]).developing_arrays_to_multiply()
    print("Your result is:")
    for tmp in list_of_result:
        print(tmp[0])


# In[ ]:




