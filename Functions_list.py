""" These are the functions to calculate scores or produce result
from a dictionary of user responses.
Includes functions for CHADS score, CHADS-VASc score,
Post-code algorithm"""

#CHADS calculator function


def CHADS_score_dictionary_method(entries):
    chads_vasc_score = 0
    ## entries = response_dict

    print("Entries are:", entries)  # debug

    if entries['CHF'] == 1:
        chads_vasc_score += 1
    if entries['HTN'] == 1:
        chads_vasc_score += 1
    if entries['AGE > 75'] == 1:
        chads_vasc_score += 1
    if entries['Diabetes'] == 1:
        chads_vasc_score += 1
    if entries['Stroke_hx'] == 1:
        chads_vasc_score += 2


    print("\n\nCHADS score is: ", chads_vasc_score)
    return chads_vasc_score



#CHADSVASc calculator function


def CHADS_VASc_score_dictionary_method(dictionary):
    chads_vasc_score = 0
    entries = dictionary

    #  print(entries)

    if entries['CHF'] == 1:
        chads_vasc_score += 1
    if entries['HTN'] == 1:
        chads_vasc_score += 1
    if entries['AGE > 75'] == 1:
        chads_vasc_score += 2
    elif entries['AGE > 65'] == 1:
        chads_vasc_score += 1
    if entries['Diabetes'] == 1:
        chads_vasc_score += 1
    if entries['Stroke_hx'] == 1:
        chads_vasc_score += 2
    if entries['Vascular_dz'] == 1:
        chads_vasc_score += 1
    if entries['Female_gender'] == 1:
        chads_vasc_score += 1

    print("\n\nCHADS-VASc score is: ", chads_vasc_score)
    return chads_vasc_score



"""Post-code algorithm function"""


def Post_Code_Cath_algorithm(entries):

    true_list = []
    false_list = []
    null_list = []
    response_list = {}

    for key in entries:
        if entries[key] == 1:
            true_list.append(key)
        elif entries[key] == 0:
            false_list.append(key)
        else:
            null_list.append(key)

    # print("True list:", true_list)
    # print("False list:", false_list)
    # print("Null list:", null_list)
    response_list = {"True:": true_list, "False:": false_list, "Null:": null_list}

    print_recs = ""
    print_recs = "\n\nUnfavorable criteria include: " + str(response_list.get('True:'))
    print_recs = print_recs + "\nFavorable criteria include: " + str(response_list.get('False:'))
    print_recs = print_recs + "\nInvalid or absent factors:" + str(response_list.get('Null:'))


    print("\n\nUnfavorable criteria include: ", response_list.get('True:'))
    print("\nFavorable criteria include: ", response_list.get('False:'))
    print("\nInvalid or absent factors:", response_list.get('Null:'))

    if len(response_list.get('True:')) > 1:
        print_recs = print_recs + """\n\n Recommendations: \n\n 
        There are multiple unfavorable factors. \n
        "Immediate coronary angiography may not yield significant benefits."""

        print("\n\n")
        print("Recommendations: \n\nThere are multiple unfavorable factors. \n"
        "Immediate coronary angiography may not yield significant benefits.")

    return print_recs




"""  OLD code """
        # def CHADS_VASc_score_dictionary_method(entries):
        #     chads_vasc_score = 0
        #     # entries = response_dict
        #
        #     print("Entries are:", entries)  # debug
        #
        #     if entries['CHF'] == 1:
        #         chads_vasc_score += 1
        #     if entries['HTN'] == 1:
        #         chads_vasc_score += 1
        #     if entries['AGE > 75'] == 1:
        #         chads_vasc_score += 1
        #     if entries['Diabetes'] == 1:
        #         chads_vasc_score += 1
        #     if entries['Stroke_hx'] == 1:
        #         chads_vasc_score += 2
        #     # if entries['Vascular_Disease'] == 'Y':
        #     #     chads_vasc_score += 1
        #     # if entries['Female_Gender'] == 'Y':
        #     #     chads_vasc_score += 1
        #
        #     print("\n\nCHADS-VASc score is: ", chads_vasc_score)
        #     return chads_vasc_score