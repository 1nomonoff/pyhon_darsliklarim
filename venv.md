agarda sz linux yoki macbook operation tizim ishlatsez va 
terminalda venv yaratgan keyin uni aktive qilish uchun :

    source venv/bin/activate

komandasini terasiz va terminal boshida (venv) sozi paydo boladi 

agarda :
    rm -rf venv 
deb venv ni ochirsez 
    deactivate
db venvni faolsizlantirish kerak 
-----------------------------------------------------------------

pythonda projectlarni saqlovchi xonalarni ochish uchun (bin , lib ........) : 

    python -m venv venv 
----------------------------------------------------------------------------
agar siz windows ishlatayotgan bo'lsangiz va powershell yoki cmd dan foydalansangiz
venv active gilish uchun
venv/Scripts/activate buyuruqdan foydalanasiz
"ve" degan so'zni yozib tap "sc" yozib yana tap "ac" yozib yana tap ni bossangiz o'zi
yozib beradi yani terminalda to'ldirib beradi.
------------------------------------------------------------------
agar siz windowsda va git bash bilan ishlayotgan bo'lsangiz
unda siz
source venv/Scripts/activate
komandasini terasiz va shu bilan venv active gilasiz.