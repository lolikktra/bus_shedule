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
            self.delete_entry()
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
        shedule = []
        try:		
            num_entry = input('Enter number of entry: ')
        except NameError:
            print "That wasn't a number. Try again"
            self.add_entry()
        else:			
            if num_entry in self.data:
                print 'Entered number is already in the shedule. Enter another number'
                self.add_entry()
            else:			
                departure_station = raw_input('Enter departure station: ')
                shedule.append(departure_station)
                departure_time = raw_input('Enter departure time: ')
                shedule.append(departure_time)
                arrival_station = raw_input('Enter arrival station: ')
                shedule.append(arrival_station)
                arrival_time = raw_input('Enter arrival time: ')
                shedule.append(arrival_time)
                self.data[int(num_entry)] = shedule
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

    def delete_entry(self):
        self.load_data()
        try:
            del_entry = input('Enter number of entry you want to delete: ')
            del self.data[del_entry]
        except (KeyError, NameError):
            print "This number isn't in the shedule. Try again"
            self.delete_entry()
        else:			
            self.save_changes()

    def edit_entry(self):
        self.load_data()
        try:		
            self.edit_ent = input('Enter number of entry you want to edit: ')
        except NameError:
            print "That wasn't a valid option. Try again"
            self.edit_entry()
        else:			
            if self.edit_ent in self.data:
                self.entry = self.data[self.edit_ent]		
                self.edit_departure_station()
            else:
                print "This number isn't in the shedule. Try again"
                self.edit_entry()

    def edit_arrival_time(self):
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
            self.edit_arrival_time()

    def edit_arrival_station(self):
        print 'Is arrival station %s correct? ' %self.entry[2], 
        ars = raw_input('(Y/N)')
        if ars == 'Y' or ars == 'y':
            self.edit_arrival_time()							
        elif ars == 'N' or ars == 'n':
            new_ars = raw_input('Enter new arrival station: ')
            self.data[self.edit_ent][2] = new_ars
            self.edit_arrival_time()
        else:
            print 'You entered wrong value. Try again'
            self.edit_arrival_station()

    def edit_departure_time(self):
        print 'Is departure time %s correct? ' %self.entry[1], 
        dt = raw_input('(Y/N)')
        if dt == 'Y' or dt == 'y':
            self.edit_arrival_station()        					
        elif dt == 'N' or dt == 'n':
            new_dt = raw_input('Enter new departure time: ')
            self.data[self.edit_ent][1] = new_dt
            self.edit_arrival_station()
        else:
            print 'You entered wrong value. Try again'
            self.edit_departure_time()

    def edit_departure_station(self):
        print 'Is departure station %s correct? ' %self.entry[0], 
        ds = raw_input('(Y/N)')
        if ds == 'Y' or ds == 'y':
            self.edit_departure_time()				
        elif ds == 'N' or ds == 'n':
            new_ds = raw_input('Enter new departure station: ')
            self.data[self.edit_ent][0] = new_ds
            self.edit_departure_time()
        else:
            print 'You entered wrong value. Try again'
            self.edit_departure_station()

if __name__ == '__main__':
    Main()