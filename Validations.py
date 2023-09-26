#Validation for Number
def isNumberValid(str):
    if len(str)==10:
        if str.isdigit():
            return True
        else:
            return False
    else:
        return  False


#Validation for Name
def isNameValid(str):
    l=str.split()
    for i in l:
        if (not i.isalpha()):
            return False
    return True

#Validation for PAN
def isPanValid(str):
    if len(str)==6:
        s1=str[0:3]
        s2=str[3:]
        if not s1.isalpha():
           return False
        if not s2.isdigit():
            return False
        return True
    else:       
            return True
        

#Validation for Bank Name
def isBankNameValid(str):
    l=str.split()
    for i in l:
        if (not i.isalpha()):
            return False
    return True

#Validation for IFSC Code
def isIFSCValid(str):
    if len(str)==11:
        a1=str[0:4]
        a2=str[4:7]
        a3=str[8]
        a4=str[9:]
        if not a1.isalpha():
            return False
        if not a2.isdigit():
            return False
        if not a3.isalpha():
            return False
        if not a4.isdigit():
            return False
        return True
    else:
	    return True
    

#Validation for Gender Code
def isGenderValid(str):
    if str=='Male':
        return True
    if str=='Female':
        return True
    if str=='Others':
        return True
    return False


#Validation for Aadhar Card
def isAadharValid(str):
    if len(str)==12:
        if str.isdigit():
            return True
        else:
            return False
    else:
        return  False
    
#Validation for DOB
def isDOBValid(str):
        if len(str)==10:
            q1=str[0:2]
            w=str[2]
            q2=str[3:5]
            e=str[5]
            q3=str[6:10]
            if len(q1)==2:
                if q1.isdigit():
                    return True
                if '-' in w:
                    return True
                if len(q2)==2:
                    return True
                if '-' in e:
                    return True
                if q3.isdigit():
                    return True
            return False
        else:
            return False    
                 

            


