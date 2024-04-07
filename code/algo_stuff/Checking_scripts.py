import random
import gs
import gs_var2
import gs_places
import gs_places_copy
import gs_uneven


#Generated dummy names from https://catonmat.net/tools/generate-random-names
students = ['A', 'B', 'C', 'D', 'E', 'F']

#students = ['Willis Spicer', 'Darby Luciano', 'Sidney Coble', 'Leonel Goetz', 'Bilal Mansfield',
            #'Lisbeth Spurlock', 'Darien McDowell', 'Doris Heckman', 'Tariq Spivey', 'Erica McCloud']

professors = ['Prof. Varun Pugh', 'Prof. Silvia Mayfield', 'Prof. Jeffery Breeden']

stud_preferences = {}

for student in students:
    stud_preferences[student] = random.sample(professors, k=3)

# print(stud_preferences)

prof_preferences = {}

for professor in professors:
    prof_preferences[professor] = random.sample(students, k=6)

# print(prof_preferences)

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

third_var = gs_places.gs_match(students_preferences=stud_preferences, prof_preferences=prof_preferences,
                               places=places)

# print(third_var)






# check limited/uneven pref

students_2 = ['A', 'B', 'C', 'D', 'E', 'F']
professors_2 = ['Prof. Pugh', 'Prof. Mayfield', 'Prof. Breeden']

# Generate student preferences with each student ranking a subset (3) of the available professors
stud_preferences_2 = {student: random.sample(professors_2, k=3) for student in students_2}
print("Student Preferences (2):", stud_preferences_2)

# Generate professor preferences with each professor having a preference list of students
prof_preferences_2 = {professor: random.sample(students_2, len(students_2)) for professor in professors_2}
print("Professor Preferences (2):", prof_preferences_2)

# Define the available places for each professor
places_2 = {
    'Prof. Pugh': 3,
    'Prof. Mayfield': 2,  # Adjusted to ensure some professors can accept multiple students
    'Prof. Breeden': 1
}


# Use the second version of gs (with different spots by professor but before uneven/limited preferences)
spots_v2 = gs_places_copy.gs_match(student_preferences=stud_preferences_2, prof_preferences=prof_preferences_2, places=places_2)
print("Matching Results (spots):", spots_v2)

# Use the third version of gs to perform the matching for uneven/limited preferences for students
limited_v3 = gs_uneven.gs_match(student_preferences=stud_preferences_2, prof_preferences=prof_preferences_2, places=places_2)
print("Matching Results (limited pref):", limited_v3)





