from hyperon import *
from hyperon.ext import register_atoms
from .agents import *

@register_atoms(pass_metta=True)
def conceptual_blending_atoms(metta):
    gptAtom = OperationAtom('gpt', lambda *args: prompt_agent(metta, *args), [AtomType.ATOM, "Expression"], unwrap=False)

    return {
        r"gpt": gptAtom,
    }
