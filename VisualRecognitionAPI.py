import json
from watson_developer_cloud import VisualRecognitionV3


version = '2018-09-03'
url='https://gateway.watsonplatform.net/visual-recognition/api'
api_key = 'Zs7YvERX-qWGY6WlDDXSwtVm1bB7faXrehisHy2jt948'
classifier_ids = 'CarsColorsCustomModel_808565986'
threshold = '0.9'

sel_class=''
real_score=''

def sendData(path):
    global sel_class, real_score
    visual_recognition = VisualRecognitionV3(
        version,
        url=url,
        iam_apikey=api_key)
    with open(path, 'rb') as image_file:
        classes = visual_recognition.classify(
            image_file,
            threshold=threshold,
            classifier_ids=classifier_ids)
        result = json.dumps(classes.result, indent=2)
        ind_class = result.find("class\":")
        if ind_class != -1:
            score = result.find("\"score\":")
            sel_class = result[ind_class + 9:score]
            ind_score = sel_class.find("\",")
            sel_class = sel_class[:ind_score]
            if score != -1:
                real_score = result[score + 9:score + 14]
