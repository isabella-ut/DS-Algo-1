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


