import dspy
from typing import Tuple, List

def load_custom_short_answers() -> Tuple[List[dspy.Example], List[dspy.Example]]:    
    """
    Load custom short answers for training and development.

    This function loads a set of predefined question-answer pairs for training and development.
    Each pair is converted into a dspy.Example object with 'question' as the input.

    Returns:
        Tuple[List[dspy.Example], List[dspy.Example]]: A tuple containing two lists of dspy.Example objects.
        The first list is for training and the second list is for development.
    """
    train = [('Who was the director of the 2009 movie featuring Peter Outerbridge as William Easton?', 'Kevin Greutert'),
            ('The heir to the Du Pont family fortune sponsored what wrestling team?', 'Foxcatcher'),
            ('In what year was the star of To Hell and Back born?', '1925'),
            ('Which award did the first book of Gary Zukav receive?', 'U.S. National Book Award'),
            ('What documentary about the Gilgo Beach Killer debuted on A&E?', 'The Killing Season'),
            ('Which author is English: John Braine or Studs Terkel?', 'John Braine'),
            ('Who produced the album that included a re-recording of "Lithium"?', 'Butch Vig')]

    train = [dspy.Example(question=question, answer=answer).with_inputs('question') for question, answer in train]

    dev = [('Who has a broader scope of profession: E. L. Doctorow or Julia Peterkin?', 'E. L. Doctorow'),
        ('Right Back At It Again contains lyrics co-written by the singer born in what city?', 'Gainesville, Florida'),
        ('What year was the party of the winner of the 1971 San Francisco mayoral election founded?', '1828'),
        ('Anthony Dirrell is the brother of which super middleweight title holder?', 'Andre Dirrell'),
        ('The sports nutrition business established by Oliver Cookson is based in which county in the UK?', 'Cheshire'),
        ('Find the birth date of the actor who played roles in First Wives Club and Searching for the Elephant.', 'February 13, 1980'),
        ('Kyle Moran was born in the town on what river?', 'Castletown River'),
        ("The actress who played the niece in the Priest film was born in what city, country?", 'Surrey, England'),
        ('Name the movie in which the daughter of Noel Harrison plays Violet Trefusis.', 'Portrait of a Marriage'),
        ('What year was the father of the Princes in the Tower born?', '1442'),
        ('What river is near the Crichton Collegiate Church?', 'the River Tyne'),
        ('Who purchased the team Michael Schumacher raced for in the 1995 Monaco Grand Prix in 2000?', 'Renault'),
        ('André Zucca was a French photographer who worked with a German propaganda magazine published by what Nazi organization?', 'the Wehrmacht')]

    dev = [dspy.Example(question=question, answer=answer).with_inputs('question') for question, answer in dev]
    return train, dev