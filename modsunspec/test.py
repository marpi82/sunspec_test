#!/usr/bin/env python3

import sys
import time
import client_sync as client
import sunspec.core.suns as suns

if __name__ == "__main__":

    try:
        sd = client.SunSpecClientDevice(client.TCP, slave_id=0x02, ipaddr="192.168.11.169", ipport=1502, timeout=2)
        # sd = client.SunSpecClientDevice(client.RTU, options.a, name=options.p, baudrate=options.b, timeout=options.T)
    except client.SunSpecClientError as e:
        print('Error: %s' % (e))
        sys.exit(1)

    if sd is not None:
        f = open("result.txt", "w")
        txt = '\nTimestamp: %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        print(txt)
        f.write(txt)

        # read all models in the device
        sd.read()

        for model in sd.device.models_list:
            if model.model_type.label:
                label = '%s (%s)' % (model.model_type.label, str(model.id))
            else:
                label = '(%s)' % (str(model.id))
            txt = '\nmodel: %s\n' % (label)
            print(txt)
            f.write(txt)
            for block in model.blocks:
                if block.index > 0:
                    index = '%02d:' % (block.index)
                else:
                    index = '   '
                for point in block.points_list:
                    if point.value is not None:
                        if point.point_type.label:
                            label = '   %s%s (%s):' % (index, point.point_type.label, point.point_type.id)
                        else:
                            label = '   %s(%s):' % (index, point.point_type.id)
                        units = point.point_type.units
                        if units is None:
                            units = ''
                        if point.point_type.type == suns.SUNS_TYPE_BITFIELD16:
                            value = '0x%04x' % (point.value)
                        elif point.point_type.type == suns.SUNS_TYPE_BITFIELD32:
                            value = '0x%08x' % (point.value)
                        else:
                            value = str(point.value).rstrip('\0')
                        txt = '%-40s %20s %-10s' % (label, value, str(units))
                        print(txt)
                        f.write(txt + '\n')
        f.close()
    sd.close()
