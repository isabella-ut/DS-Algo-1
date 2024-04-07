import random
import functions
import gs
import gs_var2
import gs_places
import gs_places_copy
import gs_uneven

# random.seed(1)

# Example random

#Generated dummy names from https://catonmat.net/tools/generate-random-names
students = ['A', 'B', 'C', 'D', 'E', 'F']

#students = ['Willis Spicer', 'Darby Luciano', 'Sidney Coble', 'Leonel Goetz', 'Bilal Mansfield',
            #'Lisbeth Spurlock', 'Darien McDowell', 'Doris Heckman', 'Tariq Spivey', 'Erica McCloud']

professors = ['Prof. Varun Pugh', 'Prof. Silvia Mayfield', 'Prof. Jeffery Breeden']

stud_preferences = {}

for student in students:
    stud_preferences[student] = random.sample(professors, k=3)

#print(stud_preferences)

prof_preferences = {}

for professor in professors:
    prof_preferences[professor] = random.sample(students, k=6)

#print(prof_preferences)

places =  {
    'Prof. Varun Pugh': 3,
    'Prof. Silvia Mayfield': 1,
    'Prof. Jeffery Breeden': 1
}

#pairs = gs.gs_match(students_preferences = stud_preferences, prof_preferences = prof_preferences)

#print(pairs)

#gs_ver2 = StableMatching_v2()

#output_pr = gs_ver2.main(student_preferences=stud_preferences, prof_preferences=prof_preferences)

#print(output_pr)

#sec_var = gs_var2.stable_matching(student_preferences=stud_preferences, prof_preferences=prof_preferences)

#print(sec_var)

#Very confusing since it gives various results :((((
#Now it's clear - Daniel's algorithm is student oriented and Daniyar's is professor-oriented. That's why results are different

#{'Prof. Silvia Mayfield': 'Willis Spicer', 'Prof. Varun Pugh': 'Darby Luciano', 'Prof. Jeffery Breeden': 'Sidney Coble'}
#[['Sidney Coble', 'Prof. Varun Pugh'], ['Darby Luciano', 'Prof. Silvia Mayfield'], ['Willis Spicer', 'Prof. Jeffery Breeden']]





# Example 1: 6 students, 3 professors (5 spots), everyone ranks everyone

stud_preferences_1 = {
    'A': ['Prof. Breeden', 'Prof. Mayfield', 'Prof. Pugh'],
    'B': ['Prof. Breeden', 'Prof. Pugh', 'Prof. Mayfield'],
    'C': ['Prof. Pugh', 'Prof. Mayfield', 'Prof. Breeden'],
    'D': ['Prof. Breeden', 'Prof. Mayfield', 'Prof. Pugh'],
    'E': ['Prof. Pugh', 'Prof. Breeden', 'Prof. Mayfield'],
    'F': ['Prof. Pugh', 'Prof. Mayfield', 'Prof. Breeden']
}

prof_preferences_1 = {
    'Prof. Pugh': ['B', 'A', 'E', 'C', 'D', 'F'],
    'Prof. Mayfield': ['B', 'E', 'D', 'C', 'F', 'A'],
    'Prof. Breeden': ['D', 'B', 'C', 'E', 'A', 'F']
}

places_1 = {
    'Prof. Pugh': 3,
    'Prof. Mayfield': 1,
    'Prof. Breeden': 1
}

# answer should be:
# Prof. Breeden - D
# Prof. Mayfield - B
# Prof. Pugh - C, E, F
# Unmatched: A

v2 = gs_places.gs_match(students_preferences=stud_preferences_1, prof_preferences=prof_preferences_1, places=places_1)
print("Example 1 (v2):", v2) #not correct

v3 = gs_uneven.gs_match_2(students_preferences=stud_preferences_1, prof_preferences=prof_preferences_1, places=places_1)
print("Example 1 (v3):", v3) #not correct



# Example 2: 6 students, 5 professors (5 spots), students rank 3 professors and professors rank all students

stud_preferences_2 = {
    'A': ['Prof. Goetz', 'Prof. Coble', 'Prof. Pugh'],
    'B': ['Prof. Goetz', 'Prof. Pugh', 'Prof. Coble'],
    'C': ['Prof. Pugh', 'Prof. Coble', 'Prof. Goetz'],
    'D': ['Prof. Goetz', 'Prof. Breeden', 'Prof. Pugh'],
    'E': ['Prof. Mayfield', 'Prof. Goetz', 'Prof. Breeden'],
    'F': ['Prof. Pugh', 'Prof. Goetz', 'Prof. Mayfield']
}

prof_preferences_2 = {
    'Prof. Pugh': ['F', 'C', 'B', 'A', 'E', 'D'],
    'Prof. Mayfield': ['D', 'B', 'F', 'C', 'E', 'A'],
    'Prof. Breeden': ['D', 'B', 'C', 'E', 'A', 'F'],
    'Prof. Coble': ['F', 'E', 'C', 'A', 'B', 'D'],
    'Prof. Goetz': ['E', 'A', 'D', 'C', 'F', 'B']
}

places_2 = {
    'Prof. Pugh': 1,
    'Prof. Mayfield': 1,
    'Prof. Breeden': 1,
    'Prof. Coble': 1,
    'Prof. Goetz': 1
}

# answer should be:
# Prof. Pugh - F
# Prof. Mayfield - E
# Prof. Breeden - D
# Prof. Coble - C
# Prof. Goetz - A
# Unmatched: B

v2 = gs_places.gs_match(students_preferences=stud_preferences_2, prof_preferences=prof_preferences_2, places=places_2)
print("Example 2 (v2):", v2) #correct

v3 = gs_uneven.gs_match_2(students_preferences=stud_preferences_2, prof_preferences=prof_preferences_2, places=places_2)
print("Example 2 (v3):", v3) #not correct


