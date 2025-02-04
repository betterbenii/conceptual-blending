from hyperon import *
from .llmagent import ChatGPTAgent


def prompt_agent(metta: MeTTa, *args):

    
    text = " ".join(str(atom) for atom in args) # Instead of overwriting text in each loop iteration, concatenate multiple inputs: because if multiple args , the last arg is the text.


    gpt_agent = ChatGPTAgent()

    prompt = f'''
    You are an expert in conceptual blending. Your task is to:
    1. **Extract two key concepts** from the given {text}.
    2. **Determine the blend type** (Simplex, Mirror, Single-Scope, or Double-Scope).
    3. **Generate a structured representation** of the blend.

    ### **Rules for Classifying Blend Types:**
    - **Simplex Blend** → One concept provides a **frame**, the other fills a role.
    - Example: **Electricity + Water Flow** → `(SimplexBlend (blend electricity waterFlow) circuitHydraulics)`
    - *HINT: If one concept clearly organizes the other, it's Simplex.*

    - **Mirror Blend** → Both concepts share the **same structure**.
    - Example: **River + Road** → `(MirrorBlend (blend river road) naturalFlowPathways)`
    - *HINT: If both concepts have the same logical organization, it's Mirror.*

    - **Single-Scope Blend** → One concept's structure dominates while the other provides meaning.
    - Example: **Drug Manufacturing + Speech** → `(SingleScopeBlend (blend DrugManufacturing Speech) PharmaceuticalMetaphors)`
    - *HINT: If only ONE structure is used, but meaning comes from both, it's Single-Scope.*

    - **Double-Scope Blend** → Two concepts with **different structures** merge into a new one.
    - Example: **Theater Management + Dictatorship** → `(DoubleScopeBlend (blend TheaterManagement Dictatorship) AuthoritarianStagecraft)`
    - *HINT: If BOTH concepts contribute unique structures, it's Double-Scope.*

    ### **Now, extract concepts and generate:**
    1. **Concept 1** and **Concept 2** from the {text}.
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

