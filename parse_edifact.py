from collections import namedtuple
import json


def parse_prd(prd_line):
    company_1_id = None
    company_2_id = None
    elements = prd_line.split('+')
    
    if '**' in elements[-1]:
        companies = elements[-1].split('**')
        company_1_id = companies[0]   
        company_2_id = companies[1]
    else:
        company_1_id = elements[-1]

    fes = elements[1].split(':')
    fes_length = len(fes)
    if fes_length < 4:
        fes += [None] * (4 - fes_length)

    return {
        'company_1_id': company_1_id,
        'company_2_id': company_2_id,
        'train_service_id': fes[0],
        'service_character': fes[1],
        'pricing_category': fes[2],
        'item_description_code': fes[3]
    }


def parse_pop(pop_line):
    elements = pop_line.split('+')
    components = elements[1].split(':')
    dates = components[1].split('/')
    start_date = dates[0]
    end_date = dates[1]
    return {
        'start_date': start_date,
        'end_date': end_date,
        'period_days': components[3]
    }

def parse_als(als_line):
    elements = als_line.split('+')
    location_type = elements[1]
    components = elements[2].split(':')
    location_id = components[0]
    name = components[1]
    longitude = elements[3]
    latitude = elements[4]
    return {
        'location_id': location_id,
        'location_type': location_type,
        'name': name,
        'longitude': longitude,
        'latitude': latitude
    }


def parse_por(por_line):

    elements = por_line.split('+')
    location_id = elements[1]
    time = elements[2].split('*')

    if len(time) == 2:
        arrival_time = time[0]
        departure_time = time[1]
    else:
        arrival_time = elements[2]
        departure_time = ''

    return {
        'location_id': location_id,
        'arrival_time': arrival_time,
        'departure_time': departure_time
    }

def parse_pdt(pdt_line):
    elements = pdt_line.split('+')
    components = elements[2].split(':')
    train_type = components[3]
    return {
        'train_type': train_type
        }



def parse_segment(lines):
    global output
    list_por = []
    if lines == []:
        return None
    if lines[0][:3] != 'PRD':
        raise Exception('First line of segment is not PRD')
    pop, prd, start_date, end_date = {}, {}, None, None
    pdt = {'train_type': None}
    train_service_id = None
    for line in lines:
        if line[:3] == 'PRD':
            prd = parse_prd(line)
            train_service_id = prd['train_service_id']
        if line[:3] == 'POP':
            pop = parse_pop(line)
            start_date = pop['start_date']
            end_date = pop['end_date']
        if line[:3] == 'PDT':
            pdt = parse_pdt(line)
        if line[:3] == 'POR':
            por = parse_por(line)
            list_por.append(por)

    if pdt == {}:
        print('PDT IS NONE!', train_service_id)


    output[train_service_id + '_' + start_date + ' ' + end_date] = {
        'train_service': {**prd, **pop, **pdt},
        'train_timetable': list_por

    }


if __name__ == '__main__':
    output = {}
    segment = []

    with open('SKDUPD.20160624082533_3.r') as f:
        for line in f:
            if line[:3] == 'HDR':
                break
        for line in f:
            if line[:3] == 'PRD':
                parse_segment(segment)
                segment = [line.rstrip()]
            if line[:3] != 'PRD':
                segment.append(line.rstrip())


#    print(json.dumps(output))
