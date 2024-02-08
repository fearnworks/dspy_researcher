from collections import Counter
from dspy_researcher.evaluation.utils import normalize
from loguru import logger 
def calculate_f1_score(true_answer, predicted_answer, *args, **kwargs):
    """
    Calculate the F1 score between the true answer and the predicted answer.
    Both inputs are assumed to be strings.
    """
    logger.info(f"args: {args}, kwargs: {kwargs}")
    logger.info(f"true_answer: {true_answer}, predicted_answer: {predicted_answer}")
    true_tokens = normalize(true_answer.answer).split()
    pred_tokens = normalize(predicted_answer.answer).split()
    
    common_tokens = Counter(true_tokens) & Counter(pred_tokens)
    num_same = sum(common_tokens.values())
    
    if num_same == 0:
        return 0.0
    
    precision = 1.0 * num_same / len(pred_tokens)
    recall = 1.0 * num_same / len(true_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    
    return f1
