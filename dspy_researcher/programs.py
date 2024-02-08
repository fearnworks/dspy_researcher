import dspy 
from loguru import logger

from dspy_researcher.signatures import GenerateAnswer, CheckForCitations, CheckCitationFaithfulness

class LongFormQnAWithAssertions(dspy.Module):
    def __init__(self, passages_per_hop=3):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=passages_per_hop)
        self.generate_query = dspy.ChainOfThought("context, question -> query")
        self.generate_cited_paragraph = dspy.ChainOfThought("context, question -> paragraph")  # better with field description
        self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
    def forward(self, question):
        context = []

        for hop in range(2):
            query = self.generate_query(context=context, question=question).query
            context += self.retrieve(query).passages
            logger.info(f" Context: {context}")

        pred = self.generate_cited_paragraph(context=context, question=question)
        check_citations = dspy.ChainOfThought(CheckForCitations)
        citation_result : bool  = bool(check_citations(context=context, text=pred.paragraph).cited)
        dspy.Suggest(citation_result, "Every 1-2 sentences should have citations: 'text... [x].'")

        # Initialize the CheckCitationFaithfulness signature
        check_faithfulness = dspy.ChainOfThought(CheckCitationFaithfulness)
        faithfulness_result = bool(check_faithfulness(context=context, text=pred.paragraph).faithfulness)
        dspy.Suggest(faithfulness_result, f"Your output should be based on the context: '{context}'")
        
        answer = self.generate_answer(context=pred.paragraph, question=question)
        return answer

