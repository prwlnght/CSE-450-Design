'''

Input: None
Output: set of .csvs of specific size with a random preference order

'''
import os
import pickle
import platform
import random

if platform.system() == 'Windows':
    import resources_windows as resources
else:
    import resources_unix as resources

number_of_students = 5
number_of_hospitals = 5

workspace_dir = resources.workspace_dir

save_dir = os.path.join(os.path.dirname(os.getcwd()), 'prog_assignment1', 'test_files')

# uncomment this after setting workspace dir in resources file
# save_dir = os.path.join(workspace_dir, 'prog_assignment1', 'test_files')


def generate_pickles(hm_hospitals=number_of_hospitals, hm_students=number_of_students, dir_to_save=save_dir):

    hospital_ids = ['h_' + str(x) for x in range(1, hm_hospitals+1)]
    student_ids = ['s_' + str(x) for x in range(1, hm_students+1)]

    hospital_prefs = {}
    for h in hospital_ids:
        # get a random ordering of 1 to x
        this_prefs = list(range(1, hm_students + 1))
        random.shuffle(this_prefs)
        hospital_prefs[h] = this_prefs

    student_prefs = {}
    for s in student_ids:
        this_prefs = list(range(1, hm_students + 1))
        random.shuffle(this_prefs)
        hospital_prefs[h] = this_prefs

    print(hospital_prefs)
    print(student_prefs)

    all_prefs = {}
    all_prefs['hospitals'] = hospital_prefs
    all_prefs['students'] = student_prefs

    print('Saving files to: ', dir_to_save)
    with open(os.path.join(dir_to_save,
                           'all_preferences_' + str(hm_hospitals) + '_' + str(hm_hospitals) + '.pkl'),
              'wb') as f1:
        pickle.dump(all_prefs, f1, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    generate_pickles(10, 10)
