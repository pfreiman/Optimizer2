"""
Holds the math and logic we need to compute our scores and recommendations.
Think of this like a tool box we are giving the main file, which builds the user interface
with this as the "brains".
"""

class CardiologyToolkit:
    def __init__(self):
        self.item = ""
        self.response_dict = {}
        self.result_text = ""
        self.current_function = ""
        self.showtext = ""
        self.__cl_CHADS = ['CHF', 'HTN', 'AGE > 75', 'Diabetes', 'Stroke_hx']
        self.__cl_CHADS_VASc = ['CHF', 'HTN', 'AGE > 75', 'Diabetes', 'Stroke_hx', 'Vascular_dz', 'AGE > 65', 'Female_gender']
        self.__cl_post_arrest = ['Unwitnessed', 'Ongoing CPR', 'ROSC_> 30 minutes', 'pH < 7.2', 'Non-cardiac cause', 'Initial rhythm non-VF', 'lactate > 7', 'No bystander COR', 'Age > 85', 'ESRD']

    def get_current_criteria_list(self):
        combo_item = self.item
        if combo_item == "CHADS score":
            criteria_list = self.__cl_CHADS
        elif combo_item == "CHADS-VASc score":
            criteria_list = self.__cl_CHADS_VASc
        elif combo_item == "Post-code algorithm":
            criteria_list = self.__cl_post_arrest
        else:
            criteria_list = []
        return criteria_list

    def get_current_score_or_rec_function(self):
        combo_item = self.item
        if combo_item == "CHADS score":
            current_function = self.__CHADS_score_dictionary_method(self.response_dict)
        elif combo_item == "CHADS-VASc score":
            current_function = self.__CHADS_VASc_score_dictionary_method(self.response_dict)
        elif combo_item == "Post-code algorithm":
            current_function = self.__Post_Code_Cath_algorithm(self.response_dict)
        return current_function


    def __CHADS_score_dictionary_method(self, entries):
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


    def __CHADS_VASc_score_dictionary_method(self, dictionary):
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


    def __Post_Code_Cath_algorithm(self, entries):

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
