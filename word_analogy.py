#!/usr/bin/env python3
import os
import sys
import math
import numpy

input_file_name = sys.argv[1]
input_directory_name = sys.argv[2]
output_directory_name = sys.argv[3]
eval_file_name = sys.argv[4]
should_normalize = int(sys.argv[5])
similarity_type = int(sys.argv[6])

#read in vector model
#store it as a dictionary

def get_vector_dict():
    vector_dict = {}
    with open(input_file_name, "r") as vector_file:
        for line in vector_file.readlines():
            spaced_line = line.split()
            element_list = spaced_line[1:]
            numpy_element_list = numpy.array(element_list, dtype=float)
            vector_dict[spaced_line[0]] = numpy_element_list
            if should_normalize == 0:
                continue
            elif should_normalize == 1:
                vector_dict[spaced_line[0]] = normalize(spaced_line[0], vector_dict)
            else:
                print("Invalid normalization value: expected 0 or 1")
                break
    return vector_dict


def get_magnitude(word, vector_dict):                      #magnitude is the sum of each element squared
    magnitude_squared = 0
    if word in vector_dict:
        elements = vector_dict[word]
        magnitude_squared = numpy.square(vector_dict[word])
        magnitude_sum = numpy.sum(magnitude_squared)
        magnitude = numpy.sqrt(magnitude_sum)
        '''for element in elements:
            element_squared = float(element)*float(element)
            magnitude_squared += element_squared 
            magnitude = math.sqrt(magnitude_squared)'''
        return magnitude


def normalize(word, vector_dict):           #normalize the vectors by dividing by the magnitude BEFORE C + B - A
    if word in vector_dict:
        vector_magnitude = get_magnitude(word, vector_dict)
        normalized_vector = vector_dict[word]/vector_magnitude
        '''elements = vector_dict[word]
        normalized_elements = []
        for element in elements:
            normalized_element = float(element)/vector_magnitude
            normalized_elements.append(normalized_element)'''
    return(normalized_vector)


def get_euclidean_distance(vec1, vec2):
    '''element_difference_squared_list = [(vec1[i]-vec2[i])^2 for i in range(len(vec1))]
    euclidean_dist_squared = sum(element_difference_squared_list)
    euclidean_dist = math.sqrt(euclidean_dist_squared)'''
    vec_difference_squared = numpy.square(vec1 - vec2) #not sure about this
    euclid_dist_squared = numpy.sum(vec_difference_squared)
    euclidean_dist = math.sqrt(euclid_dist_squared)
    return euclidean_dist

def get_manhattan_distance(vec1, vec2):
    '''element_difference_absval_list = [abs(vec1[i] - vec2[i]) for i in range(len(vec1))]
    manhattan_dist = sum(element_difference_absval_list)'''
    vec_difference = numpy.abs(vec1 - vec2)
    manhattan_dist = numpy.sum(vec_difference)
    return manhattan_dist

def get_cosine_distance(vec1, vec2):
    '''element_product_list = [vec1[i] * vec2[i] for i in range(len(vec1))] #adapted from https://www.quora.com/How-do-I-get-Python-to-multiply-a-list-with-another-list
    dot_product = sum(element_product_list)
    mag_1 = get_magnitude(vec1, vector_dict)
    mag_2 = get_magnitude(vec2, vector_dict)
    cos_distance = dot_product/(mag_1*mag_2)''' #my way, pre-numpy use
    cos_distance = vec1.dot(vec2)
    return cos_distance

def make_vector(word):
    if word in vector_dict:
        return vector_dict[word]
    else:
        return numpy.zeros(300)

def solve_analogy(dirname):
    overall_correct = 0
    overall_total = 0
    with open(eval_file_name, "w") as open_eval_file:
        for file in os.listdir(dirname): #adapted from Justin's demo code
            if file[0] != "." and file.endswith(".txt"):
                with open(os.path.join(dirname, file), "r") as analogy_file:
                    with open(os.path.join(output_directory_name, file), "w+") as analogy_output_file:
                        eval_correct_count = 0
                        eval_incorrect_count = 0
                        eval_total_count = 0
                        for line in analogy_file.readlines():
                            spaced_line = line.split()
                            analogy_abc = spaced_line[:3]

                            vector_a = make_vector(spaced_line[0])
                            vector_b = make_vector(spaced_line[1])
                            vector_c = make_vector(spaced_line[2]) #make a b and c into vectors

                            ideal_vector_d = vector_c + vector_b - vector_a # make an ideal d vector using c + b - a
                            if similarity_type == 0: #get Euclidean distance
                                shortest_distance = 1000
                                curr_word = ""
                                for word, vector in vector_dict.items():
                                    current_distance = get_euclidean_distance(vector, ideal_vector_d)
                                    if current_distance < shortest_distance:
                                        shortest_distance = current_distance
                                        curr_word = word
                             #write analogy_abc, curr_word, newline to identically named file in new directory
                                analogy_output_file.write(" ".join(analogy_abc) + " " + curr_word + "\n")

                            elif similarity_type == 1: #get manhattan distance
                                shortest_distance = 1000
                                curr_word = ""
                                for word, vector in vector_dict.items():
                                    current_distance = get_manhattan_distance(vector, ideal_vector_d)
                                    if current_distance < shortest_distance:
                                        shortest_distance = current_distance
                                        curr_word = word
                                #write analogy_abc, curr_word, newline to identically named file in new directory
                                analogy_output_file.write(" ".join(analogy_abc) + " " + curr_word + "\n")

                                #write analogy_abc, curr_word, newline to identically named file in new directory

                            elif similarity_type == 2: #get cosine distance
                                longest_distance = -1
                                curr_word = ""
                                for word, vector in vector_dict.items():
                                    current_distance = get_cosine_distance(vector, ideal_vector_d)
                                    if current_distance > longest_distance:
                                        longest_distance = current_distance
                                        curr_word = word
                                #write analogy_abc, curr_word, newline to identically named file in new directory
                                analogy_output_file.write(" ".join(analogy_abc) + " " + curr_word + "\n")

                                #write analogy_abc, curr_word, newline to identically named file in new directory

                            else:
                                print("Invalid similarity metric; please input 0, 1, or 2")
                                break

                            if curr_word.lower() != spaced_line[3].lower():
                                eval_incorrect_count += 1
                            elif curr_word.lower() == spaced_line[3].lower():
                                eval_correct_count += 1

                            eval_total_count += 1
                        overall_correct += eval_correct_count
                        overall_total += eval_total_count
                        percentage = eval_correct_count/eval_total_count
                        open_eval_file.write("ACCURACY TOP1: " + str(percentage) + " " + "(" + str(eval_correct_count) + "/" + str(eval_total_count) + ")" + "\n" + file + "\n")
        open_eval_file.write("Total accuracy: " + str(overall_correct/overall_total) + " " + "(" + str(overall_correct) + "/" + str(overall_total) + ")" )

                    #last steps above: given a similarity metric,
                    #find the closest vector in the dictionary to ideal d
                    #write a b c and the d I found to file

#main
vector_dict = get_vector_dict()
solve_analogy(input_directory_name)





