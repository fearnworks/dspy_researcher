from pydantic import BaseModel
import random
from typing import List, Tuple, TypeVar

# Define a generic type variable for examples
T = TypeVar('T')

class DataSplits(BaseModel):
    train: List[T]
    evaluate: List[T]
    dev: List[T]

def split_dataset(examples: List[T], split_ratio: Tuple[float, float, float] = (0.7, 0.2, 0.1)) -> DataSplits:
    """
    Splits a list of examples into training, evaluation, and development sets based on the provided ratio.
    
    Args:
        examples (List[T]): The list of examples to split.
        split_ratio (Tuple[float, float, float], optional): A tuple representing the ratio of train, evaluate, and dev sets respectively. Defaults to (0.7, 0.2, 0.1).
        
    Returns:
        DataSplits: A Pydantic model containing the train, evaluate, and dev datasets.
    """
    # Ensure the split ratio sums to 1
    if not 0.999 <= sum(split_ratio) <= 1.001:
        raise ValueError("Split ratios must sum to approximately 1.")
    
    
    # Shuffle the examples to ensure random distribution
    random.shuffle(examples)
    
    # Calculate split indices
    total_examples = len(examples)
    train_end = int(total_examples * split_ratio[0])
    eval_end = train_end + int(total_examples * split_ratio[1])
    
    # Split the dataset
    train_set = examples[:train_end]
    eval_set = examples[train_end:eval_end]
    dev_set = examples[eval_end:]
    
    return DataSplits(train=train_set, evaluate=eval_set, dev=dev_set)
