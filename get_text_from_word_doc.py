#!/usr/bin/env python3

import docx

def get_text_from_word_doc( filename, double_space_between_paragraph=True):
    doc = docx.Document(filename)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    paragraph_separator = '\n'
    if double_space_between_paragraph:
        paragraph_separator = '\n\n'
    return paragraph_separator.join(text)


def run_tests():
    print(f"\n\n{60*'_'}\nTesting get_text_from_word_doc()\n")
    print(get_text_from_word_doc('food_replicator.docx'))

    print(f"\n\n{60*'_'}\nTesting get_text_from_word_doc()\n")
    print(get_text_from_word_doc('food_replicator.docx', False))


run_tests()
