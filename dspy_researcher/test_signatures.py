import dspy
import pytest
from dspy_researcher.signatures import CheckCitationFaithfulness, CheckForCitations
from loguru import logger 

@pytest.fixture(scope="module", autouse=True)
def setup():
    turbo = dspy.OpenAI(model='gpt-3.5-turbo')
    colbertv2_wiki17_abstracts = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

    dspy.settings.configure(lm=turbo, rm=colbertv2_wiki17_abstracts)
    
@pytest.fixture
def faithfulness_signature():
    # Setup the ChainOfThought for CheckCitationFaithfulness
    return dspy.ChainOfThought(CheckCitationFaithfulness)

@pytest.fixture
def citation_check_signature():
    # Setup the ChainOfThought for CheckForCitations
    return dspy.ChainOfThought(CheckForCitations)

def test_faithful_text(faithfulness_signature):
    context = """
    [1](https://www.gardeningenthusiasts.com/emma-success-story) | Emma, a 27-year-old gardening enthusiast, has won multiple awards for her vegetable garden.
    Last season, her tomatoes were awarded 'Best in Show' at the local gardening fair. Emma has had two successful harvests with her innovative vertical gardening techniques, 
    producing over 100 pounds of vegetables. Her contributions to the community garden have helped improve yield and sustainability. The details of Emma's upcoming gardening 
    workshop have not been announced yet. Stay updated with all the latest gardening news on our dedicated page.
    """
    text1 = "Emma's innovative gardening techniques resulted in over 100 pounds of vegetables. [1](https://www.gardeningenthusiasts.com/emma-success-story)"

    # Invoke the CheckCitationFaithfulness signature
    result = faithfulness_signature(context=context, text=text1)
    assert result.faithfulness == 'True', "The text should be recognized as faithful."

def test_unfaithful_text(faithfulness_signature):
    context = """
    [1](https://www.gardeningenthusiasts.com/emma-success-story) | Emma, a 27-year-old gardening enthusiast, has presents her minimalist vegetable garden.
    Last season, her small kitchen garden was awarded 'Best Aesthetic' for its beautiful arrangement of flowers
    """
    text2 = "Emma once grew a tomato so large, it was mistaken for a UFO by local authorities. She was then crowned the queen of england. [1](https://www.gardeningenthusiasts.com/emma-success-story)"

    # Invoke the CheckCitationFaithfulness signature
    result = faithfulness_signature(context=context, text=text2)
    logger.info(result)
    assert result.faithfulness == 'False', "The text should not be recognized as faithful."
    
    
def test_text_with_citation(citation_check_signature):
    context = """
    [1](https://www.gardeningenthusiasts.com/emma-success-story) | Emma, a 27-year-old gardening enthusiast, has won multiple awards for her vegetable garden.
    Last season, her tomatoes were awarded 'Best in Show' at the local gardening fair. Emma has had two successful harvests with her innovative vertical gardening techniques, 
    producing over 100 pounds of vegetables. Her contributions to the community garden have helped improve yield and sustainability. The details of Emma's upcoming gardening 
    workshop have not been announced yet. Stay updated with all the latest gardening news on our dedicated page.
    """
    text1 = "Emma's innovative gardening techniques resulted in over 100 pounds of vegetables. [1](https://www.gardeningenthusiasts.com/emma-success-story)"

    # Invoke the CheckForCitations signature
    result = citation_check_signature(context=context, text=text1)
    assert result.cited == 'True', "The text should be recognized as having proper citations."

def test_text_without_citation(citation_check_signature):
    context = """
    [1](https://www.gardeningenthusiasts.com/emma-success-story) | Emma, a 27-year-old gardening enthusiast, has won multiple awards for her vegetable garden.
    Last season, her tomatoes were awarded 'Best in Show' at the local gardening fair. Emma has had two successful harvests with her innovative vertical gardening techniques, 
    producing over 100 pounds of vegetables. Her contributions to the community garden have helped improve yield and sustainability. The details of Emma's upcoming gardening 
    workshop have not been announced yet. Stay updated with all the latest gardening news on our dedicated page.
    """
    text2 = "Emma once grew a tomato so large, it was mistaken for a UFO by local authorities."

    # Invoke the CheckForCitations signature
    result = citation_check_signature(context=context, text=text2)
    assert result.cited == 'False', "The text should not be recognized as having proper citations."