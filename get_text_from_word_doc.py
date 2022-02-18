#!/usr/bin/env python3

import docx

def get_text_from_word_doc( filename):
    doc = docx.Document(filename)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)


def run_tests():
    print("\n\nTesting get_text_from_word_doc()\n")
    print(get_text_from_word_doc('food_replicator.docx'))


run_tests()
