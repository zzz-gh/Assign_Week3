from databaseconnector import connect

mydb,cursor = connect()

def setup():
    cursor.execute('create database if not exists assignweek3')
    cursor.execute('use assignweek3')
    cursor.execute('create table if not exists categories(id int auto_increment,category text,brand text,itemDescription longtext,serial_number longtext,price float,stock int,primary key (id));')
    
    cursor.execute('create table if not exists stocks(id int auto_increment,categories_id int,stockin int,stockout int,stock_date Date, primary key (id));')

#step1 build table categories and stock
#categories(id int auto_increment,category text,brand text,
#           itemDescription longtext,serial_number longtext,
#           price float,stock int,primary key (id))
#stocks(id int auto_increment,categories_id int,stockin int,
#           stockout int,stock_date Date, primary key (id))
#step2 addNewCategories() for adding new categories
#step3 displayAllCategories()
#step4 addNewStocks() for get in and get out categories from categories table
#step5 displayStocks()
#step6 getCategoriesId()
#step7 availabe_netStock() to calculate the net stock after addNewStock()
#step8 displayMenu()

def addNewCategories():

    name = input("Please enter the type of category item(laptop,phone,accessories etc..) :")
    b = input('Please enter the type of brand(Apple,Samsung,Xiaomi etc..)')
    i = input('Enter item description for your item (eg. macbook 13inches,Mi9T,Remaxspeaker)')
    se = input('Enter serial number for your item(eg,ZT79LV1379M)')
    p = input('Enter the price of your item:')
    s = input('Enter the available stock.')
    
    cursor.execute('insert into categories(category,brand,itemDescription,serial_number,price,stock) values (%s,%s,%s,%s,%s,%s)',[name,b,i,se,p,s])
    mydb.commit()
    


def displayAllCategories():
   
    cursor.execute('select * from categories')
    for access in cursor.fetchall():
        print(f'[{access[0]}] - {access[1]} - {access[2]} -{access[3]}  -{access[4]}  {access[5]}(Kyats)   ({access[6]}) stock  ')



def addNewStock():
    print('Categories.......')
    displayAllCategories()
    cid = input("Enter categories id that you want to stock in stock out,choose from above:") 
    sin = input('Enter import number of your stock_item to your shop:')
    sout = input('Enter export number of your stock_item from yout shop:')
    d = input('Enter the date(YY/MM/DD):')
    cursor.execute('insert into stocks(categories_id,stockin,stockout,stock_date) values (%s,%s,%s,%s)',[cid,sin,sout,d])
    mydb.commit()

def displayStocks():
    cursor.execute('select * from stocks')
    for sto in cursor.fetchall():
        print(f'[{sto[0]}] - category[{sto[1]}] - {sto[2]}(in) - {sto[3]}(out) - {sto[4]}')




def getCategoriesId(id):
    cursor.execute("select * from categories where id = %s", [id])
    category = cursor.fetchone()
    return category




def availabe_netStock():
    print('Preparing to calculate net stock:')
    print('Catergories.........')
    displayAllCategories()
    print('Stocks..............')
    displayStocks()
    category_id = input('Please select the category:')
    cate = getCategoriesId(category_id)
    
    
    user_choice = input(f'Are you sure want to calculatae net amount of stock ({cate[5]}) net ammount: y/n:')
    if(user_choice == 'y'):
        # increaseAmount = int(input('How do you want to increse :'))

        cid = int(category_id)
        s = int(input('Enter the stock_id for the category that you input above:'))
        cursor.execute('SELECT * FROM assignweek3.stocks where categories_id = %s and id = %s;',[cid,s])
        for sii in cursor.fetchall():
            sin = int(sii[2])
            sout = int(sii[3])
            netAmount = (sin + int(cate[6])) - sout
            cursor.execute('Update categories set stock = %s where id = %s',[netAmount,category_id])
        mydb.commit()
        displayAllCategories()


def displayMenu():
    try:
        selected_option= input(
            f'Please select the action you want to do\n'
            f'[1] Add new categories \n'
            f'[2] Add new stocks \n'
            f'[3] View All Categories \n'
            f'[4] View All Stocks \n'
            f'[5] Calculate Net Amount \n'

        )

        if(selected_option == '1'):
            addNewCategories()
        elif(selected_option == '2'):
            addNewStock()
        elif(selected_option == '3'):
            displayAllCategories()
        elif(selected_option == '4'):
            displayStocks()
        elif(selected_option == '5'):
            availabe_netStock()
        choose = input('Do you want to go back to menu: y/n \n')
        if (choose == 'y'):
            displayMenu()
        else:
            print('Bye Bye')
        
    except KeyboardInterrupt:
        print('Bye Bye')




setup()
displayMenu()
# availabe_netStock()

# addNewCategories()
# displayAllCategories()
# addNewStock()
# displayStocks()

