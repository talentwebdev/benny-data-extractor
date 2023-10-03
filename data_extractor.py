from abc import abstractmethod, ABC
import spacy


# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


class BaseInterpreter(ABC):

    def __init__(self, doc, ent):
        self.doc = doc
        self.ent = ent

    @abstractmethod
    def interpret(self):
        raise NotImplementedError


class StateEndDateInterpreter(BaseInterpreter):

    def interpret(self) -> dict:
        start_verbs = {"start", "commence", "begin"}
        end_verbs = {"end", "stop", 'precede'}
        dates_with_start_verbs = []
        dates_with_end_verbs = []

        if self.ent.label_ == "DATE":
            idx = 0
            while self.ent.start - idx >= 0:
                token = self.ent.start - idx
                if self.doc[token].pos_ == 'VERB':
                    if token >= 0 and self.doc[token].lemma_ in start_verbs:
                        dates_with_start_verbs.append(self.ent.text)

                    if token >= 0 and self.doc[token].lemma_ in end_verbs:
                        dates_with_end_verbs.append(self.ent.text)
                    break

                idx += 1

        return {
            'start_dates': dates_with_start_verbs,
            'end_dates': dates_with_end_verbs
        }


class MinMaxInterpreter(BaseInterpreter):

    def interpret(self):
        max_contributions = []
        min_contributions = []

        if self.ent.label_ in ["MONEY", "PERCENT"]:
            prev_tokens = {}
            for idx in range(0, 4):
                token = self.ent.start - idx
                prev_tokens[self.doc[token].pos_] = self.doc[token]

            is_max = None

            if prev_tokens.get('ADJ') and prev_tokens['ADJ'].lemma_ in ['less', 'more']:
                is_max = prev_tokens['ADJ'].lemma_ == 'less'

            if prev_tokens.get('VERB') and prev_tokens['VERB'].lemma_ == 'exceed':
                is_max = False

            if is_max is not None and prev_tokens.get('PART') and prev_tokens['PART'].lemma_ == 'not':
                is_max = not is_max

            if is_max is True:
                max_contributions.append(self.ent.text)
            elif is_max is False:
                min_contributions.append(self.ent.text)

        return {
            'min_contribution': min_contributions,
            'max_contribution': max_contributions
        }


class DataExtractor:

    interpreter_clss = [StateEndDateInterpreter, MinMaxInterpreter, ]

    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(self.text)

    @classmethod
    def create(cls, text: str):
        return cls(text)

    def extract(self):
        result = {}
        for ent in self.doc.ents:
            for interpreter_cls in self.interpreter_clss:
                interpreter: BaseInterpreter
                interpreter = interpreter_cls(self.doc, ent)
                interpret_result = interpreter.interpret()

                # combine the interpreted results
                for key, value in interpret_result.items():
                    result[key] = result.get(key, []) + value

        return result
