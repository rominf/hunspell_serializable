# noinspection PyUnresolvedReferences
from hunspell import HunSpellError
import hunspell


class HunSpell(hunspell.HunSpell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dic_filename, self._aff_filename = args

    def __setstate__(self, state):
        new_self = HunSpell(state['_dic_filename'], state['_aff_filename'])
        # noinspection PyUnusedLocal,PyMethodFirstArgAssignment
        self = new_self
