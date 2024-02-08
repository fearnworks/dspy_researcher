import dspy 
from loguru import logger 

class CheckCitationFaithfulness(dspy.Signature):
    """Verify that the text is based on the provided context."""

    context = dspy.InputField(desc="facts here are assumed to be true")
    text = dspy.InputField()
    faithfulness = dspy.OutputField(desc="True/False indicating if text is faithful to context")

class GenerateAnswer(dspy.Signature):
    """Answer questions with short factoid answers."""

    context = dspy.InputField(desc="contains cited relevant facts")
    question = dspy.InputField()
    answer = dspy.OutputField(desc="Descriptive answer to the question")
    
class CheckForCitations(dspy.Signature):
    """Verify the text has proper citations."""
    
    context = dspy.InputField(desc="facts here are assumed to be true")
    text = dspy.InputField()
    cited = dspy.OutputField(desc="True/False indicating if citations are present")
    
