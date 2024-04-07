def gs_match(student_preferences, prof_preferences, places):
    matches = {}
    remaining_places = places.copy()  # Copying places here
    unmatched_students = []  # Added empty list for unmatched students

    free_students = list(student_preferences.keys())  # Initiate the student as free.

    while free_students:
        student = free_students.pop(0)  # Take and remove the first free student.
        if student_preferences[student]:  # Check if the student still has preferences.
            prof = student_preferences[student].pop(0)  # Take the first preference for the student.

            if prof not in matches or remaining_places[prof] > 0:  # If prof has free places.
                if prof not in matches:
                    matches[prof] = []
                matches[prof].append(student)
                remaining_places[prof] -= 1  # Decrement the available place.
            else:  # If prof is fully matched but may prefer this student more.
                current_matches = matches[prof]
                # Changed logic to correctly handle multiple students matched to a professor
                least_preferred = min(current_matches, key=lambda x: prof_preferences[prof].index(x))
                if prof_preferences[prof].index(student) < prof_preferences[prof].index(least_preferred):
                    free_students.append(least_preferred)  # Make the least preferred student free again.
                    current_matches.remove(least_preferred)  # Remove them from the current matches.
                    current_matches.append(student)  # Add the new preferred student.
                    # No need to adjust remaining_places[prof] here as we're swapping students
        else:
            unmatched_students.append(student)  # Add student to unmatched if no more preferences left.

    print("Unmatched Students:", unmatched_students)
    return matches

# Example preferences and places
student_pref = {
    'A': ['a', 'b', 'c'],
    'B': ['a', 'c', 'b'],
    'C': ['b', 'a', 'c']
}

prof_pref = {
    'a': ['B', 'A', 'C'],
    'b': ['A', 'C', 'B'],
    'c': ['C', 'B', 'A'],
    'd': []
}

place = {
    'a': 3,
    'b': 2,
    'c': 2
}

# Execute the matching
matches = gs_match(student_preferences=student_pref, prof_preferences=prof_pref, places=place)
print(matches)
