from talaba import *
from uuid import uuid4

print("\n======================== Students Info System ========================\n")

print("Amallarni bajarish uchun uning to'g'risidagi harflardan foydalaning")

manual="""Student_add--:>a
Student_remove--:>r
Student_find--:>f
Display_all--:>d_l
Exit--:>e"""
change=None


students={}





slug=0             #full name bi xil bosa ajratish uchun








while change!='e':
    print(manual)
    change=input("Qanday amal bajarmoqchisiz?  :")
    print('\n')
    if change=='a':
        full_name=input("Full Name-")
        nationalitty = input("Nationalitty-")
        gender = input("Gender-")
        faculty = input("Faculty-")
        admission_year = int(input("Admission Year-"))
        
        student_id=f'{"".join(full_name.split())}{str(slug)}'
        slug+=1
        obj=Person(student_id, full_name, nationalitty, gender, faculty, admission_year)
        data=[obj.get_full_name(),obj.get_nationalitty(),obj.get_faculty(),obj.get_faculty(),obj.get_admission_year()]
        
        
        if int(input("Undergraduate--:>1   or  Postgraduate--:>2    -->"))==1:
            residential_hall = input("Residential Hall-")
            
            obju=Undergraduate(student_id, full_name, nationalitty, gender, faculty, admission_year,residential_hall)
            data.append(obju.get_residential_hall())
            
            students[obj.get_student_id()]=data
            
        else:
         
            supervisor_name = input("Supervisor Name-")
            research_topic = input("Research Topic-")
            
            objp=Postgraduate(student_id, full_name, nationalitty, gender, faculty, admission_year, supervisor_name, research_topic)
            data.append(objp.get_supervisor_name()),data.append(objp.get_research_topic())
            
            students[student_id]=data
        
    
    elif change=='r':
        id=input("ID--:>")
        if id in students:
            print(f"{(students[id])[0]} bazadan  o'chirib yuborildi\n")
            del students[id]
        
        else:
            print('Bunday ID li shaxs topilmadi\n')
        
    
    elif change=='f':
    
        id=input("ID--:>")
        if id in students:
            print(f"Shaxs {(students[id])[0]} topildi \n Uning malumotlari: {(students[id])[1:]}\n")
            
        
        else:
            print('Bunday ID li shaxs topilmadi\n')
        
    elif change=='d_l':
        shunchaki=f"{15*' '}id{15*' '}|{12*' '}fullname{12*' '}|"
        shunchaki+=f" nationalitty | gender |{13*' '}faculty{12*' '}|"
        shunchaki+=f"admission year|{8*' '}residential_hall{8*' '}|"
        shunchaki+=f"{9*' '}supervisor name{8*' '}|{9*' '}research topic{9*' '}|"
        print(shunchaki)
        
        
        for idx,data in students.items():
            datas=idx
            lenth=32-len(idx)
            datas+=f"{lenth*' '}|"
            lenths=[32,14,8,32,14]    #32,32
            
            for j in range(1,6):
                i=data[j-1]
                datas+=f"{i}{(lenths[j-1]-len(str(i)))*' '}|"
                
            if len(data)==7:
                datas+=f"{data.pop()}"
            
            else:
                datas+=f"{14*' '}|"
                datas+=f"{data[-2]}{(32-len(str(data[-2])))*' '}|"
                datas+=f"{data[-1]}{(32-len(data[-1]))*' '}"
            print(datas+'\n')

    else:
        print("Noto'g'ri tugmani bosdingiz\n\n")
                
            