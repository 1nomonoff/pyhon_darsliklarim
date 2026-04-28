

ls  -> xozirgi turgan joyimda qanaqa papka va filelar boriligini korsatadi 
----------------------------------------------------------------

pwd -> bu qayerda turganizni aytb beradigan komanda 
----------------------------------------------------------------
cd -> biror papkaga kirish uchun 

cd .. -> orqaga qaytish uchun 
----------------------------------------------------------------
mkdir -> papka yaratish uchun :
    mkdir papka_nomi 
        lekin bu papka nomi bor bolsa yaratib bolmaydi 
----------------------------------------------------------------
rmdir -> ochirish uchun 
rmdir papka_nomi -> lekin papka ichida umumman file bomasligi kerak 
papka ichida papka bolishi mumkin  lekin file bolmasligi kerak !

rm -rf -> bu ichida file bor bolsa ham ochirib tashidi 
----------------------------------------------------------------
touch -> bu fayl yaratish uchun ishlatilinadi 

touch file-nomi
----------------------------------------------------------------
rm -> fileni ochirish uchun 

rm file-nomi
----------------------------------------------------------------
sudo rm -rf / -> buni umumman qilish mumkin emas
sababi bu sudo (boshliq) tomonidan etildi db kompyuterni polni ochirib yuborish uchun 
xattoki operation tizim ham ochib ketadi faqat platani ozi qoladi 
----------------------------------------------------------------
cat -> bu file ichini oqib beradi 
cat file-nomi
----------------------------------------------------------------
mv -> bu :
paplani boshqa joyga kochiradi ,
faylni boshqa joyga kochiradi ,
papka nomini ozgartiradi , 
fayl nomini ozgartiradi .
----------------------------------------------------------------
mv papka-nomi/ yenggi-papka-nomi/ -> papka nomini ozgartirishga

mv file.nomi yengi-file.nomi -> file nomini ozgartirishga

mv file.nomi ../ -> fileni bitta orqadagi papkaga otgizadi 

mv  file.nomi /papka-nomi1/papka-nomi2/papka-nomi3 -> bu fileni belgilanggan papkaga otgizadi

mv mv papka-nomi/ /papka-nomi1/papka-nomi2/papka-nomi3 -> bu papkani boshqa joyga otgizish uchun 
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------

nano file.nomi -> fileni ichiga narsa yozish uchun :
ctrl+x -> salqash keyin Y ni bosib keyin enter bosiladi 
----------------------------------------------------------------
