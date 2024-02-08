from dspy import Example
from dspy.evaluate import Evaluate
from dspy_researcher.evaluation.f1 import calculate_f1_score
import os 
from loguru import logger 
num_threads = os.environ.get("DSP_NUM_THREADS", 1)

def dspy_f1_metric(gold: Example, pred ) -> float:
    logger.info(f"gold: {gold.answer}, pred: {pred.answer}")
    return calculate_f1_score(gold.answer, pred.answer)


def create_evaluators(examples):
    # create a suite of DSPy evaluators based on a set of examples
    evaluate_f1_score = Evaluate(
        devset=examples,
        metric=dspy_f1_metric,
        num_threads=num_threads,
        display_progress=False,
        display_table=15
    )


    return {
        "f1": evaluate_f1_score,

    }


supported_metrics = {
    "f1": dspy_f1_metric,
}
