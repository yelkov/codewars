def domain_name(url):
    protocol = 'https://www.'
    protocolLocation = url.find(protocol)
    
    if protocolLocation == -1:
        protocol = 'http://www.'
        protocolLocation = url.find(protocol)

    if protocolLocation == -1:
        protocol = 'https://'
        protocolLocation = url.find(protocol)

    if protocolLocation == -1:
        protocol = 'http://'
        protocolLocation = url.find(protocol)

    if protocolLocation == -1:
        protocol = 'www.'
        protocolLocation = url.find(protocol)
        
    if protocolLocation == -1:
        protocol = ''
        protocolLocation = None
    
    endProtocolLocation = len(protocol)
    extensionLocation = url.find('.',endProtocolLocation)
    return url[endProtocolLocation:extensionLocation]
    