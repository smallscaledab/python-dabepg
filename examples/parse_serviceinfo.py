from dabepg.xml import unmarshall

si = unmarshall(open('SI.xml'))

for ensemble in si.ensembles:
    print ensemble
    
    for service in ensemble.services:
        print service
