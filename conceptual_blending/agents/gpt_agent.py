from hyperon import *
from .llmagent import ChatGPTAgent


def prompt_agent(metta: MeTTa, *args):

    
    text = " ".join(str(atom) for atom in args) # Instead of overwriting text in each loop iteration, concatenate multiple inputs: because if multiple args , the last arg is the text.


    gpt_agent = ChatGPTAgent()

    prompt = f'''
    You are an expert in conceptual blending. Your task is to:
    1. **Extract two key concepts** from the given text.
        2. **Identify the blend type** (Simplex, Mirror, Single-Scope, or Double-Scope).
    3. **Generate a structured representation** of how the two concepts blend.

    ### **Input Text:**
    "{text}"

    ### **Your Task:**
    - Identify **Concept 1** and **Concept 2** from the text.
    - Determine the **blend type**:
        - **Simplex** → One concept provides a **frame**, the other fills a role.
        - **Mirror** → Both concepts share the **same structure**.
        - **Single-Scope** → One concept dominates structurally, but the other contributes meaning.
        - **Double-Scope** → Two structurally different concepts merge to form something **entirely new**.

    ### **Examples:**
    - `(SimplexBlend (blend electricity waterFlow) circuitHydraulics)`
    - `(MirrorBlend (blend thunder speech) stormWarning)`
    - `(SingleScopeBlend (blend DrugMakers Speech) AntibioticMetaphors)`
    - `(DoubleScopeBlend (blend TheaterManagers Dictators) AbsoluteTheater)`

    ### **Now, extract concepts and generate:**
    1. **Concept 1** and **Concept 2** from the text.
    2. **Blend type** (Simplex, Mirror, Single-Scope, or Double-Scope).
    3. **Blended concept representation.**

    Return only one line in the specified format.
    '''

    messages = [{"role": "user", "content": prompt}]
    answer = gpt_agent(messages, functions=[])
    print(answer.content)

    try:

        atoms = metta.parse_all(answer.content)
        return [ValueAtom(atoms, 'Expression')]

    except Exception as e:
        print("Error Parsing Gpt Response",e)
        return [ValueAtom("(blendedConcept error invalid_output)", 'Expression')]

