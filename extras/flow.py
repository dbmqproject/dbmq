"""
Object flow filter.

For more information about flow file, check out
https://docs...
"""

import json


def ContainerConfigs(configs):
    data = {}
    data['Command'] = configs['Args'][-1]
    data['Hostname'] = configs['Config']['Hostname']
    data['Image'] = configs['Config']['Image']
    data['Distro'] = configs['Config']['Labels']['org.label-schema.name']
    data['WorkDir'] = configs['Config']['WorkingDir']
    data['IPAddress'] = configs['NetworkSettings']['Networks']['bridge']['IPAddress']
    data = json.dumps(data, indent=3,
                      separators=('', '\t->\t'))

    # TODO: Using Graphene in order to filter the JSON inspect
    return data
