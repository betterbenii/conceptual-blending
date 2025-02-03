from hyperon import *
from .llmagent import ChatGPTAgent


def prompt_agent(metta: MeTTa, *args):

    for atom in args:
        text = str(atom)

    gpt_agent = ChatGPTAgent()

    prompt = f'''
    You are an expert in conceptual blending. Your task is to:
    1. **Extract two key concepts** from the given text.
    2. **Generate a structured representation** of how the two concepts blend.

    ### **Input Text:**
    "{text}"

    ### **Your Task:**
    - Identify **Concept 1** and **Concept 2** from the text.
    - Use the **Simplex Network** approach, where:
    - One concept provides a **frame** (structured organization).
    - The other fills roles within this frame.
    - Represent the blended concept in **logical form** as:

    ### **Examples:**
    - `(blendedConcept (blend electricity waterFlow) circuitHydraulics)`
    - `(blendedConcept (blend painting music) visualSymphony)`
    - `(blendedConcept (blend language math) symbolicReasoning)`
    - `(blendedConcept (blend genetics computing) bioinformatics)`

    ### **Now, extract concepts and generate:**
    1. **Concept 1** and **Concept 2** from the text.
    2. **Blended concept representation.**

    Return only one line in the specified format.
    '''

    messages = [{"role": "user", "content": prompt}]
    answer = gpt_agent(messages, functions=[])
    print(answer.content)

    atoms = metta.parse_all(answer.content)
    return [ValueAtom(atoms, 'Expression')]

