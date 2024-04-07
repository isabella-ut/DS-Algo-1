
# first try
def gs_match_1(students_preferences, prof_preferences, places):
    matches = {}
    remaining_places = places.copy()  # Copying places here
    unmatched_students = []  # Added empty list for unmatched students

    free_students = list(students_preferences.keys())  # Initiate the student as free.

    while free_students:
        student = free_students.pop(0)  # Take and remove the first free student.
        if students_preferences[student]:  # Check if the student still has preferences.
            prof = students_preferences[student].pop(0)  # Take the first preference for the student.

            if prof not in matches or remaining_places[prof] > 0:  # If prof has free places.
                if prof not in matches:
                    matches[prof] = []
                matches[prof].append(student)
                remaining_places[prof] -= 1  # Decrement the available place.
            else:  # If prof is fully matched but may prefer this student more.
                current_matches = matches[prof]
                least_preferred = min(current_matches, key=lambda x: prof_preferences[prof].index(x))
                if prof_preferences[prof].index(student) < prof_preferences[prof].index(least_preferred):
                    free_students.append(least_preferred)  # Make the least preferred student free again.
                    current_matches.remove(least_preferred)  # Remove them from the current matches.
                    current_matches.append(student)  # Add the new preferred student.
        else:
            unmatched_students.append(student)  # **Modification**: Add student to unmatched if no more preferences left.

    # **New Addition**: Handle any professors who may not have been matched at all, due to students having limited preferences.
    for prof in places.keys():
        if prof not in matches:
            matches[prof] = []
            print(f"Professor {prof} has no matches due to limited student preferences.")

    print("Unmatched Students:", unmatched_students)
    return matches


#second try
def gs_match_2(students_preferences, prof_preferences, places):
    matches = {}
    remaining_places = places.copy() #Copying places here
    unmatched_students = [] #Added empty list for unmatched students

    free_student = list(
        students_preferences.keys())  # Initiate the student as free. Returns the keys from matching dictionary and transforms to list.

    while free_student:
        student = free_student.pop(
            0)  # .pop takes and removes the student at index 0 from the free students list. Assign to student, this equals S in the lecture.
        if students_preferences[student]: # Modified to loop to check whether a student unmatched
            prof = students_preferences[student].pop(
                0)  # Take the first preference of the first student. This is a professor, as it draws from the student preferences dictionary.
            #Added if-loop to check if professor has free places
            if prof not in matches:
                matches[prof] = [student]
                remaining_places[prof] -= 1 #Here we decrease places after match
            elif remaining_places[prof] > 0: #Here we match
                matches[prof].append(student)
                remaining_places[prof] -= 1
            else: #Here we matching students and profs
                prof_pref_list = prof_preferences[
                    prof]  # If professor is matched otherwise already, get the preferences of the prof. These contain names of students in order of preferences. Assign to variable.
                current_match = matches[prof][0]

                if prof_pref_list.index(current_match) > prof_pref_list.index(student): #and remaining_places[prof] >0:
                    # Check if the current match is higher than the current student, which was defined before and is free. Higher, as in index further to the right, so less preferable.
                    matches[prof] = student  # Final match, outcome of comparison, match and add prof with student.
                    free_student.append(
                        current_match)  # As new student is preferred over current match, current match is free again and appended to free list.
                    remaining_places[prof] =-1
                else:
                    free_student.append(student)  # Vice versa of above.
        else:
            unmatched_students.append(student)
    print("Unmatched Students:", unmatched_students)

    return matches
