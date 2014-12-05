from dabepg.xml import unmarshall

pi = unmarshall(open('PI.xml'))

print 'Scope:', pi.schedule.get_scope()
print '='* 40
for programme in pi.schedule.programmes:
    print programme
    for location in programme.locations:
        print '\t', ','.join([str(x) for x in location.times])
        print '\t', ','.join([str(x) for x in location.bearers])
    for media in programme.media:
        print media
    for genre in programme.genres:
        print genre
    for link in programme.links:
        print link
    for keyword in programme.keywords:
        print keyword
    print