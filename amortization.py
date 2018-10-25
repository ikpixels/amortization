# How to calculate Loan Amortization Schedule with python
# Author Isaac Kakodwa--------------ikpixels.py@gmail.com

"""Amortization schedule – table, containing the following
   Payments, interest paid, principal paid and outstanding
   principal columns.
    
   Example:Suppose that you take out a MK 250,000 house mortgage
   from your local savings bank.The bank requires you to repay
   the mortgage in equal annual installments over the next 30
   years.It must therefore set the annual payments so that they
   have a present value of MK 250,000"""

class Amortization:
    def __init__ (self, loan, rate, duration ):
        self.loan     = loan
        self.rate     = rate/100
        self.duration = duration
        
    def Payment(self): # Monthly payment calculation
        l    = self.loan
        r    = self.rate
        t    = self.duration
        pymt = l/((1/r)-1/(r*(1+r)**t))# payment formula
        return pymt

class Amortization_Schedule(Amortization):
    
    def calculation(self):
        context  = [] #list of interest from year 1\interest deduction starts in year 1 not year zero
        context2 = [] #list of principal paid\principal is paid from year 1 
        loan     = self.loan  
        rate     = self.rate   
        payment  = self.Payment()
        duration = self.duration + 1
        time     = 0
        period   = 0
        tima     = 0
        Total_interest =round(self.duration*12*payment) - loan
        print("Total interest is MK {}.00".format(round(Total_interest)))
        print("Following Schedule, {} monthly payments of MK {}.00 is required for {} years"
              .format(round(self.duration*12),round(payment),round(self.duration)))
        print("="*80) # line
        print("Note : Outstanding balance of year {} is zero, you will find it bellow."
              .format(round(self.duration)))
        print("="*80) # line
        while loan > 0 and time < duration:
            print("Outstanding Balance for year {} : MK {}.00"
                  .format(time,round(loan)))
            
            interest          = loan * rate
            amortixation_loan = payment - interest
            loan              = loan - amortixation_loan
            time              = time + 1
        
            context2.append(round(amortixation_loan))
            context.append(round(interest))
            
        
            if len(context) and len(context2) == self.duration : 
                print("="*80) # line
                for c in context:
                    period = period +1
                    print("Interest for year {} : MK {}.00".format( period,c))
                    print("-"*80) # line
                for c2 in context2:
                    tima = tima +1
                    print("Principal paid for year {} : MK {}.00".format(tima,c2))
                    print("="*80) # line                
while True:
    try:
        print("*"*80) # line 
        L = float(input("Enter amount of loan >> "))
        R = float(input("Enter interest rate e.g if 12%,enter 12 only >> "))
        T = float(input("Enter duration of loan >> "))
        print("="*80)# line
        print("                       AMORTIZATION SCHEDULE                             ")
        print("="*80)# line
        cal = Amortization_Schedule (L,R,T)
        n = cal.calculation()
    except ValueError:
                print("Enter integer/Something is wrong with program")
    ("="*80)# line

#==========================================THE END==========================================
#     @IKpixels-2018    
