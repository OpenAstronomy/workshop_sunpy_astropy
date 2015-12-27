import json

def instructor_to_student(instructor_ipynb):
    '''
    Removes all the output of the cells and the code of these
    cells without a keep flag in their metadata, but keeps the
    commented lines.

    '''
    
    with open(instructor_ipynb, 'r') as file_instructor:
        notebook = json.load(file_instructor)

    cells = notebook['cells']

    cells_student = list()
    for cell in cells:
        if cell['cell_type'] != 'code':
            cells_student.append(cell)
        else:
            cell['outputs'] = list()
            if cell['metadata'].has_key('keep'):
                cells_student.append(cell)
            else:
                source = list()
                for elem in cell['source']:
                    if elem.startswith('#'):
                        source.append(elem)
                cell['source'] = source
                cells_student.append(cell)

    student_ipynb = instructor_ipynb.replace('_Instructor', '')
    notebook_student = notebook
    notebook_student['cells'] = cells_student

    tojson = json.JSONEncoder()
    with  open(student_ipynb, 'w') as file_student:
        json.dump(notebook_student, file_student, indent=1,separators=(',', ': '))

    return

if __name__ == '__main__':
    instructor_to_student('Units_Quantities_Instructor.ipynb')

