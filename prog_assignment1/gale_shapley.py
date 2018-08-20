'''
copyright @cse 450 Arizona State University




'''

import os
import pickle


def gale_shapley_matching(hospital_prefs, student_prefs):

    '''implement gale-shapley stable matching here '''

    ordered_hostpital_prefs = hospital_prefs
    ordered_student_prefs = student_prefs

    return ordered_hostpital_prefs, ordered_student_prefs


'''



'''


def run_unit_tests(in_file):
    with open (in_file, 'rb') as f:
        pref_dict = pickle.load(f)

    #Each pickle file will have the hospital preferences as a dictionary and the student preferences as a dictionary
    hospital_prefs = pref_dict['hospitals']
    student_prefs = pref_dict['students']

    ordered_hospital_prefs, ordered_students_prefs = gale_shapley_matching(hospital_prefs, student_prefs)

    print(ordered_hospital_prefs, ordered_hospital_prefs)


if __name__ == '__main__':
    run_unit_tests(os.path.join('test_files', 'all_preferences_10_10.pkl'))
