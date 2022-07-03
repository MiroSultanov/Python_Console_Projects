from tkinter import *
import random
import os
from tkinter import messagebox


# ============main============================
class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("SoftUni Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="SoftUni Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12,
                      bg="#badc57", fg="Black", relief=GROOVE)
        title.pack(fill=X)
        # ================variables=======================
        self.sanitizer = IntVar()
        self.face_mask = IntVar()
        self.hand_gloves = IntVar()
        self.hair_shampoo = IntVar()
        self.soap_dove = IntVar()
        self.toothpaste = IntVar()
        # ============grocery==============================
        self.pizza = IntVar()
        self.bread = IntVar()
        self.sushi = IntVar()
        self.milk = IntVar()
        self.flour = IntVar()
        self.spaghetti = IntVar()
        # =============coldDtinks=============================
        self.coffee = IntVar()
        self.redbull = IntVar()
        self.coke_cola = IntVar()
        self.fanta = IntVar()
        self.sprite = IntVar()
        self.mineral_water = IntVar()
        # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=8, bd=7, font=('arial', 12, 'bold'),
                         relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Products", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5,
                              relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Face Mask", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.face_mask, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5,
                                relief=GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        hair_shampoo = Label(F2, text="Hair Shampoo", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        hair_shampoo.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        hair_shampoo_txt = Entry(F2, width=10, textvariable=self.hair_shampoo, font=('times new roman', 16, 'bold'),
                                 bd=5,
                                 relief=GROOVE)
        hair_shampoo_txt.grid(row=3, column=1, padx=10, pady=10)

        soap_dove = Label(F2, text="Soap Dove", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        soap_dove.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        soap_dove_txt = Entry(F2, width=10, textvariable=self.soap_dove, font=('times new roman', 16, 'bold'), bd=5,
                              relief=GROOVE)
        soap_dove_txt.grid(row=4, column=1, padx=10, pady=10)

        toothpaste = Label(F2, text="Toothpaste", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        toothpaste.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        toothpaste_txt = Entry(F2, width=10, textvariable=self.toothpaste, font=('times new roman', 16, 'bold'), bd=5,
                               relief=GROOVE)
        toothpaste_txt.grid(row=5, column=1, padx=10, pady=10)

        # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        pizza = Label(F3, text="Pizza", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        pizza.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        pizza_txt = Entry(F3, width=10, textvariable=self.pizza, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        pizza_txt.grid(row=0, column=1, padx=10, pady=10)

        bread = Label(F3, text="Bread", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        bread.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        bread_txt = Entry(F3, width=10, textvariable=self.bread, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        bread_txt.grid(row=1, column=1, padx=10, pady=10)

        sushi = Label(F3, text="Sushi", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sushi.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        sushi_txt = Entry(F3, width=10, textvariable=self.sushi, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        sushi_txt.grid(row=2, column=1, padx=10, pady=10)

        milk = Label(F3, text="Milk", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        milk.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        milk_txt = Entry(F3, width=10, textvariable=self.milk, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        milk_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        spaghetti_lbl = Label(F3, text="Spaghetti", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        spaghetti_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        spaghetti_lbl_txt = Entry(F3, width=10, textvariable=self.spaghetti, font=('times new roman', 16, 'bold'), bd=5,
                                  relief=GROOVE)
        spaghetti_lbl_txt.grid(row=5, column=1, padx=10, pady=10)

        # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F4.place(x=670, y=180, width=325, height=380)

        coffee_lbl = Label(F4, text="Coffee", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        coffee_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        coffee_lbl_txt = Entry(F4, width=10, textvariable=self.coffee, font=('times new roman', 16, 'bold'), bd=5,
                               relief=GROOVE)
        coffee_lbl_txt.grid(row=0, column=1, padx=10, pady=10)

        red_bull_lbl = Label(F4, text="RedBull", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        red_bull_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        red_bull_lbl_txt = Entry(F4, width=10, textvariable=self.redbull, font=('times new roman', 16, 'bold'), bd=5,
                                 relief=GROOVE)
        red_bull_lbl_txt.grid(row=1, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        coke_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        coke_lbl_txt = Entry(F4, width=10, textvariable=self.coke_cola, font=('times new roman', 16, 'bold'), bd=5,
                             relief=GROOVE)
        coke_lbl_txt.grid(row=2, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        fanta_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        fanta_lbl_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5,
                              relief=GROOVE)
        fanta_lbl_txt.grid(row=3, column=1, padx=10, pady=10)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sprite_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        sprite_lbl_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5,
                               relief=GROOVE)
        sprite_lbl_txt.grid(row=4, column=1, padx=10, pady=10)

        mineral_water_lbl = Label(F4, text="Mineral Water", font=('times new roman', 16, 'bold'), bg="#badc57",
                                  fg="black")
        mineral_water_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mineral_water_lbl_txt = Entry(F4, width=10, textvariable=self.mineral_water,
                                      font=('times new roman', 16, 'bold'),
                                      bd=5, relief=GROOVE)
        mineral_water_lbl_txt.grid(row=5, column=1, padx=10, pady=10)

        # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=270, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#badc57",
                       fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

        # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=490, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=10, width=10,
                           font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white",
                                  pady=10, width=10, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=10,
                           width=10, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=10, width=10,
                          font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    # ================totalBill==========================
    def total(self):
        self.m_h_g_p = self.hand_gloves.get() * 3
        self.m_s_p = self.sanitizer.get() * 1
        self.m_m_p = self.face_mask.get() * 1.2
        self.m_d_p = self.hair_shampoo.get() * 6
        self.m_n_p = self.soap_dove.get() * 1
        self.m_t_g_p = self.toothpaste.get() * 5
        self.total_medical_price = float(
            self.m_m_p + self.m_h_g_p + self.m_d_p + self.m_n_p + self.m_t_g_p + self.m_s_p)

        self.medical_price.set(str(f"{self.total_medical_price:.2f}") + " Лева ")
        self.c_tax = round((self.total_medical_price * 0.20), 2)
        self.medical_tax.set(str(f"{self.c_tax:.2f}") + " Лева ")

        self.g_r_p = self.pizza.get() * 10
        self.g_f_o_p = self.bread.get() * 1.5
        self.g_w_p = self.sushi.get() * 15
        self.g_d_p = self.milk.get() * 2
        self.g_f_p = self.flour.get() * 1.8
        self.g_m_p = self.spaghetti.get() * 3
        self.total_grocery_price = float(self.g_r_p + self.g_f_o_p + self.g_w_p + self.g_d_p + self.g_f_p + self.g_m_p)

        self.grocery_price.set(str(f"{self.total_grocery_price:.2f}") + " Лева ")
        self.g_tax = round((self.total_grocery_price * 0.20), 2)
        self.grocery_tax.set(str(f"{self.g_tax:.2f}") + " Лева ")

        self.c_d_s_p = self.coffee.get() * 1.5
        self.c_d_l_p = self.redbull.get() * 3
        self.c_d_m_p = self.coke_cola.get() * 1
        self.c_d_c_p = self.fanta.get() * 1
        self.c_d_f_p = self.sprite.get() * 1
        self.c_m_d = self.mineral_water.get() * 1
        self.total_cold_drinks_price = float(
            self.c_d_s_p + self.c_d_l_p + self.c_d_m_p + self.c_d_c_p + self.c_d_f_p + self.c_m_d)

        self.cold_drinks_price.set(str(f"{self.total_cold_drinks_price:.2f}") + " Лева ")
        self.c_d_tax = round((self.total_cold_drinks_price * 0.2), 2)
        self.cold_drinks_tax.set(str(f"{self.c_d_tax:.2f}") + " Лева ")

        self.total_bill = float(
            self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    # ==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "Welcome Webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n============================")
        self.txtarea.insert(END, f"\nProducts \t    QTY\t     Price")

    # =========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Лева. 0.0" and self.grocery_price.get() == "Лева. 0.0" \
                and self.cold_drinks_price.get() == "Лева. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
        # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.face_mask.get() != 0:
            self.txtarea.insert(END, f"\n Face Mask\t\t{self.face_mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.hair_shampoo.get() != 0:
            self.txtarea.insert(END, f"\n Hair Shampoo\t\t{self.hair_shampoo.get()}\t\t{self.m_d_p}")
        if self.soap_dove.get() != 0:
            self.txtarea.insert(END, f"\n Soap Dove\t\t{self.soap_dove.get()}\t\t{self.m_n_p}")
        if self.toothpaste.get() != 0:
            self.txtarea.insert(END, f"\n Toothpaste\t\t{self.toothpaste.get()}\t\t{self.m_t_g_p}")
        # ==============Grocery============================
        if self.pizza.get() != 0:
            self.txtarea.insert(END, f"\n Pizza\t\t{self.pizza.get()}\t\t{self.g_r_p}")
        if self.bread.get() != 0:
            self.txtarea.insert(END, f"\n Bread\t\t{self.bread.get()}\t\t{self.g_f_o_p}")
        if self.sushi.get() != 0:
            self.txtarea.insert(END, f"\n Sushi\t\t{self.sushi.get()}\t\t{self.g_w_p}")
        if self.milk.get() != 0:
            self.txtarea.insert(END, f"\n Milk\t\t{self.milk.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.spaghetti.get() != 0:
            self.txtarea.insert(END, f"\n Spaghetti\t\t{self.spaghetti.get()}\t\t{self.g_m_p}")
        # ================ColdDrinks==========================
        if self.coffee.get() != 0:
            self.txtarea.insert(END, f"\n Coffee\t\t{self.coffee.get()}\t\t{self.c_d_s_p}")
        if self.redbull.get() != 0:
            self.txtarea.insert(END, f"\n RedBull\t\t{self.redbull.get()}\t\t{self.c_d_l_p}")
        if self.coke_cola.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke_cola.get()}\t\t{self.c_d_m_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.c_d_c_p}")
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_f_p}")
        if self.mineral_water.get() != 0:
            self.txtarea.insert(END, f"\n Mineral Water\t\t{self.mineral_water.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n----------------------------")
        # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nMedical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\nTotal Bill:\t\t  {self.total_bill:.2f} Лева")
        self.txtarea.insert(END, f"\n----------------------------")
        self.save_bill()

    # =========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
            return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.face_mask.set(0)
            self.hand_gloves.set(0)
            self.hair_shampoo.set(0)
            self.soap_dove.set(0)
            self.toothpaste.set(0)
            # ============grocery==============================
            self.pizza.set(0)
            self.bread.set(0)
            self.sushi.set(0)
            self.milk.set(0)
            self.flour.set(0)
            self.spaghetti.set(0)
            # =============coldDrinks=============================
            self.coffee.set(0)
            self.redbull.set(0)
            self.coke_cola.set(0)
            self.fanta.set(0)
            self.sprite.set(0)
            self.mineral_water.set(0)
            # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = BillApp(root)
root.mainloop()