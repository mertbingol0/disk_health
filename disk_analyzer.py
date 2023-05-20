import subprocess as sb
import json

def disk_test():
    first_disk = '/dev/sda'
    secon_disk = '/dev/sdb'

    test_output_1 = sb.check_output(['sudo', 'smartctl', '-H', first_disk]).decode()
    test_output_2 = sb.check_output(['sudo', 'smartctl', '-H', secon_disk]).decode()

    if 'PASSED' in test_output_1:
        first_disk_status = f'{first_disk} named disk is working \U0001F607'
    else:
        first_disk_status = f'{first_disk} named disk is not working \U0001F620'

    if 'PASSED' in test_output_2:
        second_disk_status = f'{secon_disk} named disk is working \U0001F607 '
    else:
        secons_disk_status = f'{secon_disk} named disk is not working \U0001F620'

    data =      {
        'disk1': first_disk_status,
        'disk2': second_disk_status
        }

    with open('disk_status.json', 'w') as f:
        json.dump(data, f)

disk_test()
