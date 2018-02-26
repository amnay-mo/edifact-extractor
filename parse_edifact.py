from collections import namedtuple



def parse_prd(prd_line):
    elements = prd_line.split('+')
    company_id = elements[-1]
    fes = elements[1].split(':')
    return {
        'company_id': company_id,
        'train_service_id': fes[0],
        'service_character': fes[1],
        'pricing_category': fes[2],
        'item_description_code': fes[3]
    }

def parse_pop(pop_line):
    elements = pop_line.split('+')
    components = elements.split(':')
    dates = components[1].split('/')
    start_date = dates[0]
    end_date = dates[1]



def parse_segment(lines):
    global prds
    if lines[0][:3] != 'PRD':
        raise Exception('First line of segment is not PRD')
    prds.append(parse_prd(lines[0]))


if __name__ == '__main__':
    prds = []
    segment = []
    with open('test.r') as f:
        for line in f:
            if line[:3] == 'HDR':
                break
        for line in f:
            if line[:3] == 'PRD':
                parse_segment(segment)
                segment = [line.rstrip()]
            if line[:3] != 'PRD':
                segment.append(line.rstrip())

