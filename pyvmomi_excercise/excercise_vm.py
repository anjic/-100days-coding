from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl
 
# Get all the Vms from vCenter server inventory and print its name
# Below is Python 2.7.x code, which can be easily converted to python 3.x version
 
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="172.30.60.89", user="root", pwd="p@ssw0rd",sslContext=s)
content=si.content
 
# Method that populates objects of type vimtype
def get_all_objs(content, vimtype):
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj
 
#Calling above method
getAllVms=get_all_objs(content, [vim.VirtualMachine])
 
#Iterating each vm object and printing its name
# print dir(getAllVms)
for vm in getAllVms:
    # if vm.name == 'UDS Server':
    v = vm.storage
    print dir(v)
    # print type(vm.storage)
    # print type(vm)storage