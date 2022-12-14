import gi
from pint import UnitRegistry

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join

global changed_box_1
global changed_box_2

global unit_list
global combo_opt
global mtx_conv
global unit


config_in = open('./aula12/config.txt', 'r')

config_list = list(config_in.read().split('\n#\n'))

list_temp_name = list()
list_temp_val = list()

unit_list = list()
combo_opt = list()
mtx_conv = list()

unit = 0 #starts with the first unit (set in 0)

for combo_list in config_list:
    
    element_list =combo_list.split('\n')

    #Append do título da lista em outra lista(de títulos especificamente)
    unit_list.append(element_list[0])
    
    #Retirar o título da lista
    element_list.pop(0)

    for i in range(len(element_list)):
        
        name_value_list = element_list[i].split(' - ')

        list_temp_name.append(name_value_list[0].strip())
        list_temp_val.append(float(name_value_list[1].strip()))
    
    combo_opt.append(list_temp_name.copy())  
    mtx_conv.append(list_temp_val.copy())  
    list_temp_name = []
    list_temp_val = []

config_in.close()


class TheApp:
    '''The Application Class.'''

    def __init__(self):
        global combo_opt
        global unit_list
        global combo_1
        global combo_2
        global liststore, liststore_units
        
        
        
        # Build GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./aula12/execicio_glade.glade')
        # Get objects
        self.window = self.builder.get_object('window')
        # Cria uma array de duas colunas, a primeira para ser uma espécie de
        # identificador, ID, e a outra, o texto mostrado. Poderia ser uma
        # coluna int e outra string, caso os Ids fossem numéricos.
        liststore = self.liststore = Gtk.ListStore(int, str)
        liststore_units = self.liststore_units = Gtk.ListStore(int, str)

        # Initialize interface
        
        acum = 0
        temp_list = list()
        
        for i in range(len(unit_list)):
                
                temp_list.append(acum)
                temp_list.append(unit_list[i])
                
                self.liststore_units.append(temp_list.copy())
                temp_list = []
                
                acum += 1
                
        acum = 0
        
        print(combo_opt)
        print()
        
        acum = 0
        for el in combo_opt[0]:
            self.liststore.append([acum, el])
            acum += 1
        
        # Associando a array (ListStore) ao ComboBox
        self.combo_1 = self.builder.get_object('combo_box1')
        combo_1 = self.combo_1
        
        self.combo_2 = self.builder.get_object('combo_box2')
        combo_2 = self.combo_2
        
        self.combo_units = self.builder.get_object('combo_units')
        
        self.combo_1.set_model(self.liststore)
        self.combo_2.set_model(self.liststore)
        self.combo_units.set_model(self.liststore_units)
        # É necessário adicionar um renbderizador de texto ao ComboBox
        renderer_text = Gtk.CellRendererText()
        
        self.combo_1.pack_start(renderer_text, True)
        self.combo_2.pack_start(renderer_text, True)
        self.combo_units.pack_start(renderer_text, True)
        
        # Escolher qual coluna mostrar:
        self.combo_1.add_attribute(renderer_text, "text", 1)
        self.combo_2.add_attribute(renderer_text, "text", 1)
        self.combo_units.add_attribute(renderer_text, "text", 1)

        # Opção ativa default
        self.combo_1.set_active(0)
        self.combo_2.set_active(0)
        self.combo_units.set_active(0)

        # Connect signals
        self.builder.connect_signals(self)

        # Everything is ready
        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical window close button.'''
        Gtk.main_quit()

    def teste1_chg(self, dois):
        global changed_box_1, changed_box_2

        changed_box_2 = False
        changed_box_1 = True
        
        self.convert(1)
        
    
    def teste2_chg(self, dois):
        global changed_box_1, changed_box_2

        changed_box_2 = True
        changed_box_1 = False
        
        self.convert(2)
        
        
    def convert(self, ind_mud):
        global unit
        global mtx_conv
        global changed_box_1, changed_box_2
        
        
        ind_mud -= 1 #1 - vol_1 será convertido, 2 - vol_2 sera convertido
        
        vol_1 = self.builder.get_object("vol_1")
        vol_2 = self.builder.get_object("vol_2")
        
        model1 = self.combo_1.get_model()
        active1 = self.combo_1.get_active()
        
        model2 = self.combo_2.get_model()
        active2 = self.combo_2.get_active()
        
        
        ind_box1 = model1[active1][0]
        ind_box2 = model2[active2][0]
        
        if(ind_mud == 0):
            vol1_num = float(vol_1.get_text())
            var_num = vol1_num
            
            #recebe o obj que ira mudar
            var_obj = vol_2
            
            convert_const = mtx_conv[unit][ind_box2]/mtx_conv[unit][ind_box1]
            
            
        else:
            vol2_num = float(vol_2.get_text())
            var_num = vol2_num
            
            #recebe o obj que ira mudar
            var_obj = vol_1
            
            convert_const = mtx_conv[unit][ind_box1]/mtx_conv[unit][ind_box2]
                
        resp = var_num * convert_const
        var_obj.set_text(str(resp))
        
  
    def on_combo_unit_changed(self, combo):
        global combo_1
        global combo_2
        global combo_opt
        global unit
        
        global liststore, liststore_units
        
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            unit = model[tree_iter][0]
            
            print(unit)
            
            print(combo_opt)

            liststore.clear()
            acum = 0
            for el in combo_opt[unit]:
                liststore.append([acum, el])
                acum += 1

            combo_1.set_active(0)
            combo_2.set_active(0)

        
  
if __name__ == '__main__':
    try:
        gui = TheApp()
        Gtk.main()
    except KeyboardInterrupt:
        pass
