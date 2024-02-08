import dspy
import random 
import dspy_researcher.loaders.data_splitter as DSplitter

def get_split_qa_labels(split_ratio: tuple = (0.7, 0.2, 0.1)) -> DSplitter.DataSplits:
    """
    Splits the qa_labeler_examples into training, evaluation, and development sets using the DataSplits class.
    
    Args:
        split_ratio (tuple): A tuple representing the ratio of train, evaluate, and dev sets respectively.
        
    Returns:
        DataSplits: An instance of the DataSplits class containing the train, evaluate, and dev datasets.
    """
    return DSplitter.split_dataset(qa_labeler_examples, split_ratio)

qa_labeler_examples = [
    dspy.Example(
        question="What is the process of photosynthesis?",
        answer="plants, sunlight, water, carbon dioxide, glucose, oxygen"
    ),
    dspy.Example(
        question="Who was the first president of the United States?",
        answer="George Washington, first president, United States"
    ),
    dspy.Example(
        question="How does a refrigerator work?",
        answer="cooling, refrigerant, compression, evaporation, heat exchange"
    ),
    dspy.Example(
        question="What are the main components of a computer?",
        answer="CPU, motherboard, RAM, storage, power supply"
    ),
    dspy.Example(
        question="What causes earthquakes?",
        answer="tectonic plates, faults, seismic waves, Earth's crust"
    ),
    dspy.Example(
        question="What is the significance of the Turing Test?",
        answer="artificial intelligence, human-like responses, Alan Turing"
    ),
    dspy.Example(
        question="How does blockchain technology work?",
        answer="distributed ledger, encryption, transactions, blocks, security"
    ),
    dspy.Example(
        question="What is the theory of relativity?",
        answer="Einstein, spacetime, speed of light, gravity, physics"
    ),
        dspy.Example(
        question="What is the role of DNA in genetics?",
        answer="hereditary material, genes, chromosomes, protein coding"
    ),
    dspy.Example(
        question="How does the immune system protect the body from disease?",
        answer="white blood cells, antibodies, pathogens, immune response"
    ),
    dspy.Example(
        question="What are the basic principles of democracy?",
        answer="freedom, equality, justice, majority rule, minority rights"
    ),
    dspy.Example(
        question="What is the function of the heart in the human body?",
        answer="pumping blood, oxygen transport, nutrients, waste removal"
    ),
    dspy.Example(
        question="How do solar panels generate electricity?",
        answer="solar cells, sunlight conversion, photovoltaic effect, electricity"
    ),
    dspy.Example(
        question="What was the impact of the Industrial Revolution?",
        answer="manufacturing, technology, urbanization, economic growth"
    ),
    dspy.Example(
        question="What is the importance of the water cycle?",
        answer="evaporation, condensation, precipitation, ecosystem support"
    ),
    dspy.Example(
        question="How do vaccines work?",
        answer="immune system, antibodies, disease prevention, immunization"
    ),
    dspy.Example(
        question="What causes climate change?",
        answer="greenhouse gases, fossil fuels, carbon dioxide, global warming"
    ),
    dspy.Example(
        question="What is quantum computing?",
        answer="quantum bits, superposition, entanglement, computational power"
    ),
    dspy.Example(
        question="How does artificial intelligence learn?",
        answer="machine learning, algorithms, data analysis, pattern recognition"
    ),
    dspy.Example(
        question="What is the significance of the Great Wall of China?",
        answer="defense, ancient architecture, Ming Dynasty, cultural symbol"
    ),
    dspy.Example(
        question="How does the stock market work?",
        answer="buying, selling shares, investment, company equity, market dynamics"
    ),
    dspy.Example(
        question="What are renewable energy sources?",
        answer="solar, wind, hydro, biomass, sustainability, environmental impact"
    ),
    dspy.Example(
        question="How do antibiotics combat bacterial infections?",
        answer="kill bacteria, inhibit growth, bacterial resistance, medication"
    ),
    dspy.Example(
        question="What is the process of evolution?",
        answer="natural selection, genetic variation, species adaptation, survival"
    ),
    dspy.Example(
        question="What are the functions of the United Nations?",
        answer="peacekeeping, human rights, development, international law"
    ),
    dspy.Example(
        question="How does a combustion engine work?",
        answer="fuel ignition, pistons, mechanical energy, vehicle propulsion"
    ),
    dspy.Example(
        question="What is the impact of global warming on polar ice caps?",
        answer="melting glaciers, sea level rise, habitat loss, climate effects"
    ),
    dspy.Example(
        question="What are the causes and effects of deforestation?",
        answer="tree cutting, habitat destruction, biodiversity loss, climate change"
    )
]
