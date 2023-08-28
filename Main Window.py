import tkinter
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os
import openpyxl

global filepath

filepath = "D:\Software\Data Sheet.xlsx"   #Please change this individual variable value, place in the location of the downloaded data sheet between the " "

#DEFINED SPEERATELY TO ALLOW CONNECTION TO IT LATER
def mainmenu():
    window_main = tkinter.Tk()
    window_main.title('Main Menu')
    window_main.resizable(False, False)   #Ensuring that the user cannot resize the window

    window_width = 800     #set window dimensions that are used throughout to create consistanty
    window_height = 600

    # get the screen dimension
    screen_width =  window_main.winfo_screenwidth()
    screen_height = window_main.winfo_screenheight()

    # finding the center point of the screen of the user (will adapt depending on user screen)
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window_main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #Start of all the code applicable to the Application page 1 of the program
    frame = tkinter.Frame( window_main)  #Main frame       #Define Widget
    frame.pack()       #Pack, place or grid widget


    frame = tkinter.Frame(window_main)  #Main frame       #Define Widget
    frame.pack()       #Pack, place or grid widget

    #User information label
    welcome_frame =tkinter.LabelFrame(frame, text="Welcome to the Small Buisness Application form", font=("Arial", 20), fg="#000080")   #Main heading
    welcome_frame.grid(row=0, column=0, sticky="news") 

    global filepath     #File path for the location of the data sheet

    def quit():   #Quit function
        for widget in window_main.winfo_children():
            widget.destroy()
        window_main.destroy()
    

    
    def employer():
        window_main.iconify()  #Destroying the main menu window once the button was pressed and the new page is opened


        # LOGIN PAGE FOR THE EMPLOYER
        window_login = tkinter.Toplevel()
        window_login.title('Login Page')    #Login page title 

        window_width = 800
        window_height = 600

        # get the screen dimension
        screen_width =  window_login.winfo_screenwidth()
        screen_height = window_login.winfo_screenheight()

        # finding the center point of the screen of the user (will adapt depending on user screen)
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        window_login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        frame_login = tkinter.Frame(window_login)  #Main frame       #Define Widget
        frame_login.pack()       #Pack, place or grid widget

        def login():
            username = "johnsmith"    #Allowable username for the login section
            password = "12345"        #Password for the username
            if username_entry.get()==username and password_entry.get()==password:   #getting the username and password that was inputted and seeing if they match
                messagebox.showinfo(title="Login Success", message="You successfully logged in.") #login success message
                window_login.iconify()   #closing the main window

                #Following lines 7-22 can and will be used for each subprogram
                root_criteria = tkinter.Toplevel()
                root_criteria.title('Criteria Search')    #create search pages

                window_width = 800
                window_height = 600

                # get the screen dimension
                screen_width = root_criteria.winfo_screenwidth()
                screen_height = root_criteria.winfo_screenheight()

                # finding the center point of the screen of the user (will adapt depending on user screen)
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                # set the position of the window to the center of the screen
                root_criteria.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                framec_user = tkinter.Frame(root_criteria)  #Main frame       #Define Widget
                framec_user.pack()       #Pack, place or grid widget

                main_frame =tkinter.LabelFrame(framec_user, text="Criteria Search", font=("Arial", 20), fg="#000080")
                main_frame.grid(row=0, column=0, sticky="news") 

                info_label = tkinter.Label(main_frame, text="Please select the Criteria you would like to search by: ", font=("Arial", 10), fg="#000080")
                info_label.grid(row=0, column=0)

                answer_criteria = tkinter.StringVar()     #The varibale collected by the radio buttons will all be strings
                answer_criteria.set(' ')    #Starting the buttons as none set

                def search_criteria_1():
                        criteria_search = answer_criteria.get()   ##setting a variable for easier use later

                        if criteria_search:                     #Ensuring that something was selected
                            root_criteria.iconify()

                #JOB SUBSECTION FOR THE CRITERIA SEARCH
                            if criteria_search == "Job":      
                                #Following lines 7-22 can and will be used for each subprogram
                                root_job = tkinter.Toplevel()
                                root_job.title('Job Criteria Search')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = root_job.winfo_screenwidth()
                                screen_height = root_job.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                root_job.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(root_job)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                main_frame =tkinter.LabelFrame(frame_user, text="Job Criteria Search", font=("Arial", 20), fg="#000080")
                                main_frame.grid(row=0, column=0, sticky="news") 

                                info_label = tkinter.Label(main_frame, text="Please select the Job you wish to search your applicants by:", font=("Arial", 10), fg="#000080")
                                info_label.grid(row=0, column=0)

                                global radio_job
                                radio_job = tkinter.StringVar()
                                radio_job.set(' ')          #ENSURES THAT IT STARTS WITH NONE SELECTED


                                #JOB SEARCH SUBSECTION
                                def search_job():
                                        root_job.iconify()   #MAKING   root_job into an icon, shrink to the bottom of the screen

                                        global radio_job            #radio_job has to be global for use in later subprograms
                                        job_selected = radio_job.get()   #changing the variable to make it more applicable later
                                        #Following lines 7-22 can and will be used for each subprogram
                                        root_job_file = tkinter.Toplevel()
                                        root_job_file.title('Job Files')

                                        window_width = 800
                                        window_height = 600

                                        # get the screen dimension
                                        screen_width = root_job_file.winfo_screenwidth()
                                        screen_height = root_job_file.winfo_screenheight()

                                        # finding the center point of the screen of the user (will adapt depending on user screen)
                                        center_x = int(screen_width/2 - window_width / 2)
                                        center_y = int(screen_height/2 - window_height / 2)

                                        # set the position of the window to the center of the screen
                                        root_job_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                        frame_user = tkinter.Frame(root_job_file)  #Main frame       #Define Widget
                                        frame_user.pack()       #Pack, place or grid widget

                                        info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                        info_frame.grid(row=0, column=0, sticky="news") 

                                        button_frame = tkinter.Frame(frame_user)
                                        button_frame.grid(row=1, column=0)

                                        frame_user.pack()
                                        
                                        global filepath
                                        #Setting constant variables



                                        #Defining each of the columns within the spreadsheet to improve the intrinsic documentation
                                        job_col= pd.read_excel(filepath, usecols='A')     #Column for the job is the first column in spreadsheet and therefore A

                                        #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                        data_sheet = pd.read_excel(filepath)   #Loads the excel file
                                        end = len(data_sheet. index)   #checks where the end of the file is
                                        last = end-1   #this over estimates by 1 as it assumes starting on 1 not 0
                                        count = 0    #starting count on 0 for the later loop
                                        criteria_list = [""]   #starting the list to be used later
                                        criteria_list.clear()   #clearing the list
                                        global number    #globalising number before it is set
                                        number = -1 



                                        #LOOP TO GET ALL THE DATA INTO THE LIST BASED ON THE CRITERA
                                        while count <= last:              #LOOPING BASED ON THE DATA PROVIDED
                                            current = job_col.iloc[count]
                                            string = str(current)
                                            if (job_selected in string or "All" in string):   #CHECKING IF SELECTED CRITERIA OR ALL IS IN THE STRING
                                                criteria_list.append(count)
                                                count = count+1   
                                            else:
                                                count=count+1

                                        listnumber=len(criteria_list)    #finding the ammount of variables in the list
                                        global truelistnumber
                                        truelistnumber = listnumber-1      #STARTS AT 0 not assummed 1
                                            #starting the NEXT  rountine function
                                        def next():
                                            global number  #getting all the global variable
                                            global truelistnumber
                                            if number < truelistnumber: #ensuring it isn't the last variable in the list
                                                number = number+1  #is it isn't it will increment
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()
                                                current = data_sheet.iloc[criteria_list[number]]     #from the data sheet it will display the information from the given row
                                                application_label = tkinter.Label(info_frame, text=current) #dispalying loaded data
                                                application_label.grid(row=0, column=0, pady=10, padx=5)  #location on the data
                                            else: 
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")   #if it was the last varaible it can not display anymore

                                        #BACK BUTTON FUCNTION
                                        def back():
                                            global number
                                            if number > 0:  #ensuring it isn't the first varaible in the list
                                                number = number-1 
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()     #removing the cucrrent data being displayed before dispalying new data
                                                current = data_sheet.iloc[criteria_list[number]]
                                                application_label = tkinter.Label(info_frame, text=current) 
                                                application_label.grid(row=0, column=0, pady=10, padx=5) 
                                            
                                            else:
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                            

                                        button_return_frame = tkinter.Frame(frame_user)
                                        button_return_frame.grid(row=2, column=0) 
                                            
                                        return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                        width=30, pady=10)
                                        return_button.grid(row=1, column = 0)


                                        applicant_label = tkinter.Label(info_frame, text="Please Click next to display application") 
                                        applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                        next_button = tkinter.Button(
                                            button_frame, text="Next", command=next, width=30, pady=10)
                                        next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                        back_button = tkinter.Button(
                                            button_frame, text="Back", command=back, width=30, pady=10)
                                        back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)



                                        root_job_file.mainloop()

                                #the buttons for within the job criteria search that are linked to the string variable already set previously

                                manager_button = tkinter.Radiobutton(main_frame, text="Manager", variable=radio_job, value="Manager")  
                                manager_button.grid(row=2, column=0, padx=10)

                                marketing_button = tkinter.Radiobutton(main_frame, text="Marketing Management", variable=radio_job,  value="Marketing Management")
                                marketing_button.grid(row=3, column=0, padx=10)

                                accounting_button = tkinter.Radiobutton(main_frame, text="Accounting Internship",variable=radio_job,  value="Accounting Internship")
                                accounting_button.grid(row=4, column=0, padx=10)

                                customer_button = tkinter.Radiobutton(main_frame, text="Customer Service Representative",variable=radio_job,  value="Customer Service Representative")
                                customer_button.grid(row=5, column=0, padx=10)


                                #universal padding for all the radio buttons on the screen
                                for widgets in main_frame.winfo_children():
                                            widgets.configure(padx=20, pady=20)

                                #search button that links to the subsection
                                search_button = tkinter.Button(main_frame, command=search_job, width=30, pady=10, text="Search")
                                search_button.grid(row=6, column=0)

                                frame_user.pack()
                                root_job.mainloop()



                #PAY SECTION FOR THE SEARCH
                            elif criteria_search == "Pay":

                                #Following lines 7-22 can and will be used for each subprogram
                                root_pay = tkinter.Toplevel()
                                root_pay.title('Pay Criteria Search')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = root_pay.winfo_screenwidth()
                                screen_height = root_pay.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                root_pay.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(root_pay)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                main_frame =tkinter.LabelFrame(frame_user, text="Pay Criteria Search", font=("Arial", 20), fg="#000080")
                                main_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20) 

                                info_frame = tkinter.Frame(main_frame)
                                info_frame.grid(row=0, column=0)

                                widget_frame= tkinter.Frame(main_frame)
                                widget_frame.grid(row=1, column=0)

                                button_frame = tkinter.Frame(main_frame)
                                button_frame.grid(row=2, column=0)

                                info_label = tkinter.Label(info_frame, text="Please use the menus below to set the pay criteria for you applicants ", font=("Arial", 10), fg="#000080")
                                info_label.grid(row=0, column=0, padx=20, pady=20)

                                intruction_label = tkinter.Label(info_frame, text="I would like to veiw applicants with a pay that is.......", font=("Arial", 10), fg="#000080")
                                intruction_label.grid(row=1, column=0, padx=20, pady=20)

                                white_space_label = tkinter.Label(widget_frame, text="")
                                white_space_label.grid(row=2, column=0)

                                symbol_combobox = ttk.Combobox(widget_frame, values=["", "Greater then", "Equal to", "Less then"])
                                symbol_combobox.grid(row=3, column=0, padx=40, pady=40)

                                number_spinbox = ttk.Spinbox(widget_frame, from_=0, to=100)
                                number_spinbox.grid(row=3, column=1, pady=40)

                                end_label = tkinter.Label(widget_frame, text="$/hr", font=("Arial", 10), fg="#000080")
                                end_label.grid(row=3, column=2, pady=40)



                                #SEARCH BUTTON FUCNTION

                                def search_pay():
                                    global filepath
                                    #LOOOPS FOR FINDING DATA
                                    

                                    #Defining each of the columns within the spreadsheet to improve the intrinsic documentation
                                    pay_col = pd.read_excel(filepath, usecols='L')

                                    #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                    data_sheet = pd.read_excel(filepath)
                                    end = len(data_sheet. index)
                                    last = end-1
                                    count = 0 
                                    criteria_list = [""]
                                    criteria_list.clear()
                                    global number
                                    number = -1  
                                #Specific to this loop with the values being checked

                                    symbol = symbol_combobox.get()
                                    number_given = number_spinbox.get()
                                    if number_given:                              #CHECKS IF NUMBER HAS BEEN ENTERED
                                        if symbol:                          #CHECKS IF SYMBOL HAS BEEN ENTERED
                                            root_pay.iconify()
                                            root_pay_file = tkinter.Toplevel()
                                            root_pay_file.title('Pay Search Files')

                                            window_width = 800
                                            window_height = 600

                                            # get the screen dimension
                                            screen_width = root_pay_file.winfo_screenwidth()
                                            screen_height = root_pay_file.winfo_screenheight()

                                            # finding the center point of the screen of the user (will adapt depending on user screen)
                                            center_x = int(screen_width/2 - window_width / 2)
                                            center_y = int(screen_height/2 - window_height / 2)

                                            # set the position of the window to the center of the screen
                                            root_pay_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                            frame_user = tkinter.Frame(root_pay_file)  #Main frame       #Define Widget
                                            frame_user.pack()       #Pack, place or grid widget

                                            info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                            info_frame.grid(row=0, column=0, sticky="news") 

                                            button_frame = tkinter.Frame(frame_user)
                                            button_frame.grid(row=1, column=0)

                                            frame_user.pack()


                                #LOOPING BASED ON BEING GREATER THEN
                                            if symbol == "Greater then":
                                                while count <= last:              
                                                    current = int(pay_col.iloc[count])                  #CHANGING THE VALUE INTO AN INTEGER
                                                    int_number_given = int(number_given)                     #USING THE GLOBAL VALUE FOR THE INPUT NUMBER
                                                    if current > int_number_given:          # IF THE CURRENT PAY NUMBER IS GREATER THEN THE INPUTTED NUMBER IT WILL...
                                                        criteria_list.append(count)               # ADD IT TO THE LIST
                                                        count = count+1                           # INCREMENT BY 1
                                                    else:
                                                        count=count+1

                                #LOOPING BASED ON BEING EQUAL TO
                                            elif symbol == "Equal to":
                                                while count <= last:             
                                                    current = int(pay_col.iloc[count])
                                                    int_number_given = int(number_given)
                                                    if current == int_number_given:   
                                                        criteria_list.append(count)
                                                        count = count+1   
                                                    else:
                                                        count=count+1

                                #LOOPING BASED ON BEING LESS THEN
                                            elif symbol == "Less then":
                                                while count <= last:              
                                                    current = int(pay_col.iloc[count])
                                                    int_number_given = int(number_given)
                                                    if current < int_number_given:   #CHECKING IF SELECTED CRITERIA OF WORKA IS IN THE STRING
                                                        criteria_list.append(count)
                                                        count = count+1   
                                                    else:
                                                        count=count+1

                                            listnumber=len(criteria_list)
                                            global truelistnumber
                                            truelistnumber = listnumber-1      #STARTS AT 0 not assummed 1



                                    #NEXT BUTTON FUNCTION
                                            def next():
                                                global number
                                                global truelistnumber
                                                global truelistnumber
                                                if number < truelistnumber:
                                                    number = number+1 
                                                    for widgets in info_frame.winfo_children():
                                                        widgets.destroy()
                                                    current = data_sheet.iloc[criteria_list[number]]
                                                    application_label = tkinter.Label(info_frame, text=current) 
                                                    application_label.grid(row=0, column=0, pady=10, padx=5) 
                                                else: 
                                                    tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                            #BACK BUTTON FUCNTION
                                            def back():
                                                global number
                                                if number > 0:
                                                    number = number-1 
                                                    for widgets in info_frame.winfo_children():
                                                        widgets.destroy()
                                                    current = data_sheet.iloc[criteria_list[number]]
                                                    application_label = tkinter.Label(info_frame, text=current) 
                                                    application_label.grid(row=0, column=0, pady=10, padx=5) 
                                                
                                                else:
                                                    tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                                


                                    #THE DISPLAY FOR THE PAY FILES

                                            button_return_frame = tkinter.Frame(frame_user)
                                            button_return_frame.grid(row=2, column=0) 
                                            
                                            return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                        width=30, pady=10)
                                            return_button.grid(row=1, column = 0)
                                            
                                            applicant_label = tkinter.Label(info_frame, text="Please Click next to display application") 
                                            applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                            next_button = tkinter.Button(
                                                button_frame, text="Next", command=next, width=30, pady=10)
                                            next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                            back_button = tkinter.Button(
                                                button_frame, text="Back", command=back, width=30, pady=10)
                                            back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)



                                            root_pay_file.mainloop()


                                        else:
                                            tkinter.messagebox.showwarning(title= "Missing", message= "The symbol/operator is required")      #ERROR MESSAGE FOR NO SYMBOL
                                    else:
                                        tkinter.messagebox.showwarning(title= "Missing", message= "The number for the pay is required.")      #ERROR MESSAGE FOR NO NUMBER






                                search_button = tkinter.Button(button_frame, command=search_pay, width=30, pady=10, text="Search")
                                search_button.grid(row=6, column=0)

                                frame_user.pack()


                                root_pay.mainloop()


                #EXPERIENCE CRITERIA SEARCH SUBSECTION!!!!
                            elif criteria_search == "Experience":

                                #Following lines 7-22 can and will be used for each subprogram
                                root_experience = tkinter.Toplevel()
                                root_experience.title('Completed Education Level Criteria Search')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = root_experience.winfo_screenwidth()
                                screen_height = root_experience.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                root_experience.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(root_experience)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                main_frame =tkinter.LabelFrame(frame_user, text="Experience Criteria Search", font=("Arial", 20), fg="#000080")
                                main_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20) 

                                info_frame = tkinter.Frame(main_frame)
                                info_frame.grid(row=0, column=0)

                                widget_frame= tkinter.Frame(main_frame)
                                widget_frame.grid(row=1, column=0)

                                button_frame = tkinter.Frame(main_frame)
                                button_frame.grid(row=2, column=0)


                                info_label = tkinter.Label(info_frame, text="Please use the menus below to set the experience criteria for you applicants ", font=("Arial", 10), fg="#000080")
                                info_label.grid(row=0, column=0, padx=20, pady=20)

                                intruction_label = tkinter.Label(info_frame, text="I would like to veiw applicants with experience that is.......", font=("Arial", 10), fg="#000080")
                                intruction_label.grid(row=1, column=0, padx=20, pady=20)

                                white_space_label = tkinter.Label(widget_frame, text="")
                                white_space_label.grid(row=2, column=0)

                                symbol_combobox = ttk.Combobox(widget_frame, values=["", "Greater then", "Equal to", "Less then"])
                                symbol_combobox.grid(row=3, column=0, padx=40, pady=40)

                                number_spinbox = ttk.Spinbox(widget_frame, from_=0, to=100)
                                number_spinbox.grid(row=3, column=1, pady=40)


                                #SEARCH BUTTON FUCNTION

                                def search_experience():

                                    global filepath
                                    

                                    #LOOOPS FOR FINDING DATA
                                    

                                    #Defining each of the columns within the spreadsheet to improve the intrinsic documentation
                                    experience_col = pd.read_excel(filepath, usecols='K')

                                    #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                    data_sheet = pd.read_excel(filepath)
                                    end = len(data_sheet. index)
                                    last = end-1
                                    count = 0 
                                    criteria_list = [""]
                                    criteria_list.clear()
                                    global number
                                    number = -1  


                                    #Specific to this loop with the values being checked

                                    symbol = symbol_combobox.get()
                                    number_given = number_spinbox.get()
                                    if number_given:                              #CHECKS IF NUMBER HAS BEEN ENTERED
                                        if symbol:                          #CHECKS IF SYMBOL HAS BEEN ENTERED
                                            root_experience.iconify()
                                            root_experience_file = tkinter.Toplevel()
                                            root_experience_file.title('Experience Search Files')

                                            window_width = 800
                                            window_height = 600

                                            # get the screen dimension
                                            screen_width = root_experience_file.winfo_screenwidth()
                                            screen_height = root_experience_file.winfo_screenheight()

                                            # finding the center point of the screen of the user (will adapt depending on user screen)
                                            center_x = int(screen_width/2 - window_width / 2)
                                            center_y = int(screen_height/2 - window_height / 2)

                                            # set the position of the window to the center of the screen
                                            root_experience_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                            frame_user = tkinter.Frame(root_experience_file)  #Main frame       #Define Widget
                                            frame_user.pack()       #Pack, place or grid widget

                                            info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                            info_frame.grid(row=0, column=0, sticky="news") 

                                            button_frame = tkinter.Frame(frame_user)
                                            button_frame.grid(row=1, column=0)

                                            frame_user.pack()
                                



                                #LOOPING BASED ON BEING GREATER THEN
                                            if symbol == "Greater then":
                                                while count <= last:              
                                                    current = experience_col.iloc[count]
                                                    integer_value = int(current)                  #CHANGING THE VALUE INTO AN INTEGER
                                                    int_number_given = int(number_given)                     #USING THE GLOBAL VALUE FOR THE INPUT NUMBER
                                                    if integer_value > int_number_given:          # IF THE CURRENT EXPERIENCE NUMBER IS GREATER THEN THE INPUTTED NUMBER IT WILL...
                                                        criteria_list.append(count)               # ADD IT TO THE LIST
                                                        count = count+1                           # INCREMENT BY 1
                                                    else:
                                                        count=count+1

                                #LOOPING BASED ON BEING EQUAL TO
                                            elif symbol == "Equal to":
                                                while count <= last:             
                                                    current = experience_col.iloc[count]
                                                    integer_value = int(current)
                                                    int_number_given = int(number_given)
                                                    if integer_value == int_number_given:   
                                                        criteria_list.append(count)
                                                        count = count+1   
                                                    else:
                                                        count=count+1

                                #LOOPING BASED ON BEING LESS THEN
                                            elif symbol == "Less then":
                                                while count <= last:              
                                                    current = experience_col.iloc[count]
                                                    integer_value = int(current)
                                                    int_number_given = int(number_given)
                                                    if integer_value < int_number_given:   #CHECKING IF SELECTED CRITERIA OF WORKA IS IN THE STRING
                                                        criteria_list.append(count)
                                                        count = count+1   
                                                    else:
                                                        count=count+1

                                            listnumber=len(criteria_list)
                                            global truelistnumber
                                            truelistnumber = listnumber-1      #STARTS AT 0 not assummed 1



                                    #NEXT BUTTON FUNCTION
                                            def next():
                                                global number
                                                global truelistnumber
                                                global truelistnumber
                                                if number < truelistnumber:
                                                    number = number+1 
                                                    for widgets in info_frame.winfo_children():
                                                        widgets.destroy()
                                                    current = data_sheet.iloc[criteria_list[number]]
                                                    application_label = tkinter.Label(info_frame, text=current) 
                                                    application_label.grid(row=0, column=0, pady=10, padx=5) 
                                                else: 
                                                    tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                            #BACK BUTTON FUCNTION
                                            def back():
                                                global number
                                                if number > 0:
                                                    number = number-1 
                                                    for widgets in info_frame.winfo_children():
                                                        widgets.destroy()
                                                    current = data_sheet.iloc[criteria_list[number]]
                                                    application_label = tkinter.Label(info_frame, text=current) 
                                                    application_label.grid(row=0, column=0, pady=10, padx=5) 
                                                
                                                else:
                                                    tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                                


                                    #THE DISPLAY FOR THE EXPERIENCE FILES

                                            
                                            button_return_frame = tkinter.Frame(frame_user)
                                            button_return_frame.grid(row=2, column=0) 

                                            return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                        width=30, pady=10)
                                            return_button.grid(row=1, column = 0)
                                            
                                            applicant_label = tkinter.Label(info_frame, text="Please Click next to display application") 
                                            applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                            next_button = tkinter.Button(
                                                button_frame, text="Next", command=next, width=30, pady=10)
                                            next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                            back_button = tkinter.Button(
                                                button_frame, text="Back", command=back, width=30, pady=10)
                                            back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)



                                            root_experience_file.mainloop()


                                        else:
                                            tkinter.messagebox.showwarning(title= "Missing", message= "The symbol/operator is required")      #ERROR MESSAGE FOR NO SYMBOL
                                    else:
                                        tkinter.messagebox.showwarning(title= "Missing", message= "The number for the experience is required.")      #ERROR MESSAGE FOR NO NUMBER


                                search_button = tkinter.Button(button_frame, command=search_experience, width=30, pady=10, text="Search")
                                search_button.grid(row=6, column=0)

                                frame_user.pack()

                                root_experience.mainloop()





                #SEARCHING THE WORK ALLOWANCE CRITERIA SUBSECTION
                            elif criteria_search == "WorkAllowance":
                                

                                #Following lines 7-22 can and will be used for each subprogram
                                root_work = tkinter.Toplevel()
                                root_work.title('Work Allowance Criteria Search')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = root_work.winfo_screenwidth()
                                screen_height = root_work.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                root_work.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(root_work)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                main_frame =tkinter.LabelFrame(frame_user, text="Work Allowance Criteria Search", font=("Arial", 20), fg="#000080")
                                main_frame.grid(row=0, column=0, sticky="news") 

                                info_label = tkinter.Label(main_frame, text="Please select the Work Allowance you require from your applicants; ", font=("Arial", 10), fg="#000080")
                                info_label.grid(row=0, column=0)


                                global work_radio
                                work_radio = tkinter.StringVar()
                                work_radio.set(' ')          #ENSURES THAT IT STARTS WITH NONE SELECTED




                                def search_work():
                                        root_work.iconify()

                                        global work_radio
                                        workA_selected = work_radio.get()       #WorkA stands for Work Allowance but is shorter to make it more applicable
                                        #Following lines 7-22 can and will be used for each subprogram
                                        root_work_file = tkinter.Toplevel()
                                        root_work_file.title('Work Allowance Criteria Search Files')

                                        window_width = 800
                                        window_height = 600

                                        # get the screen dimension
                                        screen_width = root_work_file.winfo_screenwidth()
                                        screen_height = root_work_file.winfo_screenheight()

                                        # finding the center point of the screen of the user (will adapt depending on user screen)
                                        center_x = int(screen_width/2 - window_width / 2)
                                        center_y = int(screen_height/2 - window_height / 2)

                                        # set the position of the window to the center of the screen
                                        root_work_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                        frame_user = tkinter.Frame(root_work_file)  #Main frame       #Define Widget
                                        frame_user.pack()       #Pack, place or grid widget

                                        info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                        info_frame.grid(row=0, column=0, sticky="news") 

                                        button_frame = tkinter.Frame(frame_user)
                                        button_frame.grid(row=1, column=0)

                                        frame_user.pack()

                                        #Setting constant variables
                                        global filepath
                                        
                                        work_col = pd.read_excel(filepath, usecols='G')

                                        #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                        data_sheet = pd.read_excel(filepath)
                                        end = len(data_sheet. index)
                                        last = end-1
                                        count = 0 
                                        criteria_list = [""]
                                        criteria_list.clear()
                                        global number
                                        number = -1


                                        #LOOP TO GET ALL THE DATA INTO THE LIST BASED ON THE CRITERA
                                        while count <= last:              #LOOPING BASED ON THE DATA PROVIDED
                                            current = work_col.iloc[count]
                                            string = str(current)
                                            if workA_selected in string :   #CHECKING IF SELECTED CRITERIA OF WORKA IS IN THE STRING
                                                criteria_list.append(count)
                                                count = count+1   
                                            else:
                                                count=count+1

                                        listnumber=len(criteria_list)
                                        global truelistnumber
                                        truelistnumber = listnumber-1      #STARTS AT 0 not assummed 1

                                        def next():
                                            global number
                                            global truelistnumber
                                            if number < truelistnumber:
                                                number = number+1 
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()
                                                current = data_sheet.iloc[criteria_list[number]]
                                                application_label = tkinter.Label(info_frame, text=current) 
                                                application_label.grid(row=0, column=0, pady=10, padx=5) 
                                            else: 
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                        #BACK BUTTON FUCNTION
                                        def back():
                                            global number
                                            if number > 0:
                                                number = number-1 
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()
                                                current = data_sheet.iloc[criteria_list[number]]
                                                application_label = tkinter.Label(info_frame, text=current) 
                                                application_label.grid(row=0, column=0, pady=10, padx=5) 
                                            
                                            else:
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")



                                        button_return_frame = tkinter.Frame(frame_user)
                                        button_return_frame.grid(row=2, column=0) 
                                            
                                        return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                        width=30, pady=10)
                                        return_button.grid(row=1, column = 0)
                                       
                                        applicant_label = tkinter.Label(info_frame, text="Please Click next to display application") 
                                        applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                        next_button = tkinter.Button(
                                            button_frame, text="Next", command=next, width=30, pady=10)
                                        next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                        back_button = tkinter.Button(
                                            button_frame, text="Back", command=back, width=30, pady=10)
                                        back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)


                                        root_work_file.mainloop()



                                auscitz_button = tkinter.Radiobutton(main_frame, text="Australian Citizen", variable=work_radio , value="Australian Citizen")
                                auscitz_button.grid(row=2, column=0, padx=10)

                                permres_button = tkinter.Radiobutton(main_frame, text="Permanent Resident", variable=work_radio ,  value="Permanent Resident")
                                permres_button.grid(row=3, column=0, padx=10)

                                intstu_button = tkinter.Radiobutton(main_frame, text="International Student", variable=work_radio , value="International Student")
                                intstu_button.grid(row=4, column=0, padx=10)

                                otherwork_button = tkinter.Radiobutton(main_frame, text="Other", variable=work_radio , value="Other")
                                otherwork_button.grid(row=5, column=0, padx=10)

                                for widgets in main_frame.winfo_children():
                                            widgets.configure(padx=20, pady=20)

                                search_button = tkinter.Button(main_frame, command=search_work, width=30, pady=10, text="Search")
                                search_button.grid(row=6, column=0)

                                frame_user.pack()

                                root_work.mainloop()


                            elif criteria_search == "Education":
                                #Following lines 7-22 can and will be used for each subprogram
                                root_education = tkinter.Toplevel()
                                root_education.title('Completed Education Level Criteria Search')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = root_education.winfo_screenwidth()
                                screen_height = root_education.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                root_education.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(root_education)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                main_frame =tkinter.LabelFrame(frame_user, text="Completed Education Level Criteria Search", font=("Arial", 20), fg="#000080")
                                main_frame.grid(row=0, column=0, sticky="news") 

                                info_label = tkinter.Label(main_frame, text="Please select the Education Level which you require your employees to have completed: ", font=("Arial", 10), fg="#000080")
                                info_label.grid(row=0, column=0)

                                global radio_education
                                radio_education = tkinter.StringVar()
                                radio_education.set(' ')          #ENSURES THAT IT STARTS WITH NONE SELECTED

                                def search_education():
                                        root_education.iconify()

                                        global radio_education
                                        education_selected = radio_education.get()       
                                        root_education_file = tkinter.Toplevel()
                                        root_education_file.title('Education Search Files')

                                        window_width = 800
                                        window_height = 600

                                        # get the screen dimension
                                        screen_width = root_education_file.winfo_screenwidth()
                                        screen_height = root_education_file.winfo_screenheight()

                                        # finding the center point of the screen of the user (will adapt depending on user screen)
                                        center_x = int(screen_width/2 - window_width / 2)
                                        center_y = int(screen_height/2 - window_height / 2)

                                        # set the position of the window to the center of the screen
                                        root_education_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                        frame_user = tkinter.Frame(root_education_file)  #Main frame       #Define Widget
                                        frame_user.pack()       #Pack, place or grid widget

                                        info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                        info_frame.grid(row=0, column=0, sticky="news") 

                                        button_frame = tkinter.Frame(frame_user)
                                        button_frame.grid(row=1, column=0)

                                        frame_user.pack()

                                        #Setting constant variables
                                        global filepath
                                        


                                        #Defining each of the columns within the spreadsheet to improve the intrinsic documentation
                                        education_col = pd.read_excel(filepath, usecols='J')

                                        #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                        data_sheet = pd.read_excel(filepath)
                                        end = len(data_sheet. index)
                                        last = end-1
                                        count = 0 
                                        criteria_list = [""]
                                        criteria_list.clear()
                                        global number
                                        number = -1



                                        #LOOP TO GET ALL THE DATA INTO THE LIST BASED ON THE CRITERA
                                        while count <= last:              #LOOPING BASED ON THE DATA PROVIDED
                                            current = education_col.iloc[count]
                                            string = str(current)
                                            if education_selected in string :   #CHECKING IF SELECTED CRITERIA OF EDUCATION IS IN THE STRING
                                                criteria_list.append(count)
                                                count = count+1   
                                            else:
                                                count=count+1

                                        listnumber=len(criteria_list)
                                        global truelistnumber
                                        truelistnumber = listnumber-1      #STARTS AT 0 not assummed 1

                                        def next():
                                            global number
                                            global truelistnumber
                                            global truelistnumber
                                            if number < truelistnumber:
                                                number = number+1 
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()
                                                current = data_sheet.iloc[criteria_list[number]]
                                                application_label = tkinter.Label(info_frame, text=current) 
                                                application_label.grid(row=0, column=0, pady=10, padx=5) 
                                            else: 
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                        #BACK BUTTON FUCNTION
                                        def back():
                                            global number
                                            if number > 0:
                                                number = number-1 
                                                for widgets in info_frame.winfo_children():
                                                    widgets.destroy()
                                                current = data_sheet.iloc[criteria_list[number]]
                                                application_label = tkinter.Label(info_frame, text=current) 
                                                application_label.grid(row=0, column=0, pady=10, padx=5) 
                                            
                                            else:
                                                tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                            

                                        button_return_frame = tkinter.Frame(frame_user)
                                        button_return_frame.grid(row=2, column=0) 
                                            
                                        return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                        width=30, pady=10)
                                        return_button.grid(row=1, column = 0)



                                        applicant_label = tkinter.Label(info_frame, text="Please Click next to display application") 
                                        applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                        next_button = tkinter.Button(
                                            button_frame, text="Next", command=next, width=30, pady=10)
                                        next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                        back_button = tkinter.Button(
                                            button_frame, text="Back", command=back, width=30, pady=10)
                                        back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)



                                        root_education_file.mainloop()


                                manager_button = tkinter.Radiobutton(main_frame, text="High School Leaver", variable=radio_education, value="High School Leaver")
                                manager_button.grid(row=2, column=0, padx=10)

                                marketing_button = tkinter.Radiobutton(main_frame, text="HSC", variable=radio_education,  value="HSC")
                                marketing_button.grid(row=3, column=0, padx=10)

                                accounting_button = tkinter.Radiobutton(main_frame, text="Tafe", variable=radio_education, value="Tafe")
                                accounting_button.grid(row=4, column=0, padx=10)

                                customer_button = tkinter.Radiobutton(main_frame, text="University",variable=radio_education,  value="University")
                                customer_button.grid(row=5, column=0, padx=10)

                                for widgets in main_frame.winfo_children():
                                            widgets.configure(padx=20, pady=20)


                                search_button = tkinter.Button(main_frame, command=search_education, width=30, pady=10, text="Search")
                                search_button.grid(row=6, column=0)

                                frame_user.pack()


                                root_education.mainloop()



                #ALL SEARCH EVERYTHING!!!!!!!!!!!!!!!!!!11111
                            elif criteria_search == "All":
                                
                                #SECTION FOR DISPLAYING ALL FILES  
                                all_file = tkinter.Toplevel()
                                all_file.title('All Search Files')

                                window_width = 800
                                window_height = 600

                                # get the screen dimension
                                screen_width = all_file.winfo_screenwidth()
                                screen_height = all_file.winfo_screenheight()

                                # finding the center point of the screen of the user (will adapt depending on user screen)
                                center_x = int(screen_width/2 - window_width / 2)
                                center_y = int(screen_height/2 - window_height / 2)

                                # set the position of the window to the center of the screen
                                all_file.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                frame_user = tkinter.Frame(all_file)  #Main frame       #Define Widget
                                frame_user.pack()       #Pack, place or grid widget

                                info_frame =tkinter.LabelFrame(frame_user, text="Files", font=("Arial", 20), fg="#000080")
                                info_frame.grid(row=0, column=0, sticky="news") 

                                button_frame = tkinter.Frame(frame_user)
                                button_frame.grid(row=1, column=0)

                                frame_user.pack()

                                #Setting constant variables
                                global filepath
                                


                                #ALL VARAIBLES THAT ARE NEEDED THROUGHOUT MOST OF THE SHEETS
                                data_sheet = pd.read_excel(filepath)
                                end = len(data_sheet. index)
                                last = end-1
                                count = 0 

                                global number
                                number = -1


                                #STARTS AT 0 not assummed 1

                                def next():
                                    global number
                                    if number < last:
                                        number = number+1 
                                        for widgets in info_frame.winfo_children():
                                            widgets.destroy()
                                        current = data_sheet.iloc[number]
                                        application_label = tkinter.Label(info_frame, text=current) 
                                        application_label.grid(row=0, column=0, pady=10, padx=5) 
                                    else: 
                                        tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                #BACK BUTTON FUCNTION
                                def back():
                                    global number
                                    if number > 0:
                                        number = number-1 
                                        for widgets in info_frame.winfo_children():
                                            widgets.destroy()
                                        current = data_sheet.iloc[number]
                                        application_label = tkinter.Label(info_frame, text=current) 
                                        application_label.grid(row=0, column=0, pady=10, padx=5) 
                                    
                                    else:
                                        tkinter.messagebox.showwarning(title= "Error", message= "No more applications to veiw")

                                    


                                button_return_frame = tkinter.Frame(frame_user)
                                button_return_frame.grid(row=2, column=0) 
                                    
                                return_button = tkinter.Button(button_return_frame, command=mainmenu, text="Return To Main Menu",
                                                                width=30, pady=10)
                                return_button.grid(row=1, column = 0)

                                applicant_label = tkinter.Label(info_frame, text="Please Click NEXT to display application") 
                                applicant_label.grid(row=0, column=0, pady=10, padx=5)  

                                next_button = tkinter.Button(
                                    button_frame, text="Next", command=next, width=30, pady=10)
                                next_button.grid(row=0, column=2, columnspan=2, pady=40, padx=20 )

                                back_button = tkinter.Button(
                                    button_frame, text="Back", command=back, width=30, pady=10)
                                back_button.grid(row=0, column=0, columnspan=2, pady=40, padx=20)

                                all_file.mainloop()
                        


                        else:
                            tkinter.messagebox.showwarning(title= "Error", message= "No Criteria Selected")
                
                


                job_button = tkinter.Radiobutton(main_frame, text="Selected Job", variable=answer_criteria, value="Job")
                job_button.grid(row=2, column=0, padx=10)

                pay_button = tkinter.Radiobutton(main_frame, text="Hourly Pay Rate", variable=answer_criteria, value="Pay")
                pay_button.grid(row=3, column=0, padx=10)

                experience_button = tkinter.Radiobutton(main_frame, text="Applicant Experience", variable=answer_criteria, value="Experience")
                experience_button.grid(row=4, column=0, padx=10)

                WorkAllowance_button = tkinter.Radiobutton(main_frame, text="Applicant Work Allowance", variable=answer_criteria, value="WorkAllowance")
                WorkAllowance_button.grid(row=5, column=0, padx=10)

                education_button = tkinter.Radiobutton(main_frame, text="Applicant Education Level", variable=answer_criteria, value="Education")
                education_button.grid(row=6, column=0, padx=10)

                All_button = tkinter.Radiobutton(main_frame, text="Veiw All", variable=answer_criteria, value="All")
                All_button.grid(row=7, column=0, padx=10)

        
                for widgets in main_frame.winfo_children():
                            widgets.configure(padx=20, pady=20)


                search_button = tkinter.Button(main_frame, command=search_criteria_1, width=30, pady=10, text="Search")
                search_button.grid(row=8, column=0)


                framec_user.pack()

                root_criteria.mainloop()


            else:
                messagebox.showerror(title="Error", message="Invalid Username or Password")



        # Username and Password entry sections
        login_label = tkinter.Label(frame_login, text="Login", font=("Arial", 20), fg="#000080")
        username_label = tkinter.Label(frame_login, text="Username: ", font=("Arial", 15), fg="#000080")
        username_entry = tkinter.Entry(frame_login, width=30)
        password_entry = tkinter.Entry(frame_login, show="*", width=30)
        password_label = tkinter.Label(frame_login, text="Password: ", font=("Arial", 15), fg="#000080")
        login_button = tkinter.Button( frame_login, text="Login", command=login, width=30, pady=10)

        # Placing widgets on the screen
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=40)

        frame.pack()

        window_login.mainloop()


#Apply subsection as set from pressing the button on the main screen previously
    def apply():
        window_main.iconify() #Deleting and removing the previous page
        def next_page():
            desired_job = apply_combobox.get()
            root_3.iconify()


            def next_data():      #Using Data Validation techniques      #Define for entering data for application page 1
                    firstname = first_name_entry.get()     #getting all the variables that were selected
                    lastname = last_name_entry.get()
                    work_allowance = work_allowance_combobox.get()
                    email = email_entry.get()

                    if firstname and lastname and email and work_allowance:      #checks if they have entered into the first name and last name boxes before proceeding

                        title = title_combobox.get()
                        age = age_spinbox.get()
                        englishfluency = fluency_combobox.get()
                        phonenumber = phone_entry.get()
                        

                        root_1.iconify()   


                        #START OF APPLICATION PAGE 2
                        def enter_data():      #Using Data Validation techniques     #only starts only the save button has been selected
                                education = education_combobox.get()

                                if education:      #checks if they have entered into the first name and last name boxes before proceeding

                                        #getting all the variables that have been entered
                                    experience = experience_spinbox.get()
                                    pay = pay_spinbox.get()
                                    referee_1_name = reference_name_1_entry.get()
                                    referee_1_relation = reference_relation_1_entry.get()
                                    referee_1_email = reference_contact_email_1_entry.get()
                                    referee_1_number = reference_contact_number_1_entry.get()

                                    referee_2_name = reference_name_2_entry.get()
                                    referee_2_relation = reference_relation_2_entry.get()
                                    referee_2_email = reference_contact_email_2_entry.get()
                                    referee_2_number = reference_contact_number_2_entry.get()

                                    global filepath

                        
                                    workbook = openpyxl.load_workbook(filepath)   #opening the excel spreadsheet
                                    sheet = workbook.active     #activating the spreadsheet
                                    #entering all the data into the spreadsheet in the order stated which connected to the columns
                                    sheet.append([desired_job, firstname, lastname, title, age, englishfluency, work_allowance,
                                                    phonenumber, email, education, experience, pay,
                                                    referee_1_name, referee_1_relation, referee_1_number,
                                                    referee_1_email, 
                                                    referee_2_name, referee_2_relation, referee_2_number,
                                                    referee_2_email])
                                    workbook.save(filepath)    #saving the stored data
 

                                    root_2.iconify()

                                    #Following lines 7-22 can and will be used for each subprogram
                                    root = tkinter.Toplevel()
                                    root.title('Thank You!')

                                    window_width = 800
                                    window_height = 600

                                    # get the screen dimension
                                    screen_width = root.winfo_screenwidth()
                                    screen_height = root.winfo_screenheight()

                                    # finding the center point of the screen of the user (will adapt depending on user screen)
                                    center_x = int(screen_width/2 - window_width / 2)
                                    center_y = int(screen_height/2 - window_height / 2)

                                    # set the position of the window to the center of the screen
                                    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                                    #Start of all the code applicable to the Application page 1 of the program
                                    frame = tkinter.LabelFrame(root, text="Thank you", font=("Arial", 20), fg="#0062cc")  #Main frame       #Define Widget
                                    frame.pack()       #Pack, place or grid widget

                                                #ALL FRAMES FOR THE JOBS SECTION    

                                    #FRAME AND INFORMATION FOR THE THANKYOU
                                    thankyou_frame=tkinter.Frame(frame)
                                    thankyou_frame.grid(row=0, column=0, padx=20, pady=20) 

                                    thank_you_text_1 = tkinter.Label(thankyou_frame, text='Thank You for you Application', font=("Arial", 15), fg="#0062cc")
                                    thank_you_text_1.grid(row=0, column=0, pady=20)

                                    thank_you_text_2 = tkinter.Label(thankyou_frame, text='Your application has been sent ot the small buissness owner', font=("Arial", 12), fg="#0062cc")
                                    thank_you_text_2.grid(row=1, column=0, pady=10)

                                    thank_you_text_3 = tkinter.Label(thankyou_frame, text='For any further questions about the status of your application please contact the number below.', font=("Arial", 10), fg="#0062cc")
                                    thank_you_text_3.grid(row=2, column=0, pady=10)

                                    thank_you_text_4 = tkinter.Label(thankyou_frame, text='Please use the contact details that are listed below ' , font=("Arial", 10), fg="#0062cc")
                                    thank_you_text_4.grid(row=4, column=0, pady=10)

                                    thank_you_text_5 = tkinter.Label(thankyou_frame, text='We do request paitence as applications will take 5-10 buissness days to be repsonded to. ' , font=("Arial", 10), fg="#0062cc")
                                    thank_you_text_5.grid(row=3, column=0, pady=10)


                                    thank_you_text_6 = tkinter.Label(thankyou_frame, text='email: job_opportunites@smallbuiness.com', font=("Arial", 10), fg="#0062cc")
                                    thank_you_text_6.grid(row=5, column=0, pady=10)

                                    thank_you_text_7 = tkinter.Label(thankyou_frame, text='phone: 0462 235 753', font=("Arial", 10), fg="#0062cc")
                                    thank_you_text_7.grid(row=6, column=0, pady=10)

                                    def quit():    #if they press the quit button in the end it will clsoe all the previous pages without saving
                                        root_3.destroy()
                                        root_2.destroy()
                                        root_1.destroy()
                                        root.destroy()

                                    #ENDING with button and closing window
                                    button_final = tkinter.Button(frame, text="Quit", width=60, command=quit)#when button is clicked execute the command enter_data
                                    button_final.grid(row=1, column=0, sticky="news", padx=20, pady=50)

                                    return_button = tkinter.Button(frame, command=mainmenu, text="Return to Main Menu",
                                                            width=60, pady=10)
                                    return_button.grid(row=2, column = 0)

                                    root.mainloop() #loops continues until closed

                            


                            

                        #Following lines 7-22 can and will be used for each subprogram
                        root_2 = tkinter.Toplevel()
                        root_2.title('Application Page 2')       #2nd application page

                        window_width = 800
                        window_height = 600

                        # get the screen dimension
                        screen_width = root_2.winfo_screenwidth()
                        screen_height = root_2.winfo_screenheight()

                        # finding the center point of the screen of the user (will adapt depending on user screen)
                        center_x = int(screen_width/2 - window_width / 2)
                        center_y = int(screen_height/2 - window_height / 2)

                        # set the position of the window to the center of the screen
                        root_2.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                        #Start of all the code applicable to the Application page 1 of the program
                        frame = tkinter.Frame(root_2)  #Main frame       #Define Widget
                        frame.pack()       #Pack, place or grid widget
                        button_frame = tkinter.Frame(frame)
                        button_frame.grid(row=3, column=0, padx=20, pady=10)


                        #User information label
                        education_frame =tkinter.LabelFrame(frame, text="Education", font=("Arial", 15), fg="#0062cc")
                        education_frame.grid(row=0, column=0, padx=20, pady=10)  #location of label + the padding around the label

                        #level  of education from particpants 
                        education_level_label = tkinter.Label(education_frame, text="Highest level of offical education completed *")
                        education_level_label.grid(row=0, column=0)
                        education_combobox = ttk.Combobox(education_frame, values=["", "High School Leaver", "HSC", "Tafe", "University"])
                        education_combobox.grid(row=1, column=0)

                        #level of experience from the applicants
                        experience_level_label = tkinter.Label(education_frame, text="Years of applicable experience to the role")
                        experience_level_label.grid(row=0, column=1)
                        experience_spinbox = ttk.Spinbox(education_frame, from_=0, to=100)
                        experience_spinbox.grid(row=1, column=1)

                        #Pay expectations from the applicants, labels and entry boxes
                        pay_label = tkinter.Label(education_frame, text="Pay expectation per hour ($/hr)")
                        pay_label.grid(row=2, column=1)
                        pay_spinbox = ttk.Spinbox(education_frame, from_=0, to=100)
                        pay_spinbox.insert(0, "$/hr")      #Temporary Text for user experience and help
                        pay_spinbox.grid(row=3, column=1)

                        #Setting the padding for all the widgets inside the user information frame
                        for widget in education_frame.winfo_children():
                            widget.grid_configure(padx=20, pady=10)



                        #Reference label FOR REFERENCE 1
                        reference_info_frame_1 =tkinter.LabelFrame(frame, text="Reference 1", font=("Arial", 15), fg="#0062cc")
                        reference_info_frame_1.grid(row=1, column=0, padx=20, pady=10)  #location of label + the padding around the label

                        #Refernce 1 labels and entry boxes 
                        reference_name_1_label = tkinter.Label(reference_info_frame_1, text="Reference Name")
                        reference_name_1_label.grid(row=0, column=0)
                        reference_name_1_entry =tkinter.Entry(reference_info_frame_1)
                        reference_name_1_entry.grid(row=0, column=1, sticky="news")

                        reference_relation_1_label = tkinter.Label(reference_info_frame_1, text="Relation")
                        reference_relation_1_label.grid(row=0, column=2)
                        reference_relation_1_entry =tkinter.Entry(reference_info_frame_1)
                        reference_relation_1_entry.grid(row=0, column=3, sticky="news")

                        reference_contact_number_1_label = tkinter.Label(reference_info_frame_1, text="Reference Contact Number")
                        reference_contact_number_1_label.grid(row=1, column=0)
                        reference_contact_number_1_entry =tkinter.Entry(reference_info_frame_1)
                        reference_contact_number_1_entry.grid(row=1, column=1, sticky="news")

                        reference_contact_email_1_label = tkinter.Label(reference_info_frame_1, text="Reference Contact Email")
                        reference_contact_email_1_label.grid(row=1, column=2)
                        reference_contact_email_1_entry =tkinter.Entry(reference_info_frame_1)
                        reference_contact_email_1_entry.grid(row=1, column=3, sticky="news")


                        #Specifcation of widgets within the reference 1 frame
                        for widget in reference_info_frame_1.winfo_children():     
                                widget.grid_configure(padx= 20, pady=10)


                        #Reference label FOR REFERENCE 2
                        reference_info_frame_2=tkinter.LabelFrame(frame, text="Reference 2", font=("Arial", 15), fg="#0062cc")
                        reference_info_frame_2.grid(row=2, column=0, padx=20, pady=10)  #location of label + the padding around the label

                        #Refernce 2 labels and entry boxes 
                        reference_name_2_label = tkinter.Label(reference_info_frame_2, text="Reference Name")
                        reference_name_2_label.grid(row=0, column=0)
                        reference_name_2_entry =tkinter.Entry(reference_info_frame_2)
                        reference_name_2_entry.grid(row=0, column=1, sticky="news")

                        reference_relation_2_label = tkinter.Label(reference_info_frame_2, text="Relation")
                        reference_relation_2_label.grid(row=0, column=2)
                        reference_relation_2_entry =tkinter.Entry(reference_info_frame_2)
                        reference_relation_2_entry.grid(row=0, column=3, sticky="news")

                        reference_contact_number_2_label = tkinter.Label(reference_info_frame_2, text="Reference Contact Number")
                        reference_contact_number_2_label.grid(row=1, column=0)
                        reference_contact_number_2_entry =tkinter.Entry(reference_info_frame_2)
                        reference_contact_number_2_entry.grid(row=1, column=1, sticky="news")

                        reference_contact_email_2_label = tkinter.Label(reference_info_frame_2, text="Reference Contact Email")
                        reference_contact_email_2_label.grid(row=1, column=2)
                        reference_contact_email_2_entry =tkinter.Entry(reference_info_frame_2)
                        reference_contact_email_2_entry.grid(row=1, column=3, sticky="news")


                        #Specifcation of widgets within the reference 1 frame
                        for widget in reference_info_frame_2.winfo_children():     
                                widget.grid_configure(padx= 20, pady=10)




                        button = tkinter.Button(button_frame, text="Save", command=enter_data)#when button is clicked execute the command enter_data
                        button.grid(row =0, column=0, padx=20, pady=20, sticky="news")

                        cancel_button = tkinter.Button(button_frame, command=mainmenu, text="Return", width=30, fg="#FF0000")
                        cancel_button.grid(row=1, column = 0, padx = 20, sticky="news")


                        root_2.mainloop() 


                    else:
                        tkinter.messagebox.showwarning(title= "Error", message= "First name, Last name, Email and Work allowance are required") 


                    #START OF APPLICATION PAGE 1

            #Following lines 7-22 can and will be used for each subprogram
            root_1 = tkinter.Toplevel()
            root_1.title('Application Page 1')

            window_width = 800
            window_height = 600

            # get the screen dimension
            screen_width = root_1.winfo_screenwidth()
            screen_height = root_1.winfo_screenheight()

            # finding the center point of the screen of the user (will adapt depending on user screen)
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            # set the position of the window to the center of the screen
            root_1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

            #Start of all the code applicable to the Application page 1 of the program
            frame = tkinter.Frame(root_1)  #Main frame       #Define Widget
            frame.pack()       #Pack, place or grid widget

            #User information label
            user_info_frame =tkinter.LabelFrame(frame, text="User Information", font=("Arial", 15), fg="#0062cc")
            user_info_frame.grid(row=0, column=0, padx=20, pady=10)  #location of label + the padding around the label

            #title of user combo box
            title_label = tkinter.Label(user_info_frame, text="Title")
            title_label.grid(row=0, column=0)
            title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
            title_combobox.grid(row=1, column=0)

            #Entry Label 
            first_name_label =tkinter.Label(user_info_frame, text="First Name *")
            first_name_label.grid(row=0, column=1)
            last_name_label =tkinter.Label(user_info_frame, text="Last Name *")
            last_name_label.grid(row=0, column=2)

            #Entry boxes
            first_name_entry =tkinter.Entry(user_info_frame)
            first_name_entry.grid(row=1, column=1)
            last_name_entry = tkinter.Entry(user_info_frame)
            last_name_entry.grid(row=1, column=2)

            #Age of user scroll box
            age_label = tkinter.Label(user_info_frame, text="Age")
            age_label.grid(row=2, column = 0)
            age_spinbox = tkinter.Spinbox(user_info_frame, from_=14, to=110)
            age_spinbox.grid(row=3, column=0)

            #Setting the padding for all the widgets inside the user information frame
            for widget in user_info_frame.winfo_children():
                widget.grid_configure(padx=20, pady=10)

            #FOVERARCHING WORK FRAME
            work_frame = tkinter.LabelFrame(frame)
            work_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)   #sticky in grid functions expands it in certain directions, news is norths east west and south. In all directions

            work_allowance_label = tkinter.Label(work_frame, text="Work Allowance *")
            work_allowance_label.grid(row=0, column=0)

            work_allowance_combobox = ttk.Combobox(work_frame, values=["", "Australian Citizen", "Permanent Resident", "International Student", "Other"])
            work_allowance_combobox.grid(row=1, column=0)

                #english fluency labels
            fluency_label = tkinter.Label(work_frame, text="English Fluency")
            fluency_label.grid(row=0, column=1)
            fluency_combobox = ttk.Combobox(work_frame, values=["", "Fluent", "Basic", "Other"])
            fluency_combobox.grid(row=1, column=1)

            for widget in work_frame.winfo_children():          #adds universal apdding to all the widgets in the work frame 
                widget.grid_configure(padx= 20, pady=20)

            contact_frame=tkinter.LabelFrame(frame, text="Contacts", font=("Arial", 10), fg="#0062cc")
            contact_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

            #Contact information labels and locations
            phone_label =tkinter.Label(contact_frame, text="Contact Number")
            phone_label.grid(row=0, column=1)
            email_label =tkinter.Label(contact_frame, text="Email *")
            email_label.grid(row=0, column=2)

            #CONTACT INFORMATION boxes
            phone_entry =tkinter.Entry(contact_frame)
            phone_entry.grid(row=1, column=1)
            email_entry = tkinter.Entry(contact_frame)
            email_entry.grid(row=1, column=2)

            for widget in contact_frame.winfo_children():          #adds universal apdding to all the widgets in the course frame 
                widget.grid_configure(padx= 20, pady=10)

            button = tkinter.Button(frame, text="Continue", command=next_data)#when button is clicked execute the command enter_data
            button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

            cancel_button = tkinter.Button(frame, command=mainmenu, text="Cancel", width=30, fg="#FF0000")
            cancel_button.grid(row=4, column = 0, padx=20)

            root_1.mainloop() #loops continues until closed





        #FRAMES AND WINDOW FOR JOBS SCREEN
        #Following lines 7-22 can and will be used for each subprogram
        root_3 = tkinter.Toplevel()
        root_3.title('Job Options')

        window_width = 800
        window_height = 600

        # get the screen dimension
        screen_width = root_3.winfo_screenwidth()
        screen_height = root_3.winfo_screenheight()

        # finding the center point of the screen of the user (will adapt depending on user screen)
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        root_3.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #Start of all the code applicable to the Application page 1 of the program
        frame = tkinter.LabelFrame(root_3, text="Job Opportunities", font=("Arial", 20), fg="#0062cc")  #Main frame       #Define Widget
        frame.pack()       #Pack, place or grid widget

        continue_frame=tkinter.Frame(root_3)
        continue_frame.pack()

                    #ALL FRAMES FOR THE JOBS SECTION    

        #Frame for Job option 1
        job1_frame=tkinter.LabelFrame(frame, text="Job 1", font=("Arial", 15), fg="#0062cc")
        job1_frame.grid(row=0, column=0, padx=20, pady=20) 

        #Frame for Job option 2
        job2_frame=tkinter.LabelFrame(frame, text="Job 2", font=("Arial", 15), fg="#0062cc")
        job2_frame.grid(row=0, column=1, padx=20, pady=20) 

        #Frame for Job Option 3
        job3_frame=tkinter.LabelFrame(frame, text="Job 3", font=("Arial", 15), fg="#0062cc")
        job3_frame.grid(row=1, column=0, padx=20, pady=20) 

        #Frame for Job Option 3
        job4_frame=tkinter.LabelFrame(frame, text="Job 4", font=("Arial", 15), fg="#0062cc")
        job4_frame.grid(row=1, column=1, padx=20, pady=20) 

        #Frame for the Apply buttons
        apply_frame=tkinter.Frame(frame)
        apply_frame.grid(row=3, column=0, pady=20)

        #Apply frame for the combobox
        apply_frame_selection = tkinter.Frame(frame)
        apply_frame_selection.grid(row=3, column=1, pady=20)

        #INFORMATION FOR JOB 1
        job1_title =tkinter.Label(job1_frame, text="Job Title:       Customer Service Representative")
        job1_title.grid(row=0, column=0)
        job1_experience=tkinter.Label(job1_frame, text="Desired Experience for the role:       2 years")
        job1_experience.grid(row=1, column=0)

        job1_description_title=tkinter.Label(job1_frame, text="Description of Role: ")
        job1_description_title.grid(row=2, column=0)

        job1_description_title_line1=tkinter.Label(job1_frame, text="   A Customer Service Representative works with clients   ")
        job1_description_title_line1.grid(row=3, column=0)
        job1_description_title_line2=tkinter.Label(job1_frame, text="    who have complaints, orders, or require information a   ")
        job1_description_title_line2.grid(row=4, column=0)
        job1_description_title_line3=tkinter.Label(job1_frame, text="    about products/services purchased from the organization   ")
        job1_description_title_line3.grid(row=5, column=0)

        #INFORMATION FOR JOB 2
        job2_title =tkinter.Label(job2_frame, text="Job Title:                 Manager")
        job2_title.grid(row=0, column=0)  
        job2_experience=tkinter.Label(job2_frame, text="Desired Experience for the role:       4 years")
        job2_experience.grid(row=1, column=0)

        job2_description_title=tkinter.Label(job2_frame, text="Description of Role: ")
        job2_description_title.grid(row=2, column=0)

        job2_description_title_line1=tkinter.Label(job2_frame, text="Accomplishes department objectives by managing staff; ")
        job2_description_title_line1.grid(row=3, column=0)
        job2_description_title_line2=tkinter.Label(job2_frame, text=" planning and evaluating department activities. Maintains ")
        job2_description_title_line2.grid(row=4, column=0)
        job2_description_title_line3=tkinter.Label(job2_frame, text=" staff by recruiting, selecting, orienting, and training employees.")
        job2_description_title_line3.grid(row=5, column=0)

        #INFORMATION FOR JOB 3
        job3_title =tkinter.Label(job3_frame, text="Job Title:                 Marketing Management")
        job3_title.grid(row=0, column=0)  
        job3_experience=tkinter.Label(job3_frame, text="Desired Experience for the role:       3 years")
        job3_experience.grid(row=1, column=0)

        job3_description_title=tkinter.Label(job3_frame, text="Description of Role: ")
        job3_description_title.grid(row=2, column=0)

        job3_description_title_line1=tkinter.Label(job3_frame, text="   Marketing Managers are responsible for developing,   ")
        job3_description_title_line1.grid(row=3, column=0)
        job3_description_title_line2=tkinter.Label(job3_frame, text="   implementing and executing strategic marketing plans for ")
        job3_description_title_line2.grid(row=4, column=0)
        job3_description_title_line3=tkinter.Label(job3_frame, text="   an organisation, to attract new or returning customers.  ")
        job3_description_title_line3.grid(row=5, column=0)

        #INFORMATION FOR JOB 4
        job4_title =tkinter.Label(job4_frame, text="Job Title:               Accounting Internship")
        job4_title.grid(row=0, column=0)  
        job4_experience=tkinter.Label(job4_frame, text="Desired Experience for the role:       0 years")
        job4_experience.grid(row=1, column=0)

        job4_description_title=tkinter.Label(job4_frame, text="Description of Role: ")
        job4_description_title.grid(row=2, column=0)

        job4_description_title_line1=tkinter.Label(job4_frame, text="Organize a financial filing system that is accessible.")
        job4_description_title_line1.grid(row=3, column=0)
        job4_description_title_line2=tkinter.Label(job4_frame, text=" Prepare accounting reports to be presented to.")
        job4_description_title_line2.grid(row=4, column=0)
        job4_description_title_line3=tkinter.Label(job4_frame, text="  management, and tracking payments for tax preparation ")
        job4_description_title_line3.grid(row=5, column=0)

        #APPLY LABELS AND SCROLL OPTIONS
        apply_label = tkinter.Label(apply_frame, text="What job would you like to apply for?", font=("Arial", 15), fg="#0062cc")
        apply_label.grid(row=0, column=0)

        apply_combobox = ttk.Combobox(apply_frame_selection, values=["Customer Service Representative", "Manager", 
                                                                    "Marketing Management", "Accounting Internship", "All" ], width=40)
        apply_combobox.grid(row=0, column = 1)

        #ENDING with button and closing window
        button = tkinter.Button(continue_frame, text="Continue", width=70, command=next_page)#when button is clicked execute the command enter_data
        button.grid(row=4, column=0, sticky="news", padx=20, pady=20)
        cancel_button = tkinter.Button(continue_frame, command=mainmenu, text="Return", width=30, fg="#FF0000",
                                        )
        cancel_button.grid(row=5, column = 0)
        
        root_3.mainloop() #loops continues until closed
                        
                        
                            #   END OF APPLY SUBPROGRAM












                                        #HELP SUBPROGRAM BEGINS HERE
    def help():
        window_main.iconify()
                #HELP SUBPROGRAM BEGINS HERE
        #Following lines 7-22 can and will be used for each subprogram
        root_help = tkinter.Toplevel()
        root_help.title('Help')

        window_width = 800
        window_height = 600

        # get the screen dimension
        screen_width = root_help.winfo_screenwidth()
        screen_height = root_help.winfo_screenheight()

        # finding the center point of the screen of the user (will adapt depending on user screen)
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        root_help.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



        frame_help = tkinter.Frame(root_help)  #Main frame       #Define Widget
        frame_help.pack()       #Pack, place or grid widget

        help_frame =tkinter.LabelFrame(frame_help, text="Help", font=("Arial", 20), fg="#000080")
        help_frame.grid(row=0, column=0, sticky="news") 

        #Employer Label and frame
        employer_help_frame = tkinter.LabelFrame(help_frame, text="Employer Help",  font=("Arial", 15), fg="#0062cc")  #The title for the emplyer
        employer_help_frame.grid(row=0, column=0, sticky="news", pady=20, padx=20)

        #Apply Label and frame
        apply_help_frame = tkinter.LabelFrame(help_frame,text="How to Apply", font=("Arial", 15), fg="#0062cc")    #Title for the applicants 
        apply_help_frame.grid(row=1, column=0, sticky="news", pady=20, padx=20)

            #frequently asked questions labels and frames
        questions_help_frame = tkinter.LabelFrame(help_frame,text="Frequently Asked Questions", font=("Arial", 15), fg="#0062cc")    #Title for the applicants 
        questions_help_frame.grid(row=2, column=0, sticky="news", pady=20, padx=20)

            #buttons have there own frame as not to mess with the formatting
        button_help_frame = tkinter.Frame(help_frame)
        button_help_frame.grid(row=3, column=0, sticky="news", pady=20, padx=20)



        #Information within the employer frame
                #first states the text that will be displayed and the following line the location of the screen
        employer_help_info1 = tkinter.Label(employer_help_frame, text="This portal is for the employer only, please do not attempt to enter unless it's you." , font=("Arial", 10))        #This is the text for the emplyer when they click the help button
        employer_help_info1.grid(row=1, column=0, sticky="news")
        employer_help_info2 = tkinter.Label(employer_help_frame, text="Type in Username and Password", font=("Arial", 10))        #This is the text for the emplyer when they click the help button
        employer_help_info2.grid(row=2, column=0, sticky="news")
        employer_help_info3 = tkinter.Label(employer_help_frame, text="To search by desired criteria of applicants go through the employer portal pages", font=("Arial", 10))        #This is the text for the emplyer when they click the help button
        employer_help_info3.grid(row=3, column=0, sticky="news")
        employer_help_info4 = tkinter.Label(employer_help_frame, text="Fill in all sections the are presented on the pages", font=("Arial", 10))        #This is the text for the emplyer when they click the help button
        employer_help_info4.grid(row=4, column=0, sticky="news")

        #Information within the apply frame
                #first states the text that will be displayed and the following line the location of the screen
        apply_help_info1 = tkinter.Label(apply_help_frame, text="Please complete all required sections", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info1.grid(row=0, column=0)
        apply_help_info2 = tkinter.Label(apply_help_frame, text="Required section are indicated by a *", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info2.grid(row=1, column=0)
        apply_help_info3 = tkinter.Label(apply_help_frame, text="To use drop down boxes select one of the options below", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info3.grid(row=2, column=0)
        apply_help_info4 = tkinter.Label(apply_help_frame, text="Use the arrows on the right of scroll boxes to change the value", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info4.grid(row=3, column=0)


        #Information within the frequently asked question page
                #first states the text that will be displayed and the following line the location of the screen
        apply_help_info1 = tkinter.Label(questions_help_frame, text="How do I return to the main menu?", font=("Arial", 11))  #This is the text for the applicants help part
        apply_help_info1.grid(row=0, column=0, sticky="news")
        apply_help_info2 = tkinter.Label(questions_help_frame, text="Use the cancel or return to main menu buttons", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info2.grid(row=1, column=0, sticky="news")
        apply_help_info3 = tkinter.Label(questions_help_frame, text="How do I quit the application?", font=("Arial", 11))  #This is the text for the applicants help part
        apply_help_info3.grid(row=2, column=0, sticky="news")
        apply_help_info4 = tkinter.Label(questions_help_frame, text="Return to the main menu using the cancel or return buttons", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info4.grid(row=3, column=0, sticky="news")
        apply_help_info5 = tkinter.Label(questions_help_frame, text="and press the 'Quit' button or the close all open tabs", font=("Arial", 10))  #This is the text for the applicants help part
        apply_help_info5.grid(row=4, column=0, sticky="news")

        help_button = tkinter.Button(button_help_frame, text="Return to Main Menu", width=30, command=mainmenu)
        help_button.grid(row=0, column=0, sticky="news")
         
        for widget in button_help_frame.winfo_children():
            widget.grid_configure(padx=280)


        for widget in apply_help_frame.winfo_children():
            widget.grid_configure(padx=130)

        for widget in employer_help_frame.winfo_children():
            widget.grid_configure(padx=130)

        for widget in questions_help_frame.winfo_children():
            widget.grid_configure(padx=130)


        frame_help.pack()

        root_help.mainloop()


#ALL BUTTON FOR WITHIN THE MAIN MENU
#EACH IS SET WITHIN THE WELCOME FRAME AND HAVE IDENTICAL ALLIGNMENT ON THE SCREEN
#THEY ARE ALSO COLOURED TO PROVIDE A COLOUR SCHEME THAT IS CONSTANT
    employer_button = tkinter.Button(welcome_frame, text="Employer", height=3, width=40, command=employer, bg="#000080", fg="#FFFFFF")
    employer_button.grid(row=1, column=2, sticky="news")

    apply_button = tkinter.Button(welcome_frame, text="Apply", height=3, width=40, command=apply, bg="#000080", fg="#FFFFFF")
    apply_button.grid(row=2, column=2, sticky="news")

    help_button = tkinter.Button(welcome_frame, text="Help", height=3, width=40, command=help, bg="#000080", fg="#FFFFFF")
    help_button.grid(row=3, column=2, sticky="news")

    quit_button = tkinter.Button(welcome_frame, text="Quit", height=3, width=40, command=quit, bg="#000080", fg="#FFFFFF")
    quit_button.grid(row=4, column=2, sticky="news")

#DEFINING THE PADDING FOR ALL THE WIDGETS IN THE WELCOME FRAME
#THESE ARE THE BUTTON ABOVE FOR REFERENCE
    for widget in welcome_frame.winfo_children():
        widget.grid_configure(padx=200, pady=30)

    frame.pack()

    window_main.mainloop()     #the main loop keeps the window open until the close button is pressed.

#STARTS THE MAINMENU PROGRAM
mainmenu()

