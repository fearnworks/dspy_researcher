import dspy

def get_3_5_turbo_and_colbertv2_wiki17_abstracts():
    turbo = dspy.OpenAI(model='gpt-3.5-turbo')
    colbertv2_wiki17_abstracts = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

    dspy.settings.configure(lm=turbo, rm=colbertv2_wiki17_abstracts)
    return turbo