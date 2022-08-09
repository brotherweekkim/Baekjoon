def solution(id_list, report, k):
    answer = []
    Hash_map = {}
    email = {}
    
    for id in id_list:
        Hash_map[id] = []
        email[id] = 0
        
    report = list(set(report))
    
    for i in range(len(report)):
        report_detail = (report[i].split())
        reporter = report_detail[0]
        reported = report_detail[1]
        Hash_map[reported].append(reporter)
    
    for key, val in Hash_map.items():
        if len(val) >= k:
            for e in val:
                email[e] += 1
    
    for val in email.values():
        answer.append(val)
    
        
    return answer