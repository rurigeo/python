new = open('dns', 'w')
with open('openwrt.dns', 'r') as f:
    for line in f:
        line = '\tlist ' + line.rstrip() + '\'\n'
        new.write(line)
new.close()
