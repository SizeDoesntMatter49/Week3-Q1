'''
Help store by creating Python function compute the change using the least numbers of
coins/bills.
Assume that the values are in full baht only and the possible coins/bills are 1, 5, 10, 20, 50, 100,
500, 1000 baht per coin/bill.
'''

# Student do quiz here below
# do not change the function name
# do not change the function input

def ChangeCalculator(price ,paid ):
    if isinstance(paid, str) or isinstance(price, str) or isinstance(paid, float) or isinstance(price, float):
        return "ERROR"
    torn = paid - price
    if paid < 0 or price < 0:
        return "ERROR"
    if torn >= 0:
        PanTorn = torn // 1000
        torn = torn % 1000
        HarRoiTorn = torn // 500
        torn = torn % 500
        RoiTorn = torn // 100
        torn = torn % 100
        HarSipTorn = torn // 50
        torn = torn % 50
        YeeSipTorn = torn // 20
        torn = torn % 20
        SipTorn = torn // 10
        torn = torn % 10
        HarTorn = torn // 5
        torn = torn % 5
        NuengTorn = torn // 1
    else:
        return "ERROR"
    Ans = [PanTorn,HarRoiTorn,RoiTorn,HarSipTorn,YeeSipTorn,SipTorn,HarTorn,NuengTorn]
    return Ans
print(ChangeCalculator(20,20))
