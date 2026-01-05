dataset_dictionary = [
    {
        "feature_name": "Marital Status",
        "description": "Student’s marital status",
        "type": "categorical",
        "allowed_values": {
            "1": "Single", "2": "Married", "3": "Widower",
            "4": "Divorced", "5": "Facto union", "6": "Legally separated"
        }
    },
    {
        "feature_name": "Application mode",
        "description": "Mode of application",
        "type": "categorical",
        "allowed_values": {
            "1": "1st phase – general contingent", "2": "Ordinance No. 612/93",
            "5": "1st phase – special contingent (Azores Island)", "7": "Holders of other higher courses",
            "10": "Ordinance No. 854-B/99", "15": "International student (bachelor)",
            "16": "1st phase – special contingent (Madeira Island)", "17": "2nd phase – general contingent",
            "18": "3rd phase – general contingent", "26": "Ordinance No. 533-A/99, (item b2) (Different Plan)",
            "27": "Ordinance No. 533-A/99, item b3 (Other Institution)", "39": "Over 23 years old",
            "42": "Transfer", "43": "Change of course", "44": "Technological specialization diploma holders",
            "51": "Change of institution/course", "53": "Short cycle diploma holders",
            "57": "Change of institution/course (International)"
        }
    },
    {
        "feature_name": "Application order",
        "description": "Order of preference",
        "type": "numerical",
        "allowed_values": {"min": 1, "max": 9}
    },
    {
        "feature_name": "Course",
        "description": "Degree program",
        "type": "categorical",
        "allowed_values": {
            "33": "Biofuel Production Technologies", "171": "Animation and Multimedia Design",
            "8014": "Social Service (evening attendance)", "9003": "Agronomy",
            "9070": "Communication Design", "9085": "Veterinary Nursing",
            "9119": "Informatics Engineering", "9130": "Equinculture", "9147": "Management",
            "9238": "Social Service", "9254": "Tourism", "9500": "Nursing",
            "9556": "Oral Hygiene", "9670": "Advertising and Marketing Management",
            "9773": "Journalism and Communication", "9853": "Basic Education",
            "9991": "Management (evening attendance)"
        }
    },
    {
        "feature_name": "Daytime/evening attendance",
        "description": "Attendance type",
        "type": "categorical",
        "allowed_values": {"1": "Daytime", "0": "Evening"}
    },
    {
        "feature_name": "Previous qualification",
        "description": "Highest qualification before enrollment",
        "type": "categorical",
        "allowed_values": {
            "1": "Secondary education", "2": "Higher education – bachelor's degree",
            "3": "Higher education – degree", "4": "Higher education – master's",
            "5": "Higher education – doctorate", "6": "Frequency of higher education",
            "9": "12th year of schooling – not completed", "10": "11th year of schooling – not completed",
            "12": "Other – 11th year of schooling", "14": "10th year of schooling",
            "15": "10th year of schooling – not completed", "19": "Basic education 3rd cycle or equivalent",
            "38": "Basic education 2nd cycle or equivalent", "39": "Technological specialization course",
            "40": "Higher education – degree (1st cycle)", "42": "Professional higher technical course",
            "43": "Higher education – master (2nd cycle)"
        }
    },
    {
        "feature_name": "Previous qualification (grade)",
        "description": "Grade obtained in previous qualification",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 200}
    },
    {
        "feature_name": "Nacionality",
        "description": "Student’s nationality",
        "type": "categorical",
        "allowed_values": {
            "1": "Portuguese", "2": "German", "6": "Spanish", "11": "Italian", "13": "Dutch",
            "14": "English", "17": "Lithuanian", "21": "Angolan", "22": "Cape Verdean",
            "24": "Guinean", "25": "Mozambican", "26": "Santomean", "32": "Turkish",
            "41": "Brazilian", "62": "Romanian", "100": "Moldova", "101": "Mexican",
            "103": "Ukrainian", "105": "Russian", "108": "Cuban", "109": "Colombian"
        }
    },
    {
        "feature_name": "Mother's qualification",
        "description": "Mother’s highest qualification",
        "type": "categorical",
        "allowed_values": {
            "1": "Secondary education", "2": "Higher education – bachelor's degree",
            "3": "Higher education – degree", "4": "Higher education – master's",
            "5": "Higher education – doctorate", "6": "Frequency of higher education",
            "9": "12th year of schooling – not completed", "10": "11th year of schooling – not completed",
            "12": "Other – 11th year of schooling", "14": "10th year of schooling",
            "15": "10th year of schooling – not completed", "19": "Basic education 3rd cycle or equivalent",
            "38": "Basic education 2nd cycle or equivalent", "39": "Technological specialization course",
            "40": "Higher education – degree (1st cycle)", "42": "Professional higher technical course",
            "43": "Higher education – master (2nd cycle)"
        }
    },
    {
        "feature_name": "Father's qualification",
        "description": "Father’s highest qualification",
        "type": "categorical",
        "allowed_values": {
            "1": "Secondary education", "2": "Higher education – bachelor's degree",
            "3": "Higher education – degree", "4": "Higher education – master's",
            "5": "Higher education – doctorate", "6": "Frequency of higher education",
            "9": "12th year of schooling – not completed", "10": "11th year of schooling – not completed",
            "12": "Other – 11th year of schooling", "14": "10th year of schooling",
            "15": "10th year of schooling – not completed", "19": "Basic education 3rd cycle or equivalent",
            "38": "Basic education 2nd cycle or equivalent", "39": "Technological specialization course",
            "40": "Higher education – degree (1st cycle)", "42": "Professional higher technical course",
            "43": "Higher education – master (2nd cycle)"
        }
    },
    {
        "feature_name": "Mother's occupation",
        "description": "Mother’s occupation",
        "type": "categorical",
        "allowed_values": {
            "0": "Student", "1": "Representatives/Directors", "2": "Intellectual/Scientific Specialists",
            "3": "Intermediate Technicians", "4": "Administrative staff", "5": "Personal Services/Security",
            "6": "Farmers/Skilled Agriculture", "7": "Skilled Industry/Construction",
            "8": "Installation/Machine Operators", "9": "Unskilled Workers", "10": "Armed Forces",
            "90": "Other Situation", "99": "blank", "122": "Health professionals", "123": "Teachers",
            "125": "ICT Specialists", "131": "Science/Engineering Technicians",
            "132": "Health Technicians", "134": "Legal/Social/Culture Technicians",
            "141": "Office/Data Operators", "143": "Financial/Registry Operators",
            "144": "Other admin support", "151": "Personal service", "152": "Sellers",
            "153": "Personal care", "171": "Skilled construction", "173": "Printing/Precision workers",
            "175": "Food/Wood/Clothing workers", "191": "Cleaning workers",
            "192": "Unskilled Agriculture/Forestry", "193": "Unskilled Extractive/Transport",
            "194": "Meal preparation assistants"
        }
    },
    {
        "feature_name": "Father's occupation",
        "description": "Father’s occupation",
        "type": "categorical",
        "allowed_values": {
            "0": "Student", "1": "Representatives/Directors", "2": "Intellectual/Scientific Specialists",
            "3": "Intermediate Technicians", "4": "Administrative staff", "5": "Personal Services/Security",
            "6": "Farmers/Skilled Agriculture", "7": "Skilled Industry/Construction",
            "8": "Installation/Machine Operators", "9": "Unskilled Workers", "10": "Armed Forces",
            "90": "Other Situation", "99": "blank", "122": "Health professionals", "123": "Teachers",
            "125": "ICT Specialists", "131": "Science/Engineering Technicians",
            "132": "Health Technicians", "134": "Legal/Social/Culture Technicians",
            "141": "Office/Data Operators", "143": "Financial/Registry Operators",
            "144": "Other admin support", "151": "Personal service", "152": "Sellers",
            "153": "Personal care", "171": "Skilled construction", "173": "Printing/Precision workers",
            "175": "Food/Wood/Clothing workers", "191": "Cleaning workers",
            "192": "Unskilled Agriculture/Forestry", "193": "Unskilled Extractive/Transport",
            "194": "Meal preparation assistants"
        }
    },
    {
        "feature_name": "Admission grade",
        "description": "Admission grade at enrollment",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 200}
    },
    {
        "feature_name": "Displaced",
        "description": "Refugee/displaced status",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Educational special needs",
        "description": "Special educational needs",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Debtor",
        "description": "Outstanding debts",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Tuition fees up to date",
        "description": "Tuition fees paid up to date",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Gender",
        "description": "Gender",
        "type": "binary",
        "allowed_values": {"1": "Male", "0": "Female"}
    },
    {
        "feature_name": "Scholarship holder",
        "description": "Scholarship status",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Age at enrollment",
        "description": "Age when enrolled",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 70}
    },
    {
        "feature_name": "International",
        "description": "International student",
        "type": "binary",
        "allowed_values": {"1": "Yes", "0": "No"}
    },
    {
        "feature_name": "Curricular units 1st sem (credited)",
        "description": "Credited units (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 1st sem (enrolled)",
        "description": "Enrolled units (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 1st sem (evaluations)",
        "description": "Evaluations (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 1st sem (approved)",
        "description": "Approved units (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 1st sem (grade)",
        "description": "Average grade (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 1st sem (without evaluations)",
        "description": "Units without evaluation (1st semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (credited)",
        "description": "Credited units (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (enrolled)",
        "description": "Enrolled units (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (evaluations)",
        "description": "Evaluations (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (approved)",
        "description": "Approved units (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (grade)",
        "description": "Average grade (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Curricular units 2nd sem (without evaluations)",
        "description": "Units without evaluation (2nd semester)",
        "type": "numerical",
        "allowed_values": {"min": 0, "max": 20}
    },
    {
        "feature_name": "Unemployment rate",
        "description": "National unemployment rate (%)",
        "type": "numerical",
        "allowed_values": {"min": 0.0, "max": 100.0}
    },
    {
        "feature_name": "Inflation rate",
        "description": "National inflation rate (%)",
        "type": "numerical",
        "allowed_values": {"min": -100.0, "max": 100.0}
    },
    {
        "feature_name": "GDP",
        "description": "National GDP",
        "type": "numerical",
        "allowed_values": {"min": 0.0, "max": 1e13}
    },
    {
        "feature_name": "target",
        "description": "Final student status",
        "type": "categorical",
        "allowed_values": {"0": "Dropout", "1": "Graduate", "2": "Enrolled"}
    }
]