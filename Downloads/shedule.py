import sys
import pickle

class Main:
    def __init__(self):
        self.display_menu()
        self.load_data()		
    def load_data(self):
        inp_file = open('db.obj', 'r')
        self.data = pickle.load(inp_file)
        inp_file.close()	
    def display_menu(self):
        menu_list = ['Veiw shedule', 'Add entry', 'Edit entry', 
                     'Delete entry', 'Exit']
        print ''
        print 'Type the number of your choice:'
        print ''
        for i in range(1, len(menu_list)+1):
            print str(i) + ' ' + menu_list[i-1]
        choice = raw_input('Your choice: ')
        self.menu_choice(choice)
    def menu_choice(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
        if choice == 1:
            self.shedule_table()
            self.display_menu()			
        elif choice == 2:
            self.add_entry()
            self.display_menu()			
        elif choice == 3:
            self.edit_entry()
            self.display_menu()
        elif choice == 4:
            self.del_entry()
            self.display_menu()			
        elif choice == 5:
            self.exit_script()
        else:
            print "That wasn't a valid option. Try again"
            self.display_menu()
    def shedule_table(self):
        self.load_data()	
        heads = {'No': ['Departure station', 'Departure time', 
                        'Arrival station', 'Arrival time']}	
        for key, lists in heads.items():
            print '+-' + '-'*len(key) + '-+-' + '-'*len(lists[0]) +\
                  '-+-' + '-'*len(lists[1]) + '-+-' +\
                  '-'*len(lists[2]) + '-+-' + '-'*len(lists[3]) + '-+'				
            print '| ' + key + ' | ' + lists[0] + ' | ' + lists[1] +\
                  ' | ' + lists[2] + ' | ' + lists[3] + ' |'
            print '+-' + '-'*len(key) + '-+-' + '-'*len(lists[0]) +\
                  '-+-' + '-'*len(lists[1]) + '-+-' +\
                  '-'*len(lists[2]) + '-+-' + '-'*len(lists[3]) + '-+'
        for key, lists in self.data.items():
            if len(str(key)) < 2:
                print '|  ' + str(key) + ' | ' + lists[0] + ' '*(17 - len(lists[0])) + ' | ' + lists[1] +\
                  ' '*(14 - len(lists[1])) + ' | ' + lists[2] + ' '*(15 - len(lists[2])) + ' | ' + lists[3] + ' '*(12 - len(lists[3]))+ ' |'
            else:
                print '| ' + str(key) + ' | ' + lists[0] + ' | ' + lists[1] +\
                  ' | ' + lists[2] + ' | ' + lists[3] + ' |'
        print '+-' + '-'*2 + '-+-' + '-'*17 +\
                  '-+-' + '-'*14 + '-+-' +\
                  '-'*15 + '-+-' + '-'*12 + '-+'				  
    def add_entry(self):
        self.load_data()	
        shed = []
        num_entry = input('Enter number of entry: ')
        if num_entry in self.data:
            print 'Entered number is already in the shedule. Enter another number'
            self.add_entry()
        else:			
            dep_stat = raw_input('Enter departure station: ')
            shed.append(dep_stat)
            dep_time = raw_input('Enter departure time: ')
            shed.append(dep_time)
            arr_stat = raw_input('Enter arrival station: ')
            shed.append(arr_stat)
            arr_time = raw_input('Enter arrival time: ')
            shed.append(arr_time)
            self.data[int(num_entry)] = shed
            self.save_changes()		
    def exit_script(self):
        s = raw_input('Do you really want to exit? (Y/N)')
        if s == 'Y' or s == 'y':
            sys.exit(0)
        elif s == 'N' or s == 'n':
            self.display_menu()
        else:
            print 'You entered wrong value. Try again'
            self.exit_script()
    def save_changes(self):
        s = raw_input('Do you want to save changes? (Y/N)')
        if s == 'Y' or s == 'y':
            inp_file = open('db.obj', 'w')			
            pickle.dump(self.data, inp_file)
            inp_file.close()			
        elif s == 'N' or s == 'n':
            self.display_menu()
        else:
            print 'You entered wrong value. Try again'
            self.save_changes()	
    def del_entry(self):
        self.load_data()
        del_ent = input('Enter number of entry you want to delete: ')
        try:		
            del self.data[del_ent]
        except KeyError:
            print "This number isn't in the shedule. Try again"
            self.del_entry()			
        self.save_changes()
    def edit_entry(self):
        self.load_data()	
        self.edit_ent = input('Enter number of entry you want to edit: ')
        if self.edit_ent in self.data:
            self.entry = self.data[self.edit_ent]		
            self.edit_ds()
        else:
            print "This number isn't in the shedule. Try again"
            self.edit_entry()
    def edit_art(self):
        print 'Is arrival time %s correct? ' %self.entry[3], 
        art = raw_input('(Y/N)')
        if art == 'Y' or art == 'y':
            self.save_changes()						
        elif art == 'N' or art == 'n':
            new_art = raw_input('Enter new arrival time: ')
            self.data[self.edit_ent][3] = new_art
            self.save_changes()
        else:
            print 'You entered wrong value. Try again'
            self.edit_art()			
    def edit_ars(self):
        print 'Is arrival station %s correct? ' %self.entry[2], 
        ars = raw_input('(Y/N)')
        if ars == 'Y' or ars == 'y':
            self.edit_art()							
        elif ars == 'N' or ars == 'n':
            new_ars = raw_input('Enter new arrival station: ')
            self.data[self.edit_ent][2] = new_ars
            self.edit_art()
        else:
            print 'You entered wrong value. Try again'
            self.edit_ars()			
    def edit_dt(self):
        print 'Is departure time %s correct? ' %self.entry[1], 
        dt = raw_input('(Y/N)')
        if dt == 'Y' or dt == 'y':
            self.edit_ars()        					
        elif dt == 'N' or dt == 'n':
            new_dt = raw_input('Enter new departure time: ')
            self.data[self.edit_ent][1] = new_dt
            self.edit_ars()
        else:
            print 'You entered wrong value. Try again'
            self.edit_dt()			
    def edit_ds(self):
        print 'Is departure station %s correct? ' %self.entry[0], 
        ds = raw_input('(Y/N)')
        if ds == 'Y' or ds == 'y':
            self.edit_dt()				
        elif ds == 'N' or ds == 'n':
            new_ds = raw_input('Enter new departure station: ')
            self.data[self.edit_ent][0] = new_ds
            self.edit_dt()
        else:
            print 'You entered wrong value. Try again'
            self.edit_ds()			
if __name__ == '__main__':
    Main()