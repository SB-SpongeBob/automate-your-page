def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

LIST_OF_CONCEPTS = [['Computer', 'A universal machine. We can program it to do essentially any computation.'],
                    ['Computer Program', 'Very precise sequence of steps.'],
                    ['Programming Language', 'A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.'], 
                    ['Python', 'An interpreter. It runs our programs, it interprets them, executes the programs that we wrote in Python language by running a program in a language that the computer can understand directly.'],
                    ['Grammar', 'Programming languages have grammars. Have to write code that is exactly correct according to the Python interpreter, otherwise will have errors.']]

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)
