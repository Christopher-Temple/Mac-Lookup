def get_vendor(macid):

    ouiList = []
    filehandle = open("oui.txt", 'r')
    dataList = filehandle.read()

    for vendor in dataList.split('\n'):
        ouiList.append(vendor.strip())
    for i in ouiList:
        if macid in i:
            return i[7:]



