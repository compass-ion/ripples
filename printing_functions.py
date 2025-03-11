# ===== printing functions =====
import printing_templates

def print_temp2():
    substitutions_minus_padding = {
        'bbbbbbbbb': 'r1n1',
        'ccccccccc': 'r1n2'
    }

    substitutions_whitespace_padding = {
        'aaaaaaaaa': 'topic',
        'ddddddddd': 'r2n1',
        'eeeeeeeee': 'r2n2'
    }

    template = printing_template[2]
    for key in substitutions_whitespace_padding:
        template = template.replace(key, substitutions_whitespace_padding[key][:9].center(9))
    for key in substitutions_minus_padding:
        template = template.replace(key, substitutions_minus_padding[key][:9].center(9, '-'))
    print(template)

def print_temp3():
    substitutions_minus_padding = {
        'bbbbbbbbb': 'r1n1',
        'ggggggggg': 'r2n3',
        'iiiiiiiii': 'r3n2'
    }

    substitutions_whitespace_padding = {
        'aaaaaaaaa': 'topic',
        'ccccccccc': 'r1n2',
        'ddddddddd': 'r1n3',
        'eeeeeeeee': 'r2n1',
        'fffffffff': 'r2n2',
        'hhhhhhhhh': 'r3n1',
        'jjjjjjjjj': 'r3n3'
    }

    template = printing_template[3]
    for key in substitutions_whitespace_padding:
        template = template.replace(key, substitutions_whitespace_padding[key][:9].center(9))
    for key in substitutions_minus_padding:
        template = template.replace(key, substitutions_minus_padding[key][:9].center(9, '-'))
    print(template)

def print_temp4():
    substitutions_minus_padding = {
        'fffffffff': 'r2n1',
        'hhhhhhhhh': 'r2n3',
        'ooooooooo': 'r4n3',
        'qqqqqqqqq': 'r4n4'
    }

    substitutions_whitespace_padding = {
        'aaaaaaaaa': 'topic',
        'ggggggggg': 'r2n2',
        'iiiiiiiii': 'r2n4',
        'nnnnnnnnn': 'r4n1',
        'ppppppppp': 'r4n2'
    }

    substitutions_minus_padding_left = {
        'ddddddddd': 'r1n3',
        'eeeeeeeee': 'r1n4',
        'jjjjjjjjj': 'r3n1',
        'mmmmmmmmm': 'r3n4'
        }

    substitutions_minus_padding_right = {
        'bbbbbbbbb': 'r1n1',
        'ccccccccc': 'r1n2',
        'kkkkkkkkk': 'r3n2',
        'lllllllll': 'r3n3'
        }

    template = printing_template[4]
    for key in substitutions_whitespace_padding:
        template = template.replace(key, substitutions_whitespace_padding[key][:9].center(9))
    for key in substitutions_minus_padding:
        template = template.replace(key, substitutions_minus_padding[key][:9].center(9, '-'))
        
    for key in substitutions_minus_padding_left:
        template = template.replace(key, substitutions_minus_padding_left[key][:9].ljust(9, '-'))
        
    for key in substitutions_minus_padding_right:
        template = template.replace(key, substitutions_minus_padding_right[key][:9].rjust(9, '-'))
    print(template)

def print_temp5():
    substitutions_center_minus = {
        'bbbbbbbbb': 'r1n1',
        'jjjjjjjjj': 'r2n4',
        'mmmmmmmmm': 'r3n2',
        'uuuuuuuuu': 'r4n5',
        'xxxxxxxxx': 'r5n3'
    }
        
    substitutions_center_whitespace = {
        'aaaaaaaaa': 'topic',
        'ccccccccc': 'r1n2',
        'fffffffff': 'r1n5',
        'iiiiiiiii': 'r2n3',
        'kkkkkkkkk': 'r2n5',
        'lllllllll': 'r3n1',
        'nnnnnnnnn': 'r3n3',
        'qqqqqqqqq': 'r4n1',
        'ttttttttt': 'r4n4',
        'wwwwwwwww': 'r5n2',
        'yyyyyyyyy': 'r5n4'
    }
    
    substitutions_left_minus = {
        'eeeeeeeee': 'r1n4',
        'ggggggggg': 'r2n1',
        'ppppppppp': 'r3n5',
        'rrrrrrrrr': 'r4n2',
        'vvvvvvvvv': 'r5n1'
        }
    
    substitutions_right_minus = {
        'ddddddddd': 'r1n3',
        'hhhhhhhhh': 'r2n2',
        'ooooooooo': 'r3n4',
        'sssssssss': 'r4n3',
        'zzzzzzzzz': 'r5n5'
        }




    template = printing_template[5]
    for key in substitutions_center_whitespace:
        template = template.replace(key, substitutions_center_whitespace[key][:9].center(9))
    for key in substitutions_center_minus:
        template = template.replace(key, substitutions_center_minus[key][:9].center(9, '-'))
        
    for key in substitutions_left_minus:
        template = template.replace(key, substitutions_left_minus[key][:9].ljust(9, '-'))
        
    for key in substitutions_right_minus:
        template = template.replace(key, substitutions_right_minus[key][:9].rjust(9, '-'))
    print(template)
