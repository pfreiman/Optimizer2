"""
Holds the math and logic we need to compute our scores and recommendations.
Think of this like a tool box we are giving the main file, which builds the user interface
with this as the "brains".
"""


class CardiologyToolkit:
    def __init__(self):
        self.item = ""
        self.response_dict_checkboxes = {}
        self.response_dict_radiobuttons = {}
        self.response_dict_numerical = {}
        self.questions_dict = {}
        self.result_for_current_function = ""
        self.result_text = ""
        self.display_long_text = ""  # text for long display on results window

        self.set_of_checkbox_questions = {"CHADS score", "CHADS-VASc score", "Post-code algorithm", "HAS-BLED score",
                                          "Pre-op evaluation", "Sgarbossa criteria", "TIMI score ACS"}
        self.set_of_radiobutton_questions = {"HEART score", "Pre-op evaluation"}
        self.set_of_numerical_input_questions = {"QTc interval"}

        self.heart_score_criteria = {
            'History': ('Slightly suspicious', 'Moderately suspicious', 'Highly suspicious'),
            'EKG': ('No changes', 'Non-specific repolarization abnormality', 'Significant ST deviation'),
            'Age': ('<45', '45-64', '>=65'),
            'Risk factors': ('None', '1-2 risk factors', '>=3 risk factors'),
            'Troponin': ('Normal', '1-3 x normal', '> 3 x normal')
        }

        self.combobox_scores_options_list = ["", "CHADS score", "CHADS-VASc score", "HAS-BLED score",
                                             "HEART score", "QTc interval", "Sgarbossa criteria", "TIMI score ACS"]
        self.combobox_clinical_scenarios_options_list = ["", "Pre-op evaluation", "Post-code algorithm"]

        self.__cl_CHADS = ['CHF', 'HTN', 'AGE > 75', 'Diabetes', 'Stroke_hx']
        self.__cl_CHADS_VASc = ['CHF', 'HTN', 'AGE > 75', 'Diabetes', 'Stroke_hx', 'Vascular_dz', 'AGE > 65',
                                'Female_gender']
        self.__cl_post_arrest = ['Unwitnessed', 'Ongoing CPR', 'ROSC_> 30 minutes', 'pH < 7.2', 'Non-cardiac cause',
                                 'Initial rhythm non-VF', 'lactate > 7', 'No bystander CPR', 'Age > 85', 'ESRD']
        self.__cl_HAS_BLED = ['HTN', 'Renal dz', 'Liver dz', 'Stroke hx', 'Prior bleeding', 'Labile INR', 'Age > 65',
                              'High risk meds', 'Alcohol use']
        self.__cl_QTc = ["Enter QT interval (in msec)", "Enter RR' interval (in msec)"]
        self.__cl_Pre_op_checkboxes = ['Is this emergency surgery?', 'Acute coronary syndrome?']
        self.cl_Pre_op_criteria_radiobuttons = {
            "Surgical risk": ('Low risk', 'Elevated risk'),
            "Functional capacity": (' < 4 METS or unknown ', ' 4-10 METS ', ' > 10 METS ')}
        self.__cl_Sgarbossa_criteria = ["Concordant ST elevation", "Concordant ST depression in V1-V3",
                                        "Proportionally excessive discordant ST elevation in >= one lead"]
        self.__cl_TIMI_ACS = ["Age > 65", "Used aspirin within the last week", "2 or more angina episodes in last 24 hrs",
                              "Elevated cardiac biomarkers", "ST segment deviation on EKG",
                              "Known coronary artery disease", "3 or more risk factors"]


    def get_current_criteria_list(self):
        combo_item = self.item
        if combo_item == "CHADS score":
            criteria_list = self.__cl_CHADS
        elif combo_item == "CHADS-VASc score":
            criteria_list = self.__cl_CHADS_VASc
        elif combo_item == "Post-code algorithm":
            criteria_list = self.__cl_post_arrest
        elif combo_item == "HAS-BLED score":
            criteria_list = self.__cl_HAS_BLED
        elif combo_item == "QTc interval":
            criteria_list = self.__cl_QTc
        elif combo_item == "Pre-op evaluation":
            criteria_list = self.__cl_Pre_op_checkboxes
        elif combo_item == "Sgarbossa criteria":
            criteria_list = self.__cl_Sgarbossa_criteria
        elif combo_item == "TIMI score ACS":
            criteria_list = self.__cl_TIMI_ACS
        else:
            criteria_list = []
        return criteria_list

    def get_current_questions_dict(self):
        combo_item = self.item
        questions_dict = {}
        if combo_item == "HEART score":
            questions_dict = self.heart_score_criteria
        elif combo_item == "Pre-op evaluation":
            questions_dict = self.cl_Pre_op_criteria_radiobuttons
        return questions_dict

    def get_result_for_current_function(self):
        combo_item = self.item

        if combo_item == "CHADS score":
            result_for_current_function = self.__CHADS_score_dictionary_method(self.response_dict_checkboxes)
        elif combo_item == "CHADS-VASc score":
            result_for_current_function = self.__CHADS_VASc_score_dictionary_method(self.response_dict_checkboxes)
        elif combo_item == "Post-code algorithm":
            result_for_current_function = self.__Post_Code_Cath_algorithm(self.response_dict_checkboxes)
        elif combo_item == "HAS-BLED score":
            result_for_current_function = self.__HAS_BLED(self.response_dict_checkboxes)
        elif combo_item == "HEART score":
            result_for_current_function = self.__heart_score(self.response_dict_radiobuttons)
        elif combo_item == "QTc interval":
            result_for_current_function = self.__QTc_calculator(self.response_dict_numerical)
        elif combo_item == "Pre-op evaluation":
            result_for_current_function = self.__pre_op_evaluation(self.response_dict_checkboxes,
                                                                   self.response_dict_radiobuttons)
        elif combo_item == "Sgarbossa criteria":
            result_for_current_function = self.__smith_modified_sgarbossa_criteria(self.response_dict_checkboxes)
        elif combo_item == "TIMI score ACS":
            result_for_current_function = self.__TIMI_score_ACS(self.response_dict_checkboxes)
        print("result:", result_for_current_function)
        return result_for_current_function

    def long_button_command(self):  # opens text file and prepares text to place in results label

        item = self.item

        if item == "CHADS score":
            textfile = "CHADS_text"
        elif item == "CHADS-VASc score":
            textfile = "CHADSVASc_text"
        elif item == "Post-code algorithm":
            textfile = "Postcode_algorithm_text"
        elif item == "HAS-BLED score":
            textfile = "HAS_BLED_text"
        elif item == "HEART score":
            textfile = "HEART_score_text"
        elif item == "TIMI score ACS":
            textfile = "TIMI_score_ACS_text_long"

        fh = open(textfile, 'r')

        display_long_text = ""

        for line in fh:
            display_long_text = display_long_text + line

        return display_long_text

    def open_details_window(self):

        win_details = self.Toplevel(win_results)
        win_details.self.title("Additional details")
        win_details.self.geometry('800x800')
        win_details.self.resizable(True, True)

        win_details.self.mainloop()

    def __CHADS_score_dictionary_method(self, entries):
        chads_vasc_score = 0

        print("CHADS Entries are:", entries)

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

    # CHADSVASc calculator function

    def __CHADS_VASc_score_dictionary_method(self, entries):
        chads_vasc_score = 0

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
            Immediate coronary angiography may not yield significant benefits."""

            print("\n\n")
            print("""Recommendations: \n\nThere are multiple unfavorable factors. \n
            Immediate coronary angiography may not yield significant benefits.""")

        return print_recs

    # HAS-BLED function

    def __HAS_BLED(self, entries):
        has_bled_score = 0

        if entries['HTN'] == 1:
            has_bled_score += 1
        if entries['Renal dz'] == 1:
            has_bled_score += 1
        if entries['Liver dz'] == 1:
            has_bled_score += 1
        elif entries['Stroke hx'] == 1:
            has_bled_score += 1
        if entries['Prior bleeding'] == 1:
            has_bled_score += 1
        if entries['Labile INR'] == 1:
            has_bled_score += 2
        if entries['Age > 65'] == 1:
            has_bled_score += 1
        if entries['High risk meds'] == 1:
            has_bled_score += 1
        if entries['Alcohol use'] == 1:
            has_bled_score += 1

        print("\n\nHAS-BLED score is: ", has_bled_score)
        return has_bled_score

    # HEART score function

    def __heart_score(self, entries):
        heart_score = 0

        if entries['History'] == "Slightly suspicious":
            heart_score += 0
        elif entries['History'] == "Moderately suspicious":
            heart_score += 1
        elif entries['History'] == "Highly suspicious":
            heart_score += 2

        if entries['EKG'] == "No changes":
            heart_score += 0
        elif entries['EKG'] == "Non-specific repolarization abnormality":
            heart_score += 1
        elif entries['EKG'] == "Significant ST deviation":
            heart_score += 2

        if entries['Age'] == "<45":
            heart_score += 0
        elif entries['Age'] == "45-64":
            heart_score += 1
        elif entries['Age'] == ">=65":
            heart_score += 2

        if entries['Risk factors'] == "None":
            heart_score += 0
        elif entries['Risk factors'] == "1-2 risk factors":
            heart_score += 1
        elif entries['Risk factors'] == ">=3 risk factors":
            heart_score += 2

        if entries['Troponin'] == "Normal":
            heart_score += 0
        elif entries['Troponin'] == "1-3 x normal":
            heart_score += 1
        elif entries['Troponin'] == "> 3 x normal":
            heart_score += 2

        print("\n\nHEART score is: ", heart_score)
        return heart_score

    # QTc calculator function

    def __QTc_calculator(self, entries):
        qtc_interval = (entries["Enter QT interval (in msec)"] / (
                    (entries["Enter RR' interval (in msec)"] / 1000) ** (1 / 2)))
        qtc_interval = round(qtc_interval)
        print("QTc is:", qtc_interval)
        return qtc_interval

    def __pre_op_evaluation(self, entries_checkboxes, entries_radiobuttons):
        print("RD cb is: ", entries_checkboxes)
        print("RD rb is: ", entries_radiobuttons)

        if entries_checkboxes['Is this emergency surgery?'] == 1:
            recommendation = "Recommendation:  Clinical risk stratification and proceed to surgery."
            return recommendation
        elif entries_checkboxes['Acute coronary syndrome?'] == 1:
            recommendation = "Recommendation:  Evaluate and treat according to GDMT."
            return recommendation
        elif entries_radiobuttons["Surgical risk"] == "Low":
            recommendation = "Recommendation:  No further testing (class III).  Proceed to surgery."
            return recommendation
        elif entries_radiobuttons["Surgical risk"] == "Elevated risk":
            if entries_radiobuttons["Functional capacity"] == ' < 4 METS or unknown ':
                recommendation = "Recommendation:  If further testing will impact decision making " \
                                 "or post-operative care, proceed to pharmacologic nuclear stress " \
                                 "testing."
                return recommendation
        elif entries_radiobuttons["Functional capacity"] == " 4-10 METS " or \
                entries_radiobuttons["Functional capacity"] == " >10 METS ":
            recommendation = "Recommendation:  No further testing.  Proceed to surgery."
            return recommendation

    def __smith_modified_sgarbossa_criteria(self, entries):

        if entries['Concordant ST elevation'] == 1 or entries['Concordant ST depression in V1-V3'] ==  1 or entries['Proportionally excessive discordant ST elevation in >= one lead'] == 1:
            sgarbossa_criteria = "Smith modified Sgarbossa criteria are positive.  Acute MI is suspected."
        else:
            sgarbossa_criteria = "Smith modified Sgarbossa criteria are not met.  Acute MI is not suspected."
        print(sgarbossa_criteria)
        return sgarbossa_criteria

    def __TIMI_score_ACS(self, entries):
        TIMI_score = 0
        for key in entries:
            TIMI_score += entries[key]
        print(TIMI_score)
        return TIMI_score
