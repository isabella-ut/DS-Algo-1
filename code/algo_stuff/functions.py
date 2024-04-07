import pandas as pd
import random



#1. Create a function to create a list of students and professors


def create_data(num_students, num_profs):
    # Set a number of students and professors, where s < p
    
    # Create empty lists to append into
    students_list = []
    profs_list = []
    
    # Loop through the number of students and professors and append to the lists
    # Each list should have a structure of 'student_#' or 'prof_#' etc.
    for i in range(num_students):
        students_list.append('student_' + str(i))
    for i in range(num_profs):
        profs_list.append('prof_' + str(i))
    
    # Return lists
    return students_list, profs_list

# function to create preferences in one, nxn and with characters instead of names.
def create_n_n(n):
    # Initiate empty dictionary to store the preferences
    preferences = {}
    
    # loop through the range of n and create preferences X Y Z for students A B C.
    for i in n:
        student = chr(65 + i) # 65 in ASCII is A etc. + i in range(n) for all.
        random.shuffle(list(range(n))) # make it random
        preference_list = [chr(88 + j) for j in list(range(n))] # same logic for the actual preferences from X on
        preferences[student] = preference_list
    return preferences# assign preferences value to each student key of the dictionary.


#2. Create a function to randomly assign students to professors. We speficy a maximum number of students per professor as an additional argument.


def random_assignment(student_list, prof_list, max_num):
    # Initialize an empty dictionary to store the assignments
    assignments = {}
    
    # Loop through the professors and assign a random number of students to each professor
    for prof in prof_list:
        assignments[prof] = random.sample(student_list, random.randint(1, max_num))
        
    return assignments


#3. Create a function to randomly assign preferences for each student and professor.


def preferences(students_profs):
    # Create empty dictionary to store the preferences
    preferences = {}
    
    # Loop through student/prof list to assign random preferences
    # Loop through the length of the first list in the list of lists. This is important, as stundent names and prof names will be combined into one list of lists.
    for i in range(len(students_profs[0])):
        # For [0][i]Make sure to start at ith item in the list at index 0. With the current directions, this is the first student in the student list within the list of lists.
        # Add 'preferences' in front, as this is our dictionary key we initiated before.
        # Now, just use 'random' to assign a radnom preference for each student and each prof, with input data from the list of lists.
        preferences[students_profs[0][i]] = sorted(students_profs[1], key=lambda x: random.random())
    
    # Return the dictionary
    return preferences







# Function to verify stability of the algorithms
# This is not working 100% yet

def verify_stability(student_preferences, prof_preferences, matches, places):
    # Check for each student
    for student, prefs in student_preferences.items():
        matched_prof = None
        for prof in prefs:
            if student in matches.get(prof, []):
                matched_prof = prof
                break
        if matched_prof is None:
            continue  # Student is unmatched, no stability issue here
        # Check if there's a higher-ranked prof that would prefer this student
        for higher_ranked_prof in prefs[:prefs.index(matched_prof)]:
            # Check if higher-ranked prof would prefer this student over current matches
            current_matches = matches.get(higher_ranked_prof, [])
            if not current_matches or prof_preferences[higher_ranked_prof].index(student) < min(
                    prof_preferences[higher_ranked_prof].index(s) for s in current_matches):
                print(f"Instability found: {student} prefers {higher_ranked_prof} over {matched_prof}")
                return False

    # Check for each professor's preference stability
    for prof, current_matches in matches.items():
        if len(current_matches) < places[prof]:
            continue  # Professor hasn't filled their quota, no issue here
        least_preferred = min(current_matches, key=lambda x: prof_preferences[prof].index(x))
        for student in [s for s in prof_preferences[prof] if s not in current_matches]:
            if prof_preferences[prof].index(student) < prof_preferences[prof].index(least_preferred):
                print(f"Instability found: {prof} would prefer {student} over {least_preferred}")
                return False

    print("No instability found. The matching is stable.")
    return True

