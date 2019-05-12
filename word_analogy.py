#!/usr/bin/env python3
import os
import sys
import math
import numpy

input_file_name = sys.argv[1]
input_directory_name = sys.argv[2]
output_directory_name = sys.argv[3]
eval_file_name = sys.argv[4]
should_normalize = sys.argv[5]
similarity_type = sys.argv[6]

#read in vector model
#store it as a dictionary

def get_vector_dict():
    vector_dict = {}
    with open(input_file_name, "r") as vector_file:
        for line in vector_file.readlines():
            spaced_line = line.split()
            element_list = spaced_line[1:]
            vector_dict[spaced_line[0]] = element_list
    return vector_dict


def get_magnitude(vector, vector_dict):                      #magnitude is the sum of each element squared
    magnitude_squared = 0
    if vector in vector_dict:
        elements = vector_dict[vector]
        for element in elements:
            element_squared = float(element)*float(element)
            magnitude_squared += element_squared
            magnitude = math.sqrt(magnitude_squared)
        return magnitude


def normalize(word):           #normalize the vectors by dividing by the magnitude BEFORE C + B - A
    if word in vector_dict:
        elements = vector_dict[word]
        normalized_elements = []
        vector_magnitude = get_magnitude(word, vector_dict)
        for element in elements:
            normalized_element = float(element)/vector_magnitude
            normalized_elements.append(normalized_element)
    return(normalized_elements)

def get_similarity(similarity_type):
    if similarity_type == 0:
        return 0 #use Euclidean distance
    if similarity_type == 1:
        return 1 #use Manhattan distance
    if similarity_type == 2:
        return 2 #use cosine distance

def get_euclidean_distance(vec1, vec2):
    element_difference_squared_list = [(vec1[i]-vec2[i])^2 for i in range(len(vec1))]
    euclidean_dist_squared = sum(element_difference_squared_list)
    euclidean_dist = math.sqrt(euclidean_dist_squared)
    return euclidean_dist

def get_manhattan_distance(vec1, vec2):
    element_difference_absval_list = [abs(vec1[i] - vec2[i]) for i in range(len(vec1))]
    manhattan_dist = sum(element_difference_absval_list)
    return manhattan_dist

def get_cosine_distance(vec1, vec2):
    element_product_list = [vec1[i] * vec2[i] for i in range(len(vec1))] #adapted from https://www.quora.com/How-do-I-get-Python-to-multiply-a-list-with-another-list
    dot_product = sum(element_product_list)
    mag_1 = get_magnitude(vec1, vector_dict)
    mag_2 = get_magnitude(vec2, vector_dict)
    cos_distance = dot_product/(mag_1*mag_2)
    return cos_distance



def solve_analogy(dirname):
    for file in os.listdir(dirname): #adapted from Justin's demo code
        if file[0] != "." and file.endswith(".txt"):
            with open(os.path.join(dirname, file), "r") as analogy_file:
                for line in analogy_file.readlines():
                    spaced_line = line.split()
                    analogy_abc = spaced_line[:3]
                    #print(analogy_abc)

vector_dict = get_vector_dict()
#solve_analogy("GoogleTestSet")
play_magnitude = get_magnitude("play", vector_dict)
print(play_magnitude)

normalize("play")

'''#testing normalizer func
sum = 0
for element in vector_dict["play"]:
    sum += float(element)*float(element)

print("sum: " + str(sum))'''

