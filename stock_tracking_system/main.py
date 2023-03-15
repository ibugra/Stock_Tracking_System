from cgitb import text
import locale
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import back, color, width
import pymysql 
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import datetime

class stockTracking: 
    
    def __init__(self, root):
        self.root = root
        titleSpace = " "
        self.root.title(80 * titleSpace + "STOCK TRACKING SYSTEM ORTA ANADOLU")
        self.root.geometry("834x700+300+0")
        self.root.resizable(width=False, height=False)
        root.iconbitmap("orta.ico")
        
        #defining variables
        product_ID = StringVar()
        product_name = StringVar()
        product_amount = StringVar()
        product_category = StringVar()
        
        product_detail_ID = StringVar()
        product_detail_date = StringVar()
        product_detail_product_ID = StringVar()
        product_detail_invoice_ID = StringVar()

        invoice_ID = StringVar()
        invoice_customer_ID = StringVar()
        invoice_date = StringVar()

        customer_ID = StringVar()
        customer_name = StringVar()
        customer_tel = StringVar()
        customer_address = StringVar()

        address_customer_ID = StringVar()
        address_city = StringVar()
        address_country = StringVar()
        addres_district = StringVar()
        address_open = StringVar()
        address_post_code = StringVar()

        def exit():
            exit = tkinter.messagebox.askyesno("Stock Tracking System", "Do you want to exit?")
            if exit>0:
                root.destroy()
                return

        def InsertWindow():
            
            newWindow = Toplevel(root)
            newWindow.title("Inserting")
            newWindow.geometry("900x700+300+0")

            def reset():
                entProductName.delete(0,END)
                product_amount.set("")
                entProductCategory.delete(0,END)
                entCustomerName.delete(0,END)
                entCustomerTel.delete(0,END)
                entAddressCountry.delete(0,END)
                entAddressCity.delete(0,END)
                entAddressDistrict.delete(0,END)
                entAddressOpen.delete(0,END)
                entAddressPostCode.delete(0,END)
                invoice_date.set("YYYY-MM-DD")



            #Frames
            MainFrameInsert = Frame(newWindow, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
            MainFrameInsert.grid()
            
            TitleFrameInsert = Frame(MainFrameInsert, bd=7, width=770, height=100, relief=RIDGE)
            TitleFrameInsert.grid(row=0, column=0)
         

            TopFrameInsert = Frame(MainFrameInsert, bd=5, width=770, height=500, relief=RIDGE)
            TopFrameInsert.grid(row=1, column=0)

            LeftFrameInsert = Frame(TopFrameInsert, bd=5, width=770, height=400, padx=2, bg='#40739f', relief=RIDGE)
            LeftFrameInsert.pack(side=LEFT)
            LeftFrame1Insert = Frame(LeftFrameInsert, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
            LeftFrame1Insert.pack(side=TOP)

            TopFrameInsert1 = Frame(MainFrameInsert, bd=5, width=770, height=500, relief=FLAT)
            TopFrameInsert1.grid(row=2, column=0)

            ButtonFrame = Frame(TopFrameInsert1,bd=5, width=770, height=100, padx=2, bg='#40739f', relief=FLAT)
            ButtonFrame.pack(side=BOTTOM)
            ButtonFrame1 = Frame(ButtonFrame, bd=5, width=90, height=300, padx=2, pady=2, relief=FLAT)
            ButtonFrame1.pack(side=BOTTOM)

            newWindow.btnInsert=Button(ButtonFrame1,font=('verdana',12,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2,command=insert).grid(row=0,column=0,padx=1)            
            newWindow.btnInsert=Button(ButtonFrame1,font=('verdana',12,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2,command=reset).grid(row=0,column=1,padx=1)            

            
            #Title
            self.lbltitle = Label(TitleFrameInsert, font=('VERDANA', 20, 'bold'), text="STOCK TRACKING SYSTEM INSERTING", bd=7)
            self.lbltitle.grid(row=0, column=0, padx=132)

            #Labels

            #Products
            lblProduct = Label(LeftFrame1Insert, font=('verdana', 12, 'bold',), text="Product Details", bd=7,bg='#40739f',fg='white')
            lblProduct.grid(row=1, column=0, stick=W, padx=5)

            lblProductName = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Product Name", bd=7)
            lblProductName.grid(row=2, column=0, sticky=W, padx=5)
            entProductName = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_name)
            entProductName.grid(row=2, column=1, sticky=W, padx=5)  

            lblProductAmount = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Product Amount", bd=7)
            lblProductAmount.grid(row=3, column=0, sticky=W, padx=5)
            entProductAmount = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_amount)
            entProductAmount.grid(row=3, column=1, sticky=W, padx=5)  
            
            lblProductCategory = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Category", bd=7)
            lblProductCategory.grid(row=4, column=0, sticky=W, padx=5)
            entProductCategory = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_category)
            entProductCategory.grid(row=4, column=1, sticky=W, padx=5) 

            #Customer

            lblCustomer = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Customer Details", bd=7, bg='#40739f',fg='white')
            lblCustomer.grid(row=5, column=0, padx=5, stick=W)

            lblCustomerName = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Customer Name", bd=7)
            lblCustomerName.grid(row=6, column=0, sticky=W, padx=5)
            entCustomerName = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=customer_name)
            entCustomerName.grid(row=6, column=1, sticky=W, padx=5)  

            lblCustomerTel = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Customer Tel", bd=7)
            lblCustomerTel.grid(row=7, column=0, sticky=W, padx=5)
            entCustomerTel = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=customer_tel)
            entCustomerTel.grid(row=7, column=1, sticky=W, padx=5) 

            #Address

            lblAddress = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Address Details", bd=7, bg='#40739f',fg='white')
            lblAddress.grid(row=8, column=0, sticky=W, padx=5)

            lblAddressCountry = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Country", bd=7)
            lblAddressCountry.grid(row=9, column=0, sticky=W, padx=5)
            entAddressCountry = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_country)
            entAddressCountry.grid(row=9, column=1, sticky=W, padx=5)  

            lblAddressCity = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="City", bd=7)
            lblAddressCity.grid(row=10, column=0, sticky=W, padx=5)
            entAddressCity = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_city)
            entAddressCity.grid(row=10, column=1, sticky=W, padx=5) 

            lblAddressDistrict = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="District", bd=7)
            lblAddressDistrict.grid(row=11, column=0, sticky=W, padx=5)
            entAddressDistrict = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=addres_district)
            entAddressDistrict.grid(row=11, column=1, sticky=W, padx=5)  

            lblAddressOpen = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Open Address", bd=7)
            lblAddressOpen.grid(row=12, column=0, sticky=W, padx=5)
            entAddressOpen = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_open)
            entAddressOpen.grid(row=12, column=1, sticky=W, padx=5)

            lblAddressPostCode = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Post Code", bd=7)
            lblAddressPostCode.grid(row=13, column=0, sticky=W, padx=5)
            entAddressPostCode = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_post_code)
            entAddressPostCode.grid(row=13, column=1, sticky=W, padx=5)

            #Invoice

            lblInvoice = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Invoice Details", bd=7, bg='#40739f',fg='white')
            lblInvoice.grid(row=14, column=0, sticky=W, padx=5)

            lblInvoiceDate = Label(LeftFrame1Insert, font=('verdana', 12, 'bold'), text="Invoice Date", bd=7)
            lblInvoiceDate.grid(row=15, column=0, sticky=W, padx=5)
            entInvoiceDate = Entry(LeftFrame1Insert, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=invoice_date)
            entInvoiceDate.insert(0, "YYYY-MM-DD")
            invoice_date.set("YYYY-MM-DD")

            def on_enter(e):
                entInvoiceDate.delete(0,'end')
            def on_leave(e):
                if entInvoiceDate.get()=='':
                    entInvoiceDate.insert(0,'YYYY-MM-DD')

            entInvoiceDate.bind("<FocusIn>",on_enter)
            entInvoiceDate.bind("<FocusOut>",on_leave)
            entInvoiceDate.grid(row=15, column=1, sticky=W, padx=5)

        
        def insert():
            if product_name.get() == "" or product_amount.get() == "" or product_category == "":
               tkinter.messagebox.showerror("Stock Tracking System", "An error has occurred")
            
            else:
                sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
                cur = sqlCon.cursor()

                #inserting address into database and fetching the last ID of address
                cur.execute("insert into address (`Country`, `City`, `District`, `OpenAddress`, `PostCode`) values(%s,%s,%s,%s,%s)", (address_country.get(), address_city.get(), addres_district.get(), address_open.get(),address_post_code.get()))
                cur.execute('SELECT address.ID FROM address WHERE id = ( SELECT MAX(ID) FROM address )')
                created_address_ID = cur.fetchall()
                temporary_ID = created_address_ID[0][0]
                

                #inserted customer into db and fetched last ID of customer
                cur.execute("insert into customer (`Name_Surname`, `Tel`, `Address_ID`) values(%s,%s,%s)", (customer_name.get(), customer_tel.get(), temporary_ID))
                cur.execute('SELECT customer.ID FROM customer WHERE id = ( SELECT MAX(ID) FROM customer )')
                created_customer_ID = cur.fetchall()
                temporary_customer_ID = created_customer_ID[0][0]
                
                #inserted invoice date into db and fetching the last ID of invoice 
                temp = invoice_date.get()
                list = temp.split("-")
                year = list[0]
                month = list[1]
                day = list[2]
                now = datetime(int(year),int(month),int(day))
                formatted_date = now.strftime('%Y-%m-%d')
                cur.execute("insert into invoices (`Customer_ID`, `Date_`) values(%s,%s)", (temporary_customer_ID, formatted_date))
                cur.execute('SELECT invoices.ID FROM invoices WHERE id = ( SELECT MAX(ID) FROM invoices )')
                created_invoice_ID = cur.fetchall()
                temporary_invoice_ID = created_invoice_ID[0][0]

                #inserted product into db
                cur.execute("insert into products (`Product_Name`, `Amount`, `Category`) values(%s,%s,%s)", (product_name.get(), product_amount.get(), product_category.get()))
                cur.execute('SELECT products.ID FROM products WHERE id = ( SELECT MAX(ID) FROM products )')
                created_product_ID = cur.fetchall()
                temporary_product_ID = created_product_ID[0][0]

               
                # inserted product detail into db
                now1 = datetime.now()
                formatted_date1 = now1.strftime('%Y-%m-%d')
                cur.execute("insert into product_detail (`Date_`, `Invoice_ID`, `Product_ID`) values(%s,%s,%s)", (formatted_date1, temporary_invoice_ID, temporary_product_ID))

                
                sqlCon.commit()
                sqlCon.close()
          
                print(product_amount.get())
                tkinter.messagebox.showinfo("Stock Tracking System", "Record Entered Successfully")

        def displayData():
            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select products.ID, products.Product_Name, products.Amount, product_detail.Invoice_ID, products.Category from products INNER JOIN product_detail on products.ID = product_detail.product_ID")
            result = cur.fetchall()
            if len(result) != 0:
                self.product_records.delete(*self.product_records.get_children())
                for row in result:
                    self.product_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()

            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select customer.ID, customer.Name_Surname, customer.Tel, address.OpenAddress from customer INNER JOIN address on address.ID = customer.Address_ID")
            result = cur.fetchall()
            if len(result) != 0:
                self.customer_records.delete(*self.customer_records.get_children())
                for row in result:
                    self.customer_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close() 

            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select invoices.ID, invoices.Customer_ID, invoices.Date_ from invoices")
            result = cur.fetchall()
            if len(result) != 0:
                self.invoices_records.delete(*self.invoices_records.get_children())
                for row in result:
                    self.invoices_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close() 

        def productInfo(ev):
            viewInfo = self.product_records.focus()
            learnData = self.product_records.item(viewInfo)
            row = learnData['values']
            product_ID.set(row[0])
            product_name.set(row[1])
            product_amount.set(row[2])
            product_category.set(row[3])
            invoice_ID.set(row[4])

        
        def search():

            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select products.ID, products.Product_Name, products.Amount, product_detail.Invoice_ID, products.Category from products INNER JOIN product_detail on products.ID = product_detail.ID where products.ID = %s", product_ID.get())
            result = cur.fetchall()
            if len(result) != 0:
                self.product_records.delete(*self.product_records.get_children())
                for row in result:
                    self.product_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()
          
            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select customer.ID, customer.Name_Surname, customer.Tel, address.OpenAddress from customer INNER JOIN address on customer.Address_ID = address.ID where customer.ID = %s", customer_ID.get())
            result = cur.fetchall()
            if len(result) != 0:
                self.customer_records.delete(*self.customer_records.get_children())
                for row in result:
                    self.customer_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close() 

            sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
            cur = sqlCon.cursor()
            cur.execute("select invoices.ID, invoices.Customer_ID, invoices.Date_ from invoices where invoices.ID = %s", invoice_ID.get())
            result = cur.fetchall()
            if len(result) != 0:
                self.invoices_records.delete(*self.invoices_records.get_children())
                for row in result:
                    self.invoices_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close() 

        def Reset():
            self.entProductID.delete(0,END)
            self.entCustomerID.delete(0,END)
            self.entInvoiceID.delete(0,END)
            self.product_records.delete(*self.product_records.get_children())
            self.customer_records.delete(*self.customer_records.get_children())
            self.invoices_records.delete(*self.invoices_records.get_children())


        def newWindowUpdate():
            newWindowUpdate = Toplevel(root)
            newWindowUpdate.title("Updating")
            newWindowUpdate.geometry("1250x722+300+0")    

            def displayDataUpdate():
                sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
                cur = sqlCon.cursor()
                cur.execute("select products.ID, products.Product_Name, products.Amount, product_detail.Invoice_ID, products.Category from products INNER JOIN product_detail on products.ID = product_detail.product_ID")
                result = cur.fetchall()
                if len(result) != 0:
                    self.product_records.delete(*self.product_records.get_children())
                    for row in result:
                        self.product_records.insert('',END,values=row)
                sqlCon.commit()
                sqlCon.close()

                sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
                cur = sqlCon.cursor()
                cur.execute("select customer.ID, customer.Name_Surname, customer.Tel, invoices.Date_ from customer INNER JOIN invoices on invoices.customer_ID = customer.ID")
                result = cur.fetchall()
                if len(result) != 0:
                    self.customer_records.delete(*self.customer_records.get_children())
                    for row in result:
                        self.customer_records.insert('',END,values=row)
                sqlCon.commit()
                sqlCon.close() 

                sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
                cur = sqlCon.cursor()
                cur.execute("select customer.ID, address.Country, address.City, address.District, address.OpenAddress, address.PostCode from customer INNER JOIN address on customer.Address_ID = address.ID")
                result = cur.fetchall()
                if len(result) != 0:
                    self.address_records.delete(*self.address_records.get_children())
                    for row in result:
                        self.address_records.insert('',END,values=row)
                sqlCon.commit()
                sqlCon.close()

            def InfoProduct(ev):
                viewInfo = self.product_records.focus()
                learnData = self.product_records.item(viewInfo)
                row = learnData['values']
                product_ID.set(row[0])
                product_name.set(row[1])
                product_amount.set(row[2])
                product_category.set(row[4])

            def InfoCustomer(ev):
                viewInfoCustomer = self.customer_records.focus()
                learnDataCustomer = self.customer_records.item(viewInfoCustomer)
                rowCustomer = learnDataCustomer['values']
                customer_ID.set(rowCustomer[0])
                customer_name.set(rowCustomer[1])
                customer_tel.set(rowCustomer[2])
                invoice_date.set(rowCustomer[3])

            def InfoAddress(ev):
                viewInfoAddress = self.address_records.focus()
                learnDataAddress = self.address_records.item(viewInfoAddress)
                rowAddress = learnDataAddress['values']
                address_customer_ID.set(rowAddress[0])
                address_country.set(rowAddress[1])
                address_city.set(rowAddress[2])
                addres_district.set(rowAddress[3])
                address_open.set(rowAddress[4])
                address_post_code.set(rowAddress[5])
                
            
            def update():
                if (product_name.get() == "" or product_amount.get() == "" or product_category.get() == "") and ( customer_name.get() == "" or customer_tel.get() == "") and (address_country.get() == "" or address_city.get() == "" or addres_district.get() == "" or address_open.get() == "" or address_post_code.get() == "" ):
                    tkinter.messagebox.showerror("Stock Tracking System", "There is no selected record!")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="3859", database="dbstock")
                    cur = sqlCon.cursor()
                    cur.execute("update products set Product_Name=%s, Amount=%s, Category=%s where products.ID = %s",
                                (product_name.get(), product_amount.get(), product_category.get(), product_ID.get()))
                    sqlCon.commit()
                    sqlCon.close()


                    sqlCon = pymysql.connect(host="localhost", user="root", password="3859", database="dbstock")
                    cur = sqlCon.cursor()
                    cur.execute("update customer set Name_Surname = %s, Tel = %s where customer.ID = %s",
                                (customer_name.get(), customer_tel.get(), customer_ID.get()))
                    sqlCon.commit()
                    sqlCon.close()

                    sqlCon = pymysql.connect(host="localhost", user="root", password="3859", database="dbstock")
                    cur = sqlCon.cursor()
                    cur.execute("update address inner join customer on address.ID = customer.Address_ID set Country = %s, City = %s, District = %s, OpenAddress = %s, PostCode = %s where customer.ID = %s",
                                (address_country.get(), address_city.get(), addres_district.get(), address_open.get(), address_post_code.get(), address_customer_ID.get()))
                    sqlCon.commit()
                    sqlCon.close()

                    tkinter.messagebox.showinfo("Stock Tracking System", "Record Updated Successfully")
                    displayDataUpdate() 


            #Frames
            MainFrameUpdate = Frame(newWindowUpdate, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
            MainFrameUpdate.grid()
            
            TitleFrameUpdate = Frame(MainFrameUpdate, bd=7, width=770, height=100, relief=RIDGE)
            TitleFrameUpdate.grid(row=0, column=0)
         

            TopFrameUpdate = Frame(TitleFrameUpdate, bd=5, width=770, height=500, relief=RIDGE)
            TopFrameUpdate.grid(row=1, column=0)

            LeftFrameUpdate = Frame(TopFrameUpdate, bd=5, width=770, height=400, padx=2, bg='#40739f', relief=RIDGE)
            LeftFrameUpdate.pack(side=LEFT)
            LeftFrame1Update = Frame(LeftFrameUpdate, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
            LeftFrame1Update.pack(side=TOP)
        
            ButtomFrameMid = Frame(TopFrameUpdate, bd=5, width=770, height=2, padx=2, bg='#40739f', relief=RIDGE)
            ButtomFrameMid.pack(side=RIGHT)
            
            TopFrameUpdate1 = Frame(MainFrameUpdate, bd=5, width=770, height=500, relief=FLAT)
            TopFrameUpdate1.grid(row=2, column=0)

            ButtonFrameUpdate = Frame(TopFrameUpdate1,bd=5, width=770, height=100, padx=2, bg='#40739f', relief=FLAT)
            ButtonFrameUpdate.pack(side=BOTTOM)
            ButtonFrame1Update = Frame(ButtonFrameUpdate, bd=5, width=90, height=300, padx=2, pady=2, relief=FLAT)
            ButtonFrame1Update.pack(side=BOTTOM)

            newWindowUpdate.btnInsert=Button(ButtonFrame1Update,font=('verdana',12,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2,command=update).grid(row=0,column=0,padx=1)            
            
            #Title
            self.lbltitle = Label(TitleFrameUpdate, font=('VERDANA', 20, 'bold'), text="STOCK TRACKING SYSTEM UPDATING", bd=7)
            self.lbltitle.grid(row=0, column=0, padx=132)

            #Labels

            #Products
            lblProduct = Label(LeftFrame1Update, font=('verdana', 12, 'bold',), text="Product Details", bd=7,bg='#40739f',fg='white')
            lblProduct.grid(row=1, column=0, stick=W, padx=5)

            lblProductName = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Product Name", bd=7)
            lblProductName.grid(row=2, column=0, sticky=W, padx=5)
            entProductName = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_name)
            entProductName.grid(row=2, column=1, sticky=W, padx=5)  

            lblProductAmount = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Product Amount", bd=7)
            lblProductAmount.grid(row=3, column=0, sticky=W, padx=5)
            entProductAmount = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_amount)
            entProductAmount.grid(row=3, column=1, sticky=W, padx=5)  
            
            lblProductCategory = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Category", bd=7)
            lblProductCategory.grid(row=4, column=0, sticky=W, padx=5)
            entProductCategory = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_category)
            entProductCategory.grid(row=4, column=1, sticky=W, padx=5) 

            #Customer

            lblCustomer = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Customer Details", bd=7, bg='#40739f',fg='white')
            lblCustomer.grid(row=5, column=0, padx=5, stick=W)

            lblCustomerName = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Customer Name", bd=7)
            lblCustomerName.grid(row=6, column=0, sticky=W, padx=5)
            entCustomerName = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=customer_name)
            entCustomerName.grid(row=6, column=1, sticky=W, padx=5)  

            lblCustomerTel = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Customer Tel", bd=7)
            lblCustomerTel.grid(row=7, column=0, sticky=W, padx=5)
            entCustomerTel = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=customer_tel)
            entCustomerTel.grid(row=7, column=1, sticky=W, padx=5) 

            #Address

            lblAddress = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Address Details", bd=7, bg='#40739f',fg='white')
            lblAddress.grid(row=8, column=0, sticky=W, padx=5)

            lblAddressCountry = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Country", bd=7)
            lblAddressCountry.grid(row=9, column=0, sticky=W, padx=5)
            entAddressCountry = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_country)
            entAddressCountry.grid(row=9, column=1, sticky=W, padx=5)  

            lblAddressCity = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="City", bd=7)
            lblAddressCity.grid(row=10, column=0, sticky=W, padx=5)
            entAddressCity = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_city)
            entAddressCity.grid(row=10, column=1, sticky=W, padx=5) 

            lblAddressDistrict = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="District", bd=7)
            lblAddressDistrict.grid(row=11, column=0, sticky=W, padx=5)
            entAddressDistrict = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=addres_district)
            entAddressDistrict.grid(row=11, column=1, sticky=W, padx=5)  

            lblAddressOpen = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Open Address", bd=7)
            lblAddressOpen.grid(row=12, column=0, sticky=W, padx=5)
            entAddressOpen = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_open)
            entAddressOpen.grid(row=12, column=1, sticky=W, padx=5)

            lblAddressPostCode = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Post Code", bd=7)
            lblAddressPostCode.grid(row=13, column=0, sticky=W, padx=5)
            entAddressPostCode = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=address_post_code)
            entAddressPostCode.grid(row=13, column=1, sticky=W, padx=5)

            #Invoice

            lblInvoice = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Invoice Details", bd=7, bg='#40739f',fg='white')
            lblInvoice.grid(row=14, column=0, sticky=W, padx=5)

            lblInvoiceDate = Label(LeftFrame1Update, font=('verdana', 12, 'bold'), text="Invoice Date", bd=7)
            lblInvoiceDate.grid(row=15, column=0, sticky=W, padx=5)
            entInvoiceDate = Entry(LeftFrame1Update, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=invoice_date)
            entInvoiceDate.insert(0, "YYYY-MM-DD")
            invoice_date.set("YYYY-MM-DD")
       

            def on_enter(e):
                entInvoiceDate.delete(0,'end')
            def on_leave(e):
                if entInvoiceDate.get()=='':
                    entInvoiceDate.insert(0,'YYYY-MM-DD')
                  

            entInvoiceDate.bind("<FocusIn>",on_enter)
            entInvoiceDate.bind("<FocusOut>",on_leave)
            entInvoiceDate.grid(row=15, column=1, sticky=W, padx=5)


            scroll_y = Scrollbar(ButtomFrameMid, orient=VERTICAL)
            scroll_X = Scrollbar(ButtomFrameMid, orient=HORIZONTAL)
            #product treeview 
            self.product_records = ttk.Treeview(ButtomFrameMid,height=6,
                        columns=("product_ID","product_name","product_amount","product_detail_invoice_ID","product_category"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)
                        
            
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_X.pack(side=BOTTOM, fill=X)
           

            self.product_records.heading("product_ID", text="Product ID")
            self.product_records.heading("product_name", text="Product Name")
            self.product_records.heading("product_amount", text="Amount")
            self.product_records.heading("product_detail_invoice_ID", text="Invoice ID")
            self.product_records.heading("product_category", text="Category")

            self.product_records['show'] = 'headings'

            self.product_records.column("product_ID", width=100)
            self.product_records.column("product_name", width=100)
            self.product_records.column("product_amount", width=100)
            self.product_records.column("product_detail_invoice_ID", width=100)
            self.product_records.column("product_category", width=100)

            self.product_records.pack(fill=BOTH, expand=1)

            self.product_records.bind("<ButtonRelease-1>",InfoProduct)
            

            #self.product_records.bind("<ButtonRelease-1>",productInfo)

            #customer treeview
            self.customer_records = ttk.Treeview(ButtomFrameMid,height=6,
                    columns=("customer_ID","customer_name","customer_tel","invoice_date"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)


            self.customer_records.heading("customer_ID", text="Customer ID")
            self.customer_records.heading("customer_name", text="Customer Name")
            self.customer_records.heading("customer_tel", text="Customer Tel")
            self.customer_records.heading("invoice_date", text="Invoice Date")

            self.customer_records['show'] = 'headings'

            self.customer_records.column("customer_ID", width=100)
            self.customer_records.column("customer_name", width=100)
            self.customer_records.column("customer_tel", width=100)
            self.customer_records.column("invoice_date", width=100)

            self.customer_records.pack(fill=BOTH, expand=1)
            self.customer_records.bind("<ButtonRelease-1>",InfoCustomer)  

            #address treeview
            self.address_records = ttk.Treeview(ButtomFrameMid,height=6,
                    columns=("customer_ID","address_country","address_city","addres_district","address_open", "address_post_code"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)

            self.address_records.heading("customer_ID", text="Customer ID")
            self.address_records.heading("address_country", text="Country")
            self.address_records.heading("address_city", text="City")
            self.address_records.heading("addres_district", text="District")
            self.address_records.heading("address_open", text="Open Address")
            self.address_records.heading("address_post_code", text="Post Code")

            self.address_records['show'] = 'headings'

            self.address_records.column("customer_ID", width=50)
            self.address_records.column("address_country", width=50)
            self.address_records.column("address_city", width=50)
            self.address_records.column("addres_district", width=50)
            self.address_records.column("address_open", width=50)
            self.address_records.column("address_post_code", width=50)
            
            self.address_records.pack(fill=BOTH, expand=1)
            self.address_records.bind("<ButtonRelease-1>",InfoAddress)

            #CustomerID, adresleri bilgileri
            displayDataUpdate()





        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        
        TopFrame = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame, bd=5, width=770, height=400, padx=2, bg='#40739f', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('VERDANA', 26, 'bold'), text="STOCK TRACKING SYSTEM", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblProductID = Label(LeftFrame1, font=('verdana', 12, 'bold'), text="Product ID", bd=7)
        self.lblProductID.grid(row=1, column=0, sticky=W, padx=5)
        self.entProductID = Entry(LeftFrame1, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=product_ID)
        self.entProductID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblCustomerID = Label(LeftFrame1, font=('verdana', 12, 'bold'), text="Customer ID", bd=7)
        self.lblCustomerID.grid(row=2, column=0, sticky=W, padx=5)
        self.entCustomerID = Entry(LeftFrame1, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=customer_ID)
        self.entCustomerID.grid(row=2, column=1, sticky=W, padx=5)

        self.lblInvoiceID = Label(LeftFrame1, font=('verdana', 12, 'bold'), text="Invoice ID", bd=7)
        self.lblInvoiceID.grid(row=3, column=0, sticky=W, padx=5)
        self.entInvoiceID = Entry(LeftFrame1, font=('verdana', 12, 'bold'), bd=5, width=40, justify='left',textvariable=invoice_ID)
        self.entInvoiceID.grid(row=3, column=1, sticky=W, padx=5)

        self.btnInsert=Button(RightFrame1a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2, command=InsertWindow).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2, command=newWindowUpdate).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame1a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2, command=displayData).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame1a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2,command=search).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame1a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2,command=Reset).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame1a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2, command=exit).grid(row=5,column=0,padx=1)


        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        scroll_X = Scrollbar(LeftFrame, orient=HORIZONTAL)
        #product treeview 
        self.product_records = ttk.Treeview(LeftFrame,height=6,
                    columns=("product_ID","product_name","product_amount","product_detail_invoice_ID","product_category"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)
                    
        
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_X.pack(side=BOTTOM, fill=X)

        self.product_records.heading("product_ID", text="Product ID")
        self.product_records.heading("product_name", text="Product Name")
        self.product_records.heading("product_amount", text="Amount")
        self.product_records.heading("product_detail_invoice_ID", text="Invoice ID")
        self.product_records.heading("product_category", text="Category")

        self.product_records['show'] = 'headings'

        self.product_records.column("product_ID", width=100)
        self.product_records.column("product_name", width=100)
        self.product_records.column("product_amount", width=100)
        self.product_records.column("product_detail_invoice_ID", width=100)
        self.product_records.column("product_category", width=100)

        self.product_records.pack(fill=BOTH, expand=1)

        #self.product_records.bind("<ButtonRelease-1>",productInfo)

        #customer treeview
        self.customer_records = ttk.Treeview(LeftFrame,height=6,
                columns=("customer_ID","customer_name","customer_tel","customer_address"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)


        self.customer_records.heading("customer_ID", text="Customer ID")
        self.customer_records.heading("customer_name", text="Customer Name")
        self.customer_records.heading("customer_tel", text="Customer Tel")
        self.customer_records.heading("customer_address", text="Address")

        self.customer_records['show'] = 'headings'

        self.customer_records.column("customer_ID", width=100)
        self.customer_records.column("customer_name", width=100)
        self.customer_records.column("customer_tel", width=100)
        self.customer_records.column("customer_address", width=100)

        self.customer_records.pack(fill=BOTH, expand=1)

        #invoices treeview
        self.invoices_records = ttk.Treeview(LeftFrame,height=6,
                columns=("invoice_ID","invoice_customer_ID","invoice_date"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_X.set)

        self.invoices_records.heading("invoice_ID", text="Invoice ID")
        self.invoices_records.heading("invoice_customer_ID", text="Customer ID")
        self.invoices_records.heading("invoice_date", text="Date")

        self.invoices_records['show'] = 'headings'

        self.invoices_records.column("invoice_ID", width=100)
        self.invoices_records.column("invoice_customer_ID", width=100)
        self.invoices_records.column("invoice_date", width=100)

        self.invoices_records.pack(fill=BOTH, expand=1)



if __name__ == '__main__':
    root = Tk()
    application = stockTracking(root)
    root.mainloop()