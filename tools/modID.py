import xml.etree.ElementTree as ET

class modID:
    def __init__(self, modsettings_dir=None):
        self.modsettings_dir = modsettings_dir
    
    def getUUID(self, pak_file):
        tree = self._parse_modsettings()
        mods_node = tree.find("./node[@id='Mods']")
        
        for module_node in mods_node.iter("node"):
            if module_node.attrib.get('id') == 'ModuleShortDesc':
                folder_attr = module_node.find("./attribute[@id='Folder']")
                if folder_attr is not None and folder_attr.attrib.get('value') == pak_file:
                    uuid_attr = module_node.find("./attribute[@id='UUID']")
                    if uuid_attr is not None:
                        return uuid_attr.attrib.get('value')
        
        return None
    
    def getLoadorder(self, uuid):
        tree = self._parse_modsettings()
        mod_order_node = tree.find("./node[@id='ModOrder']")
        
        for module_node in mod_order_node.iter("node"):
            uuid_attr = module_node.find("./attribute[@id='UUID']")
            if uuid_attr is not None and uuid_attr.attrib.get('value') == uuid:
                load_order = module_node.attrib.get('order')
                if load_order is not None:
                    return str(load_order).zfill(3)
        
        return None
    
    def _parse_modsettings(self):
        modsettings_file = "modsettings.lsx"
        if self.modsettings_dir:
            modsettings_file = f"{self.modsettings_dir}/{modsettings_file}"
        
        tree = ET.parse(modsettings_file)
        return tree