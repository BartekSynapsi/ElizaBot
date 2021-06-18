import os
import jsgf

class NLU:
    def __init__(self):
        self.grammars = [
            jsgf.parse_grammar_file(f"bot/JSGFs/{file_name}")
            for file_name in os.listdir("bot/JSGFs")
        ]

    def get_dialog_act(self, rule):
        slots = []
        self.get_slots(rule.expansion, slots)
        return {"act": rule.grammar.name, "slots": slots}

    def get_slots(self, expansion, slots):
        if expansion.tag != "":
            slots.append((expansion.tag, expansion.current_match))
            return

        for child in expansion.children:
            self.get_slots(child, slots)

        if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
            self.get_slots(expansion.referenced_rule.expansion, slots)

    def match(self, utterance):
        list_of_illegal_character = [",", ".", "'", "?", "!", ":", "-", "/"]
        for illegal_character in list_of_illegal_character[:-2]:
            utterance = utterance.replace(f"{illegal_character}", "")
        for illegal_character in list_of_illegal_character[-2:]:
            utterance = utterance.replace(f"{illegal_character}", " ")

        for grammar in self.grammars:
            matched = grammar.find_matching_rules(utterance)
            if matched:
                return self.get_dialog_act(matched[0])
        return {"act": "null", "slots": []}
