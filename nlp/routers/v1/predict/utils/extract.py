from spacy.util import compile_prefix_regex, compile_infix_regex, compile_suffix_regex
from spacy.tokenizer import Tokenizer
from spacy.pipeline import EntityRuler
import spacy
import re

nlp = spacy.load('en_core_web_lg')
url_regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
nlp.tokenizer = Tokenizer(nlp.vocab,
    prefix_search=compile_prefix_regex(nlp.Defaults.prefixes).search,
    suffix_search=compile_suffix_regex(nlp.Defaults.suffixes).search,
    url_match=url_regex.match,
    infix_finditer= re.compile(r'''[~]''').finditer
)

ruler = nlp.add_pipe("entity_ruler", config={"validate": True})
patterns = [
    {"label": "CVE", "pattern": [{"SHAPE": "XXX-dddd-dddd"}]},
    {"label": "CVE", "pattern": [{"SHAPE": "xxx-dddd-dddd"}]},
    {"label": "CVE", "pattern": [{"SHAPE": "XXX-dddd-ddddd"}]},
    {"label": "CVE", "pattern": [{"SHAPE": "xxx-dddd-ddddd"}]},
    {"label": "ADVISORY", "pattern": [{"SHAPE": "XXXdddddd"}]},
    {"label": "ADVISORY", "pattern": [{"SHAPE": "xxxdddddd"}]}
]
ruler.add_patterns(patterns)


class Extract:
    def __init__(self, doc=None):
        self.doc = doc

    def props(self, min_length=2):
        stop_words = nlp.Defaults.stop_words
        tokens = [set(token.lemma_ for token in self.doc
            if (token.tag_ == 'NNP' and token.pos_ == 'PROPN') and \
                len(token.lemma_) > min_length and \
                not token.lemma_ in stop_words)]
        return tokens

    def entities(self):
        all_ents = {
            'PERSON': set(),
            'ORG': set(),
            'PRODUCT': set(),
            'CVE': set(),

        }
        for ent in self.doc.ents:
            if ent.label_ in all_ents:
                all_ents[ent.label_].add(ent)
        return all_ents
       