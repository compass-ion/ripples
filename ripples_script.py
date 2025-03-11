# =================================================
#  >>>Ripples: Brainstorming with a Purpose<<<
#               (script version)
# =================================================

import printing_templates
import test_data

# Initializing constants:
#NUM_RIPPLES = 5
#NUM_SUBTOPICS = NUM_RIPPLES

# initializing dictionaries collecting nodes
dic_center = {'center': 'topic'}

dic_ripple1 = {
    'r1n1': 'caption of r1n1',
    'r1n2': 'caption of r1n2',
    'r1n3': 'caption of r1n3',
    'r1n4': 'caption of r1n4',
    'r1n5': 'caption of r1n5'
    }

dic_ripple2 = {
    'r2n1': 'caption of r2n1',
    'r2n2': 'caption of r2n2',
    'r2n3': 'caption of r2n3',
    'r2n4': 'caption of r2n4',
    'r2n5': 'caption of r2n5'
    }

dic_ripple3 = {
    'r3n1': 'caption of r3n1',
    'r3n2': 'caption of r3n2',
    'r3n3': 'caption of r3n3',
    'r3n4': 'caption of r3n4',
    'r3n5': 'caption of r3n5',
    }

dic_ripple4 = {
    'r4n1': 'caption of r4n1',
    'r4n2': 'caption of r4n2',
    'r4n3': 'caption of r4n3',
    'r4n4': 'caption of r4n4',
    'r4n5': 'caption of r4n5',
    }

dic_ripple5 = {
    'r5n1': 'caption of r4n1',
    'r5n2': 'caption of r4n2',
    'r5n3': 'caption of r4n3',
    'r5n4': 'caption of r4n4',
    'r5n5': 'caption of r4n5'
    }

ancestor_nodes = {
    'center': None,
    'r1n1': 'center',
    'r1n2': 'center',
    'r1n3': 'center',
    'r1n4': 'center',
    'r1n5': 'center',
    'r2n1': ['r1n5', 'r1n1'],
    'r2n2': ['r1n1', 'r1n2'],
    'r2n3': ['r1n2', 'r1n3'],
    'r2n4': ['r1n3', 'r1n4'],
    'r2n5': ['r1n4', 'r1n5'],
    'r3n1': ['r2n5', 'r2n1'],
    'r3n2': ['r2n1', 'r2n2'],
    'r3n3': ['r2n2', 'r2n3'],
    'r3n4': ['r2n3', 'r2n4'],
    'r3n5': ['r2n4', 'r2n5'],
    'r4n1': ['r3n5', 'r3n1'],
    'r4n2': ['r3n1', 'r3n2'],
    'r4n3': ['r3n2', 'r3n3'],
    'r4n4': ['r3n3', 'r3n4'],
    'r4n5': ['r3n4', 'r3n5'],
    'r5n1': ['r4n5', 'r4n1'],
    'r5n2': ['r4n1', 'r4n2'],
    'r5n3': ['r4n2', 'r4n3'],
    'r5n4': ['r4n3', 'r4n4'],
    'r5n5': ['r4n4', 'r4n5']
    }

dic_prompts = {
    'center': "Select a topic you want to dive into: ",
    'ripple1': "Freely associate to your topic: '{}'. ",
    'ripple2': "Find a connection between '{}' and '{}'. ",
    'ripple3': "Find a connection between '{}' and '{}'. ",
    'ripple4': "Find a connection between '{}' and '{}'. ",
    'ripple5': "Find a connection between '{}' and '{}'. "
    }

ripples = {'center': dic_center,
           'ripple1': dic_ripple1,
           'ripple2': dic_ripple2,
           'ripple3': dic_ripple3,
           'ripple4': dic_ripple4,
           'ripple5': dic_ripple5
           }

previous_ripple = None

def get_captions(dic_ripple: dict, ripple: str, previous_ripple: str) -> None:
    prompt = dic_prompts[ripple]
    if ripple == 'center':
        for key in dic_ripple:
            print(prompt, end='')
            dic_ripple[key] = input()
            #dic_ripple[key] = input(prompt,)
    elif ripple == 'ripple1':
        prompt = prompt.format(dic_center['center'])
        for key in dic_ripple:
            #dic_ripple[key] = input(prompt,)
            print(prompt, end='')
            dic_ripple[key] = input()
    else:
        for key in dic_ripple:
            ancestors = ancestor_nodes[key]
            anc1 = ripples[previous_ripple][ancestors[0]]
            anc2 = ripples[previous_ripple][ancestors[1]]
            prompt = prompt.format(anc1, anc2)
            #dic_ripple[key] = input(prompt,)
            print(prompt, end='')
            dic_ripple[key] = input()
            prompt = dic_prompts[ripple]

def create_node_to_caption() -> dict:
    node_to_caption = {
        'center': ripples['center']['center'],
        'r1n1': ripples['ripple1']['r1n1'],
        'r1n2': ripples['ripple1']['r1n2'],
        'r1n3': ripples['ripple1']['r1n3'],
        'r1n4': ripples['ripple1']['r1n4'],
        'r1n5': ripples['ripple1']['r1n5'],
        'r2n1': ripples['ripple2']['r2n1'],
        'r2n2': ripples['ripple2']['r2n2'],
        'r2n3': ripples['ripple2']['r2n3'],
        'r2n4': ripples['ripple2']['r2n4'],
        'r2n5': ripples['ripple2']['r2n5'],
        'r3n1': ripples['ripple3']['r3n1'],
        'r3n2': ripples['ripple3']['r3n2'],
        'r3n3': ripples['ripple3']['r3n3'],
        'r3n4': ripples['ripple3']['r3n4'],
        'r3n5': ripples['ripple3']['r3n5'],
        'r4n1': ripples['ripple4']['r4n1'],
        'r4n2': ripples['ripple4']['r4n2'],
        'r4n3': ripples['ripple4']['r4n3'],
        'r4n4': ripples['ripple4']['r4n4'],
        'r4n5': ripples['ripple4']['r4n5'],
        'r5n1': ripples['ripple5']['r5n1'],
        'r5n2': ripples['ripple5']['r5n2'],
        'r5n3': ripples['ripple5']['r5n3'],
        'r5n4': ripples['ripple5']['r5n4'],
        'r5n5': ripples['ripple5']['r5n5']
        }
    return node_to_caption


def print_temp5() -> None:
    substitutions_center_minus = {
        'bbbbbbbbbbbbb': 'r1n1',
        'jjjjjjjjjjjjj': 'r2n4',
        'mmmmmmmmmmmmm': 'r3n2',
        'uuuuuuuuuuuuu': 'r4n5',
        'xxxxxxxxxxxxx': 'r5n3'
    }
        
    substitutions_center_whitespace = {
        'aaaaaaaaaaaaa': 'center',
        'ccccccccccccc': 'r1n2',
        'fffffffffffff': 'r1n5',
        'iiiiiiiiiiiii': 'r2n3',
        'kkkkkkkkkkkkk': 'r2n5',
        'lllllllllllll': 'r3n1',
        'nnnnnnnnnnnnn': 'r3n3',
        'qqqqqqqqqqqqq': 'r4n1',
        'ttttttttttttt': 'r4n4',
        'wwwwwwwwwwwww': 'r5n2',
        'yyyyyyyyyyyyy': 'r5n4'
    }
    
    substitutions_left_minus = {
        'eeeeeeeeeeeee': 'r1n4',
        'ggggggggggggg': 'r2n1',
        'ppppppppppppp': 'r3n5',
        'rrrrrrrrrrrrr': 'r4n2',
        'vvvvvvvvvvvvv': 'r5n1'
        }
    
    substitutions_right_minus = {
        'ddddddddddddd': 'r1n3',
        'hhhhhhhhhhhhh': 'r2n2',
        'ooooooooooooo': 'r3n4',
        'sssssssssssss': 'r4n3',
        'zzzzzzzzzzzzz': 'r5n5'
        }

    node_to_caption = create_node_to_caption()

    for key in substitutions_center_minus:
        substitutions_center_minus[key] = node_to_caption[substitutions_center_minus[key]]
    for key in substitutions_center_whitespace:
        substitutions_center_whitespace[key] = node_to_caption[substitutions_center_whitespace[key]]
    for key in substitutions_left_minus:
        substitutions_left_minus[key] = node_to_caption[substitutions_left_minus[key]]
    for key in substitutions_right_minus:
        substitutions_right_minus[key] = node_to_caption[substitutions_right_minus[key]]

    template = printing_templates.printing_template[5]
    for key in substitutions_center_whitespace:
        template = template.replace(key, substitutions_center_whitespace[key][:13].center(13))
    for key in substitutions_center_minus:
        template = template.replace(key, substitutions_center_minus[key][:13].center(13, '-'))
        
    for key in substitutions_left_minus:
        template = template.replace(key, substitutions_left_minus[key][:13].ljust(13, '-'))
        
    for key in substitutions_right_minus:
        template = template.replace(key, substitutions_right_minus[key][:13].rjust(13, '-'))
    print(template)



if __name__ == '__main__':
    for key in ripples:
        get_captions(ripples[key], key, previous_ripple)
        previous_ripple = key
    print_temp5()

    # printing example output
    # =========================
    # import test_data
    # ripples = test_data.test_ripple
    # print_temp5()


# direkt printen
# inline prompt
