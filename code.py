import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="root")
cur=db.cursor()

def insert():
    trainerid=int(input("Enter Trainer ID : "))
    tname=input("Enter Trainer Name : ")
    contact=input("Enter Trainer Phone Number : ")
    workingdays=int(input("Enter Number of Working Days : "))
    remuneration=int(input("Enter Remuneration : "))
    memberid=int(input("Enter Member ID : "))
    mname=input("Enter Member Name : ")
    workoutdays=int(input("Enter Workout Days : "))
    try:
        cur.execute("INSERT INTO members values('"+str(memberid)+"','"+str(mname)+"','"+str(trainerid)+"','"+str(workoutdays)+"')")
        db.commit()
        print("DATA INSERTION SUCCESSFULL")
    except:
        print("ERROR WHILE EXECUTING PROGRAM !!")
    try:
        cur.execute("INSERT INTO trainers values('"+str(trainerid)+"','"+str(tname)+"','"+str(contact)+"','"+str(workingdays)+"','"+str(remuneration)+"')")
        db.commit()
        print("DATA INSERTION SUCCESSFULL")
    except:
        print("ERROR WHILE EXECUTING PROGRAM !!")


def q1():
    cur.execute("select max(workout_days) from member_name ")
    db.commit()


def q2():
    cur.execute("select member_id and trainer_id, members.workout_days from members and trainers.working_days from trainers where members.workout_days= trainers.working_days ")
    for i in cur:
        print(i)
    

def q3():
    cur.execute("alter table trainers add bonus int")
    print("COLOUMN ADDED ")
    cur.execute("update trainers set bonus=2300 where trainer_id='101' ")
    cur.execute("update trainers set bonus=2600 where trainer_id='102' ")
    cur.execute("update trainers set bonus=2000 where trainer_id='103' ")
    db.commit()
    print("DATA UPDATED ")


def q4_5():
    avgsalary=int(input("Enter Average Salary : "))
    cur.execute("select trainer_remuneration from trainers where trainer_remuneration< avgsalary ")
    db.commit()
    
    
def q6():
    cur.execute("select * from members")
    db.commit()


def q7():
    cur.execute("select member_id and member_name from members where workout_days%2!=0 ")
    db.commit()
    

def q8():
    #Enter 102 as TrainerID
    trainerid2=input("Enter Trainer ID : ")
    cur.execute("update users set trainer_id= '"+str(trainerid2)+"' where trainers.trainer_id='101'")
    db.commit()
    
def q9():
    cur.execute("DELETE from trainers,members where trainers.trainer_id = members.trainer_id and trainer_name='Rahul' ")
    db.commit
    

def main():
    cur.execute("create database if not exists localgym")
    db.commit()
    print("DATABASE CREATED ")
    cur.execute("use localgym")
    cur.execute("create table if not exists trainers(trainer_id int(50) primary key, trainer_name varchar(50), trainer_contact varchar(50), working_days int(50), trainer_remuneration int(50)))")
    db.commit()
    print("TABLE CREATED")
    cur.execute("create table if not exists members(member_id int(50) primary key, member_name varchar(50), trainer_id int(50) references trainers(trainer_id), workout_days int(50)))")
    db.commit()
    print("TABLE CREATED")
    print("Press 0 to Insert Data ")
    print("Press 1 to do Q1 ")
    print("Press 2 to do Q2 ")
    print("Press 3 to do Q3 ")
    print("Press 4 to do Q4 ")
    print("Press 5 to do Q5 ")
    print("Press 6 to do Q6 ")
    print("Press 7 to do Q7 ")
    print("Press 8 to do Q8 ")
    print("Press 9 to do Q9 ")
    ch=int(input("Enter Your Choice : "))
    try:
        if(ch==0):
            insert()
        elif(ch==1):
            q1()
        elif(ch==2):
            q2()
        elif(ch==3):
            q3()
        elif(ch==4):
            q4()
        elif(ch==5):
            q5()
        elif(ch==6):
            q6()
        elif(ch==7):
            q7()
        elif(ch==8):
            q8()
        elif(ch==9):
            q9()
        else:
            print("INVALID CHOICE !!")
    except:
        print("ENTER A VALID CHOICE FROM THE GIVEN MENU !!! ")
            
            
main()
    
    
