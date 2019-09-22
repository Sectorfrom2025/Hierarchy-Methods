#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Lab №2 
#version 0.0.1

class Method_CI():
    
    def __init__(self, array, table_of_size):
        self.original_array = array 
        self.table_of_the_size = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.4, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
        
    def transforming_array(self, array_to_transform):
        return [list(x) for x in zip(*array_to_transform)]
    
    def developing_vector(self, original_array):
        summ_list = []
        maximum_value = 0
        for tmp_row in original_array:
            tmp_iterator = 0
            for tmp_element in tmp_row:
                tmp_iterator += tmp_element
            summ_list.append(tmp_iterator)
            maximum_value += tmp_iterator
        vector_list = [[tmp_element/maximum_value] for tmp_element in summ_list]
        return vector_list
    
    def rechanging_array(self, listing, index):
        tmp_list = []
        for tmp in range(0, len(listing), 1):
            tmp_listing = []
            if tmp != index:
                for tmp_element in range(0, len(listing[tmp]), 1):
                    if tmp_element != index:
                        tmp_listing.append(listing[tmp][tmp_element])
                tmp_list.append(tmp_listing)
        return tmp_list

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

    def making_ci_criterion_comparison(self, array_to_work_with):
        vector = self.developing_vector(array_to_work_with)
        one_value = [[1 for tmp in range(0, len(array_to_work_with), 1)]]
        first_multiplier = self.multiplying_arrays(one_value, array_to_work_with)
        lambda_max = round(self.multiplying_arrays(first_multiplier, vector)[0][0], 3)
        consistency_index = round((lambda_max - len(array_to_work_with))/(len(array_to_work_with) - 1), 2)
        consistency_ratio = round(consistency_index/self.table_of_the_size[len(array_to_work_with) - 1],2)
        return [lambda_max, consistency_index, consistency_ratio]
                    
    def calculating_ci_method(self):
        result_values = []
        values_of_original_array = self.making_ci_criterion_comparison(self.original_array)
#         print("Here are original value: ", values_of_original_array[1])
        new_array = []
        for tmp_element in range(0, len(self.original_array), 1):
            tmp_value = self.rechanging_array(self.original_array, tmp_element)
            new_array.append(self.making_ci_criterion_comparison(tmp_value)[1])
        result_values.append(new_array.index(min(new_array)) + 1)
        new_array.remove(min(new_array))
        result_values.append(new_array.index(min(new_array)) + 2)
        print("Wikid is element D", result_values[0], result_values[1])
        return result_values
    
class Method_correlation():
    
    def __init__(self, array):
        self.original_array = array
    
    def transforming_array(self, array_to_transform):
        return [list(x) for x in zip(*array_to_transform)]
    
    def middle_value(self, list_value):
        return sum(list_value)/len(list_value)
    
    def squad_middle_value(self, list_value):
        squad_value = 0
        middle = self.middle_value(list_value)
        for tmp_iterable in list_value:
            squad_value += (tmp_iterable - middle)**2
        return squad_value/(len(list_value) - 1)
    
    def calculating_new_values(self, x_vector, y_vector):
        tmp_summ = 0
        middle_x, middle_y = self.middle_value(x_vector), self.middle_value(y_vector)
        squad_middle_x, squad_middle_y = self.squad_middle_value(x_vector), self.squad_middle_value(y_vector)
        for tmp_value in range(0, len(x_vector), 1):
            tmp_summ += (x_vector[tmp_value] - middle_x)*(y_vector[tmp_value] - middle_y)
        tmp_summ /= (squad_middle_x * squad_middle_y)**0.5
        tmp_summ /= (len(x_vector) - 1)
        return tmp_summ
            
    def finding_min(self, vector_with_minimums):
        return (vector_with_minimums.index(min(vector_with_minimums)) + 1)
    
    def finding_correlation_coeficients(self, original_array):
        tmp_list_value = []
        tmp_iterator = 0
        while tmp_iterator < len(original_array):
            list_to_work_with = []
            list_tmp = original_array[tmp_iterator]
            for tmp_value in range(0, len(original_array), 1):
                list_to_correlate = original_array[tmp_value]
                value = 1
                if(tmp_iterator != tmp_value):
                    tmp_correlation = self.calculating_new_values(list_tmp, list_to_correlate)
                    value *= tmp_correlation
            tmp_list_value.append(value)
            tmp_iterator += 1
        return tmp_list_value
        
    def using_lists(self, original_list):
        x_list = self.finding_correlation_coeficients(original_list)
        y_list = self.finding_correlation_coeficients(self.transforming_array(original_list))
        x_list = self.finding_min(x_list)
        y_list = self.finding_min(y_list)
        return [x_list, y_list]
        
    def calculating_values(self):
        first = self.using_lists(self.original_array)
        print("Wikid is element D", first[1], first[0])
        return first
    
class Method_Xi_square():
    
    def __init__(self, array):
        self.original_array = array
        
    def developing_an_t_value(self, tmp_i, tmp_j):
        tmp_n = len(self.original_array)
        tmp_a = 0
        tmp_b = 0
        tmp_c = 0
        for tmp_k in range(0, tmp_n, 1):
            tmp_a += self.original_array[tmp_i][tmp_k]
        for tmp_l in range(0, tmp_n, 1):
            tmp_b += self.original_array[tmp_l][tmp_j]
        for tmp_k in range(0, tmp_n, 1):
            for tmp_l in range(0, tmp_n, 1):
                tmp_c += self.original_array[tmp_k][tmp_l]
        return (tmp_a * tmp_b) / tmp_c;
    
    def creating_xi_criterion(self):
        tmp_list = []
        for tmp_rows in range(0, len(self.original_array), 1):
            tmp_array = []
            for tmp_element in range(0, len(self.original_array), 1):
                tmp_exchange = self.developing_an_t_value(tmp_rows, tmp_element)
                tmp_array.append(((self.original_array[tmp_rows][tmp_element] - tmp_exchange)**2)/tmp_exchange)
            tmp_list.append(tmp_array)
        return tmp_list
    
    def developing_value(self):
        tmp_array = self.creating_xi_criterion()
        math_expectations = 0
        dispertion = 0
        for tmp_rows in tmp_array:
            for tmp_element in tmp_rows:
                math_expectations += tmp_element
        math_expectations /= len(tmp_array)**2
        square_dispertion = 0
        for tmp_rows in tmp_array:
            for tmp_element in tmp_rows:
                dispertion += (tmp_element - math_expectations)**2
        dispertion /= (len(tmp_array) - 1)**2
        square_dispertion = dispertion**0.5
        mini_delta = abs(tmp_array[0][0] - square_dispertion)
        mini_value = 0
        for tmp_rows in range(0, len(tmp_array), 1):
            for tmp_elements in range(0, len(tmp_array), 1):
                if abs(tmp_array[tmp_rows][tmp_elements] - square_dispertion) < mini_delta:
                    mini_delta = abs(tmp_array[tmp_rows][tmp_elements] - square_dispertion)
                    mini_value = tmp_array[tmp_rows][tmp_elements]
        for tmp_rows in range(0, len(tmp_array), 1):
            for tmp_elements in range(0, len(tmp_array), 1):
                if tmp_array[tmp_rows][tmp_elements] == mini_value:
                    result_values = [tmp_rows + 1, tmp_elements + 1]
                    print("Wikid is element D", result_values[0], result_values[1])
                    return result_values

class Automatic_correction(Method_CI):
    
    def __init__(self, array_to_work_with, alpha_values, table_of_the_size):
        self.original_array = array_to_work_with
        self.alpha_values = alpha_values
        self.table_of_the_size = table_of_the_size
        self.list_to_answer = []
        
    def norming_list(self, array_to_norm):
        tmp_weight_coefficients = []
        tmp_list = []
        tmp_list_of_lists = []
        for tmp_rows in array_to_norm:
            tmp_multiplier = 1
            for tmp_values in tmp_rows:
                tmp_multiplier *= tmp_values
            tmp_weight_coefficients.append(tmp_multiplier**(1/len(array_to_norm)))
        return tmp_weight_coefficients
        
    def wgmm_calculation(self, given_old_array, alpha, k):
        old_array = given_old_array
        tmp_weight_coefficients = self.norming_list(old_array)
        value_of_list = []
        for tmp_rows in range(0, len(old_array), 1):
            value_of_rows = []
            for tmp_element in range(0, len(old_array), 1):
                value = (old_array[tmp_rows][tmp_element]**alpha)
                value *= ((tmp_weight_coefficients[tmp_rows]/tmp_weight_coefficients[tmp_element])**(1-alpha))
                value_of_rows.append(value)
            value_of_list.append(value_of_rows)
        comparing = self.making_ci_criterion_comparison(value_of_list)
        if comparing[2] <= 0.1:
            maxi = abs(value_of_list[0][0] - self.original_array[0][0])
            sumi = 0
            for tmp_rows in range(0, len(value_of_list), 1):
                for tmp_elements in range(0, len(value_of_list), 1):
                    vali = (value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements])**2
                    vali = vali**0.5
                    sumi += vali
                    if abs(value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements]) > maxi:
                        maxi = abs(value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements])
            return [k, alpha, value_of_list, comparing[2], maxi, sumi/len(value_of_list)]
        return self.wgmm_calculation(value_of_list, alpha, k + 1)
    
    def wamm_calculation(self, given_old_array, alpha, k):
        old_array = given_old_array
        tmp_weight_coefficients = self.norming_list(old_array)
        value_of_list = []
        for tmp_rows in range(0, len(old_array), 1):
            value_of_rows = []
            for tmp_element in range(0, len(old_array), 1):
                if tmp_rows <= tmp_element:
                    value = alpha*old_array[tmp_rows][tmp_element]
                    value += (1 - alpha)*(tmp_weight_coefficients[tmp_rows]/tmp_weight_coefficients[tmp_element])
                    value_of_rows.append(value)
                else:
                    value = alpha*old_array[tmp_rows][tmp_element]
                    value += (1 - alpha)*(tmp_weight_coefficients[tmp_rows]/tmp_weight_coefficients[tmp_element])
                    value_of_rows.append(1/value)
            value_of_list.append(value_of_rows)
        comparing = self.making_ci_criterion_comparison(value_of_list)
        if comparing[2] <= 0.1:
            maxi = abs(value_of_list[0][0] - self.original_array[0][0])
            sumi = 0
            for tmp_rows in range(0, len(value_of_list), 1):
                for tmp_elements in range(0, len(value_of_list), 1):
                    vali = (value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements])**2
                    vali = vali**0.5
                    sumi += vali
                    if abs(value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements]) > maxi:
                        maxi = abs(value_of_list[tmp_rows][tmp_elements] - self.original_array[tmp_rows][tmp_elements])            
            a = [k, alpha, value_of_list, comparing[2], maxi, sumi/len(value_of_list)]
            return [k, alpha, value_of_list, comparing[2]]
        return self.wamm_calculation(value_of_list, alpha, k + 1)
    
    def main_calculations(self):
        first_value = self.making_ci_criterion_comparison(self.original_array)
        value_wamm = []
        value_wgmm = []
        finished_wamm = []
        finished_wgmm = []
        if first_value[2] <= 0.1:
            print(self.original_array, 'alpha = 0', 'k = 0')
        else:
            for tmp_alpha in alpha_values:
                value_wamm = self.wamm_calculation(self.original_array, tmp_alpha, 1)
                value_wgmm = self.wgmm_calculation(self.original_array, tmp_alpha, 1)
                finished_wamm.append(value_wamm)
                finished_wgmm.append(value_wgmm)
#         pprint.pprint(finished_wamm)
#         pprint.pprint(finished_wgmm)
        return finished_wamm, finished_wgmm
    
if __name__ == "__main__":
    taski_array = [[1, 1/3, 2, 1/4, 1, 1/2, 2],
                  [3, 1, 0.142, 0.75, 3, 1.5, 6],
                  [0.5, 7, 1, 0.125, 0.5, 0.25, 1],
                  [4, 1.3333, 8 , 1, 4, 2, 8],
                  [1, 1/3, 2, 0.25, 1, 0.5, 2],
                  [2, 2/3, 4, 0.5, 2, 1, 4],
                  [0.5, 0.167, 1, 0.125, 0.5, 0.25, 1]]
    task_array = [[1, 5, 3, 1/7, 6],
                 [1/5, 1, 1/3, 1, 1/3],
                 [1/3, 3, 1, 6, 3],
                 [7, 1, 1/6, 1, 1/3],
                 [1/6, 3, 1/3, 3, 1]]
    table_of_size = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.4, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
    alpha_values = [0.5, 0.6, 0.7, 0.8, 0.9]
    
    a = Method_CI(taski_array, table_of_size).calculating_ci_method()
    b = Method_correlation(taski_array).calculating_values()
    c = Method_Xi_square(taski_array).developing_value()
    d = Automatic_correction(taski_array, alpha_values, table_of_size).main_calculations()


# In[ ]:




