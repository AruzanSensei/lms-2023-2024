from flask import Flask, render_template, request, jsonify
import random
import os
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

class LMS_data:
    @staticmethod
    def X_DKV_I():
        kelas = [
    ["Ade Solehudin", "232410257", "c58778"],
    ["AFINA RIZWANTI SUNGKAWA", "232410258", "3bcf62"],
    ["AGI FANSYAH SYAHIDIN", "232410259", "46c7f6"],
    ["ALFATHIR SYAHWALL", "232410261", "150d5a"],
    ["AL`MAIDA VIOREINS DINA", "232410260", "b9e1ca"],
    ["AMANAHTAN MUHAIMIN", "232410262", "59bb0d"],
    ["ANGGI LISDIAN WIGUNA", "232410263", "88b671"],
    ["ANISA AULIA", "232410264", "57a153"],
    ["ARMAN AR RAHMAN", "232410265", "f459a0"],
    ["AYU FASA RAMDANI", "232410266", "b2ae88"],
    ["DAFFA ARDABILLY", "232410267", "5cc87f"],
    ["DESI", "232410268", "b08e31"],
    ["DIMITRA WIBISONO", "232410269", "f89fb6"],
    ["FADLI AZAHRA", "232410270", "af73a6"],
    ["FARID ABDUL RAHMAN", "232410271", "604def"],
    ["HAFIZ ZAKWAN", "232410272", "b0a626"],
    ["Intan Ali", "232410273", "6400a5"],
    ["IQBAL ABILLAL HALINTAR", "232410274", "003fd9"],
    ["KHAYRI TAFAZZUL AMIN", "232410275", "7e615b"],
    ["MEGA SRI RAHAYU", "232410276", "bac50a"],
    ["MEYLANI PUTRI", "232410277", "e7a818"],
    ["Muhamad Eka Satria", "232410278", "f65f05"],
    ["MUHAMAD FAREL ALGOJALI", "232410279", "a38b19"],
    ["MUHAMMAD DAFFA", "232410280", "2743f5"],
    ["NANDANA NAFIS", "232410281", "6c1ed2"],
    ["NENG ZAHRA", "232410282", "b821f8"],
    ["RAJA MANGGALA BUANA", "232410283", "b908eb"],
    ["RANI CAHYADEWI", "232410284", "5d2072"],
    ["RENDI TRI WIDIYANTO", "232410285", "0d699c"],
    ["RIZKI ANDRIANSYAH", "232410286", "813509"],
    ["SAILA APRILA", "232410287", "4ab56c"],
    ["SALSABILA RAMADHANI", "232410288", "a2f699"],
    ["SATRIA SYAHRUL RAMADHAN", "232410289", "ea568c"],
    ["SILVIA RAMADANI", "232410290", "b34714"],
    ["SUCI AMELIA RAHMADANI", "232410291", "517a18"],
    ["UDRI LUKMAN WIJAYA", "232410292", "53c250"],
    ["YUNDA AGUSTIAN PUTRI", "232410293", "4905b3"]]
        panjang = len(kelas)    
        return kelas, panjang
    
    @staticmethod
    def X_DKV_II():
        kelas = [
    ["ADITIA RAHMAN", "232410294", "5f59ab"],
    ["Aghni Febriani", "232410295", "a23296"],
    ["AHMAD FARIS MARLIANSYAH", "232410296", "74afa3"],
    ["ALVIANSYAH HABIB", "232410297", "67bd2f"],
    ["AMANDA ROINA", "232410298", "ff4fdf"],
    ["ANANDA RESTU GUSTI", "232410299", "2b8602"],
    ["ANGKASA RAYA NURANDI", "232410300", "dd7ee4"],
    ["Aprilia Kholilah", "232410301", "1233d9"],
    ["BIMA IBNU FADILLAH", "232410302", "2868e1"],
    ["CHIKA AULIA", "232410303", "f000a5"],
    ["DAFVA ALFARIZQI RAMADHAN", "232410304", "14316f"],
    ["EKI RIZALDI", "232410305", "c6eb68"],
    ["FAHRI ANDRIANSYAH", "232410306", "58cd19"],
    ["FAIRUZ GHINA RAMADHAN", "232410307", "453df3"],
    ["FERDY RAHADIAN PUTRA", "232410308", "4e1d5a"],
    ["HAIKAL SAPUTRA", "232410309", "b41842"],
    ["KESYA APRILIA", "232410310", "9efd21"],
    ["KSATRIA CANDRA GUMILANG", "232410311", "7bdac1"],
    ["M LUTFI ZIDAN SYAPUTRA", "232410312", "17a7df"],
    ["MIA AZKIA ZAHRA", "232410313", "cf8f35"],
    ["MUHAMAD AGUNG GUMELAR", "232410314", "bf83f7"],
    ["MUHAMAD ELTA PAHRIAN", "232410315", "513974"],
    ["MUHAMMAD FADILAH MUBAROQ", "232410316", "c7e954"],
    ["NUNI NURIYANTI", "232410317", "ca0216"],
    ["Raditya Alhafis Putra Mulya", "232410318", "849ee8"],
    ["RADITYA PUTRA", "232410319", "1fe17a"],
    ["RAKA WANDIHAZATI", "232410320", "e81528"],
    ["RATU FUJIYANTHI", "232410321", "fb2b70"],
    ["REZA FAQIH FADILAH", "232410322", "33af0f"],
    ["RIZKY RIAN SASMITA", "232410323", "b2f000"],
    ["SALMA SETIA RAHMADHANI", "232410324", "efe758"],
    ["SALWATUNNISA", "232410325", "392260"],
    ["Siti Nadiatul Almu Airoh", "232410326", "4f0aaa"],
    ["Sultan Pardiansyah", "232410327", "9df1c2"],
    ["Triana Ayu Ningtyas", "232410328", "747cbd"],
    ["Zahra Khairani", "232410329", "d2d39a"]]

        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_DKV_III():
        kelas = [
    ["ADITIA RIZKIA", "232410330", "986940"],
    ["Al Fachri Solehudin", "232410331", "ef7498"],
    ["ALIKA AIKAILA RAHMAN", "232410332", "4ab3ef"],
    ["ALVITODEKA", "232410333", "4df396"],
    ["ANDHIKA YUSUF", "232410334", "568d59"],
    ["ARFA ABDULLAH", "232410335", "ae77e1"],
    ["ASHILA MEIDA AZ-ZAHRA", "232410336", "9b6603"],
    ["BUDI SANTOSO KELANA", "232410337", "aae256"],
    ["BUNGA RAMADANI HAKIM", "232410338", "b42a3a"],
    ["DIMAS AFRIYANSAH", "232410339", "d79f6e"],
    ["EZRA RAFA SETIAWAN", "232410340", "0e055a"],
    ["FAIRUZ SAEFUL MAHASIN", "232410341", "91cc37"],
    ["FERY YATNA MULYA", "232410342", "26e4cf"],
    ["FIONA DESWITA", "232410343", "8d7aae"],
    ["HANIFA KODIR ZAELANI", "232410344", "825d95"],
    ["KHAIRUL SYIFA", "232410345", "1fa5d9"],
    ["Lala Damayanti", "232410346", "6a57b3"],
    ["M GALIH GUMELAR", "232410347", "393602"],
    ["MELINDA LUTFIAH", "232410348", "b5f7c7"],
    ["MUHAMAD AKMAL RAZIQ", "232410349", "0fecb8"],
    ["MUHAMAD SHAFA ABDILLAH", "232410350", "e316ea"],
    ["MUHAMMAD FADHILAH", "232410351", "73fba7"],
    ["MUHAMMAD FAUZAN", "232410352", "416243"],
    ["NAYLA ZAHRANI", "232410353", "77a24d"],
    ["PUTRI GUSTIANINGSIH", "232410354", "ac5dd4"],
    ["RAHYANDI SUKMANA PRADITYA", "232410355", "475ba9"],
    ["RAKEAN RUDRA WIWAHA", "232410356", "317787"],
    ["REVA AURORA", "232410357", "18df2e"],
    ["RIAN APRIANSYAH", "232410358", "a9e7b9"],
    ["SAHRUL RAMDONI", "232410359", "4a253b"],
    ["SALSA DESTIANA", "232410360", "553de7"],
    ["SANDRINA BILQIS ZAHROTUSYTA", "232410361", "d6bb3d"],
    ["SRI AYU WULANDARI", "232410362", "3fbda3"],
    ["ULANDARI", "232410363", "8c1e95"],
    ["ZAHROTU SYAPARUDIN", "232410364", "2570c3"],
    ["ZURIANI PUTRI", "232410365", "d47424"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_I():
        kelas = [
    ["ABDUL LATIP", "232410001", "7685d7"],
    ["ACIH", "232410002", "53f44f"],
    ["Agung Prasetyo", "232410003", "853eec"],
    ["ALWI PUTRA DWI AKBAR", "232410004", "801f24"],
    ["AMANDA DAMAYANTI", "232410005", "6c7a22"],
    ["APRIL BAGUS PAKERTI", "232410006", "06add9"],
    ["Astri Okta Riani", "232410007", "f719bd"],
    ["Beto Satriana", "232410008", "b42f78"],
    ["CHELSI ARUMI FITRIANI", "232410009", "fb4dcf"],
    ["DERA PARLISA", "232410010", "4f2755"],
    ["DIDIN HAERUDIN", "232410011", "02bd10"],
    ["ELSIANA FEBRIYANTI", "232410012", "4581a7"],
    ["FAHRI GUNTUR JAYA WIJAYA RAHMATULLOH", "232410013", "f785bc"],
    ["FERDY HERDIANSYAH PRATAMA", "232410014", "4d8ad7"],
    ["IKBAL", "232410015", "a4fc61"],
    ["JUHAMI WIDIANTINI", "232410016", "4c706f"],
    ["KURNIAWAN HERDIANSAH", "232410017", "e30f1c"],
    ["Marsel Oktapiansah", "232410018", "13c591"],
    ["MAURA AISYA KAMIL", "232410019", "ad4683"],
    ["MUHAMAD AMRI", "232410020", "279067"],
    ["MUHAMAD FAUZI", "232410021", "e5e5b1"],
    ["MUHAMAD RAFLI ALFIAN", "232410022", "ce971f"],
    ["MUHAMMAD AZFA AL MUZAYYIN", "232410023", "fc59b1"],
    ["MUHAMMAD REZA PUTRA PRATAMA", "232410024", "4d7d22"],
    ["Nabila Agustina", "232410025", "9233cf"],
    ["NISA TABELA", "232410026", "6e5158"],
    ["NOUVAL AHMAD MUTTAQIN", "232410027", "9a39ef"],
    ["PIRA NUR ASYIFA", "232410028", "abcf69"],
    ["RAHMA WATY", "232410029", "5873ee"],
    ["REJA MAULANA", "232410030", "e98943"],
    ["REVI MUAWANAH", "232410031", "ecf510"],
    ["RIZKI", "232410032", "95fbe1"],
    ["SANDIY ROMANSAH", "232410033", "315af5"],
    ["Sheina Hafizatu Zahra", "232410034", "9acfaf"],
    ["SITI NAZWATU ILMAH", "232410035", "d23f7a"],
    ["TESSA SALSABILAH", "232410036", "6e3bf1"],
    ["YUNITA", "232410037", "cf95e0"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_II():
        kelas = [
    ["ABIDZAR RACHMAT KHAIRAN", "232410038", "acb743"],
    ["Adinda", "232410039", "fa9a50"],
    ["AHMAD RIFA`I", "232410040", "b3f2a3"],
    ["AMELIA FUTRI", "232410041", "2d0d2a"],
    ["ANANDA DWI PUTRA HERMAWAN", "232410042", "86ba29"],
    ["APRILA SETIO", "232410043", "57bb7e"],
    ["AULIA WIJAYANTI", "232410044", "d03712"],
    ["CHOLIPAH NUR", "232410045", "2bb521"],
    ["Daffi Ahmadansyah Putra", "232410046", "650c69"],
    ["DESY", "232410047", "262752"],
    ["DWI ANGGORO", "232410048", "3f3259"],
    ["FAHSYA NURHAILIKA", "232410049", "f153fd"],
    ["FANI APRILIANI", "232410050", "f47b14"],
    ["GEMA MAHARDIKA DRAJAT", "232410051", "012239"],
    ["IPAN", "232410052", "912c4b"],
    ["JULIA MANDARISKA", "232410053", "b26dfa"],
    ["M ERLANGGA SEJAHTERA", "232410054", "19af27"],
    ["MAYADA QURROTU AINI", "232410055", "370859"],
    ["MOCH PURNAMA AJI", "232410056", "ba1019"],
    ["MUHAMAD ANDRA KURNIAWAN", "232410057", "02c6ce"],
    ["MUHAMAD HAFIZ AL FAZRI", "232410058", "11af2e"],
    ["MUHAMAD RAIPAL ROBBANI", "232410059", "cc2ec3"],
    ["MUHAMMAD FACHRI APRIYONO", "232410060", "7373d1"],
    ["MUHAMMAD RIZAN FADILLAH", "232410061", "7ccd8b"],
    ["Nabila Rahma", "232410062", "173d84"],
    ["NONA SRI DERIANTI", "232410063", "a8716b"],
    ["NOVAL ZASUA SAPUTRA", "232410064", "28842b"],
    ["PRITA LIDIANA", "232410065", "a840b1"],
    ["RAYSHA KARIMAH HERDANI", "232410066", "6f6d2a"],
    ["RENDIANSYAH ABDILAH", "232410067", "fa90a3"],
    ["RIAANA ASSITA RAHMAN", "232410068", "54aab7"],
    ["RIZKI BAGASTA HIDAYAT PUTRA", "232410069", "06265a"],
    ["SHEINA MASRINA PERTIWI", "232410070", "cd4df3"],
    ["SITI NURAISAH", "232410071", "d8b4bd"],
    ["SUGIH PERMANA", "232410072", "41a3ee"],
    ["Trias Saputri Nurul Aulia", "232410073", "b7122b"],
    ["ZAHRATUSITA", "232410074", "114274"]]
        panjang = len(kelas)
        return kelas, panjang

    @staticmethod
    def X_AGRI_III():
        kelas = [
    ["ADE", "232410075", "0c9dc2"],
    ["ADINDA AMALIA PUTRI", "232410076", "0217cb"],
    ["AKSHAL MEILANDRY DAFAREL", "232410077", "d745e1"],
    ["ANANDA FUJIAH ISTIKOMAH", "232410078", "f61567"],
    ["ANDI ANANDA SAPUTRA", "232410079", "649bbb"],
    ["ANIS FADILAH", "232410080", "d924a7"],
    ["ARGA ARULIA HADI", "232410081", "cb3ac8"],
    ["BUNGA SITI AZIZAH", "232410082", "80e9ba"],
    ["CINTA PEBRIANI", "232410083", "8d751b"],
    ["DANI SEPTIANA", "232410084", "2be3c0"],
    ["DESTIANA NUR FADILLAH", "232410085", "3c4723"],
    ["EGI FIRMANSYAH", "232410086", "3d37b5"],
    ["FAISAL ADE PUTRA", "232410087", "7a5580"],
    ["FEBRI AISAH SOPIYAN", "232410088", "0b4883"],
    ["GILANG ANGGARA", "232410089", "bcb1e5"],
    ["IQBAL AJI UTAMI", "232410090", "2bce79"],
    ["KEYLA ADISTI", "232410091", "94a967"],
    ["M RIFAN PEBRIAN", "232410092", "212e44"],
    ["M SANDY RIJALDY", "232410093", "dcdfea"],
    ["MOHAMAD AZTADES PAPARAZI ALBANI", "232410094", "712517"],
    ["Muhamad Arief Chandra Budiman", "232410095", "13763e"],
    ["MUHAMAD HAIKAL HALIM", "232410096", "30073a"],
    ["MUHAMAD RAPI ALPAYAT", "232410097", "29f280"],
    ["MUHAMMAD FARID", "232410098", "f3036c"],
    ["NADIA PUTRI", "232410099", "c8727c"],
    ["Nova", "232410100", "a66589"],
    ["NURCA PASHA", "232410101", "f5fa18"],
    ["PUTRI ALMIRA", "232410102", "e44164"],
    ["REFA", "232410103", "13077d"],
    ["RESYA PUTRA SATRIANA", "232410104", "e25e03"],
    ["RIMA YUHILSA", "232410105", "7c0cde"],
    ["RIZKI INDA ROBBI", "232410106", "0f5a99"],
    ["SILVIA NAZYLA FRIESCA", "232410107", "d1d3f4"],
    ["SITI NURLELA", "232410108", "b19faf"],
    ["SURGA AUREL GIFARI", "232410109", "8cd984"],
    ["TRISANIDA MARIAM AYU PRATIWI", "232410110", "97c7be"],
    ["ZASKIA CAHAYA PUTRI", "232410111", "3ecf23"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_IV():
        kelas = [
    ["Ade Baharudin Kamal", "232410112", "ea1dc5"],
    ["AGNIA BILQIS NURSYAMBA", "232410113", "c3c370"],
    ["ALDI HARDIANSYAH", "232410114", "b3c6ee"],
    ["ANDIKA MAULANA", "232410115", "157430"],
    ["ANDINI AULIA NINGSIH", "232410116", "2e5047"],
    ["ARIP", "232410117", "1c398a"],
    ["CAHYA RAHMAYANTI", "232410118", "07af8e"],
    ["CHINTYA MAULIDA LESTARI", "232410119", "cd9338"],
    ["DELPIN", "232410120", "b41f42"],
    ["DEVI MEYDINA", "232410121", "64c4b8"],
    ["ENDANG KURNIAWAN", "232410122", "521f32"],
    ["FAISAL RAMA AKBAR", "232410123", "3192c8"],
    ["GUNAWAN", "232410124", "68b87b"],
    ["INDIRA PUTRI SOFY", "232410125", "1b5582"],
    ["IRGI ANDIKA", "232410126", "8a4450"],
    ["KIRANA ALFIANI", "232410127", "6f1aae"],
    ["M PAJAR KOSASIH", "232410128", "cee611"],
    ["MELSI", "232410129", "d8bb82"],
    ["MUARA BAYU FIRDAUS", "232410130", "9e6f17"],
    ["MUHAMAD FADLI", "232410131", "ce0fda"],
    ["MUHAMAD MISBAHUL ALAM", "232410132", "ef924d"],
    ["MUHAMAD RIDO FAIZAL", "232410133", "7e7209"],
    ["MUHAMMAD HASBI ARRUZI", "232410134", "4b8c7b"],
    ["MUHAMMAD SATRIA ABABIL", "232410135", "c52d16"],
    ["NAHLA KAYLA RIDWAN", "232410136", "b57644"],
    ["NOVANY ASHKA NABILA", "232410137", "192e30"],
    ["PAISAL MAHMUD", "232410138", "69d6e3"],
    ["PUTRI CINTA BAKTI", "232410139", "59b7dc"],
    ["RENI", "232410140", "7d77fe"],
    ["Ridho Afrizani", "232410141", "f32c69"],
    ["RINANDA AULIA RIZQI", "232410142", "6f66ca"],
    ["ROBI DWIJULIANTO", "232410143", "983825"],
    ["SITI FATIMAH ZAHRA", "232410144", "c24343"],
    ["SITI RAISYAH PUTRI", "232410145", "1e0d72"],
    ["UDAY AWALUDIN", "232410146", "c1455f"],
    ["USMARRAFI ROSA SANJIA", "232410147", "3e6bd7"],
    ["VEBBY ADELLA", "232410148", "552eef"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_V():
        kelas = [
    ["AEP", "232410149", "f756ec"],
    ["ALDI MUHAMAD USMAN", "232410150", "49bc43"],
    ["ALIFAH KHAIRA FIRDAUS", "232410151", "4ba84c"],
    ["ANDIKA PUTRA PRATAMA", "232410152", "c8ab1a"],
    ["ANDINI OKTAVIANI", "232410153", "85e10a"],
    ["ARUL IRWANSYAH", "232410154", "a58e56"],
    ["Cantika Asyifa Edystia", "232410155", "9fc95b"],
    ["Dea Talita", "232410156", "d754e0"],
    ["DENI", "232410157", "48f249"],
    ["DIANA SABRINA", "232410158", "c82ef6"],
    ["EZAR AL- MUGHNI", "232410159", "4bf308"],
    ["FARIZAL ISTIHORI", "232410160", "8c84fa"],
    ["HARDIYANSYAH", "232410161", "cd8038"],
    ["INTAN SUSWANTO PUTRI", "232410162", "8dd944"],
    ["IRPAN", "232410163", "5ff999"],
    ["KIRANA ANJEL", "232410164", "5fc48c"],
    ["M. PAHRU ROJI", "232410165", "878a08"],
    ["MILAH KARLINA", "232410166", "31cb61"],
    ["MUHAMAD AGUNG SURYA LESMANA", "232410167", "cf3bab"],
    ["MUHAMAD FAHMI MUZAKY", "232410168", "0cd2cf"],
    ["MUHAMAD PARHAN ALPARIS", "232410169", "7cb3cc"],
    ["MUHAMAD RIDWAN MAULANA", "232410170", "7c9c8a"],
    ["MUHAMMAD HENDI BACHTIAR", "232410171", "6a163a"],
    ["Nabil Agustian", "232410172", "d5274c"],
    ["NASYA SILVANA", "232410173", "99802f"],
    ["NUR ALIFAH", "232410174", "9b8e7d"],
    ["PUTRI NUR LEDIYA", "232410175", "36ad8a"],
    ["RAFAEL NUR RIZQ", "232410176", "aa8321"],
    ["RESTIYANTI CAHYANI NASOLIHIN", "232410177", "70d7b3"],
    ["RIDHO MAULIDAN", "232410178", "1a7369"],
    ["RUDI ALFARIZKI", "232410179", "f7e238"],
    ["SELA MARSELIA", "232410180", "a012c0"],
    ["SITI MARIA", "232410181", "037e41"],
    ["SITI RUKMANA", "232410182", "056825"],
    ["VIRLI PRASETIA", "232410183", "3aa4e9"],
    ["VITA NABIL MUFLIHAH SAHERTIAN", "232410184", "23e7c3"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_VI():
        kelas = [
    ["AFRILLIAN", "232410185", "9b04a5"],
    ["ALDO MUHAMAD USMAN", "232410186", "a57457"],
    ["ALIFIA SEPTIANI PUTRI", "232410187", "1796c8"],
    ["ANGGI", "232410188", "8376cf"],
    ["ANNISA NUR SYAHVIRA", "232410189", "69ba84"],
    ["ARYO RAMADANI", "232410190", "abd58b"],
    ["CECILIA CITRA APRILIANI", "232410191", "709430"],
    ["DENIA PEBRIANTI", "232410192", "e0228c"],
    ["DEVA ANANTA", "232410193", "a7efb4"],
    ["DINDA NUR AULIA", "232410194", "c29456"],
    ["Fachry Indriawan Rizky Pratama", "232410195", "115157"],
    ["Fauzan Amarullah", "232410196", "b4f9c4"],
    ["HENDRA W", "232410197", "d5367c"],
    ["IRMA DAMAYANTI", "232410198", "15bb65"],
    ["JALALUDIN", "232410199", "1a52a8"],
    ["LARAS SATI", "232410200", "f1bb1f"],
    ["M. RIZKI", "232410201", "cc0cb0"],
    ["Mita Anastasya", "232410202", "37da45"],
    ["MUHAMAD ALFATHIR FEBIAN", "232410203", "d0b0d9"],
    ["MUHAMAD FAIZAL", "232410204", "aaa689"],
    ["MUHAMAD PRADIPTA AL BAZY", "232410205", "d8807f"],
    ["MUHAMAD SAEPULLOH", "232410206", "59214a"],
    ["MUHAMMAD IHSAN PAJRIL", "232410207", "8258e0"],
    ["NANDA FIRDAUS", "232410208", "3a13de"],
    ["NENENG MARDIANA", "232410209", "98e697"],
    ["NURAENI", "232410210", "85fd74"],
    ["QINANTYA ANKIESTI", "232410211", "82cd37"],
    ["RAPI RAMADANI", "232410212", "4ff037"],
    ["REVA MARINA", "232410213", "f61c86"],
    ["RUDIANSYAH", "232410214", "042655"],
    ["SEPTI RAMDANIA", "232410215", "ff81fb"],
    ["SITI MASITOH", "232410216", "d43abb"],
    ["SUCI AGISNI", "232410217", "8264e7"],
    ["WAFFA VIQRAH", "232410218", "d2a499"],
    ["WAHYU ILAHI", "232410219", "bf60fd"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def X_AGRI_VII():
        kelas = [
    ["AFRIZAL FAHREZI", "232410220", "f10d7c"],
    ["ALIP RAMADANI", "232410221", "24e9f6"],
    ["AMANDA", "232410222", "5817f9"],
    ["ANGGI SATRIA", "232410223", "679d97"],
    ["APIPAH RADWA", "232410224", "94d541"],
    ["ASEP SOPIAN", "232410225", "ff68f7"],
    ["CHELSA ALFA FITRIANA", "232410226", "bd5bbc"],
    ["DERA AINUN MAHYA", "232410227", "5e76dd"],
    ["DIANSAH", "232410228", "7ec288"],
    ["DWI AYUNITA SARI", "232410229", "70b44d"],
    ["FAHREZI PUTRA HIDAYAT", "232410230", "b67501"],
    ["faris Fauzan Syamsu", "232410231", "d29db7"],
    ["Febri Ade Haerudin", "232410232", "bb321b"],
    ["Hendrik Sandika", "232410233", "6d83f2"],
    ["ISKA SRI OKTOVIA", "232410234", "da7f1d"],
    ["KARNA RAHMADANI", "232410235", "2b83d7"],
    ["LULU DESTIANI", "232410236", "7bec06"],
    ["M. ZIDAN AZRIL", "232410237", "f6b5c2"],
    ["Muhamad Alfiansah", "232410238", "ae4fd0"],
    ["MUHAMAD FAREL", "232410239", "98301f"],
    ["MUHAMAD RAFI AL-RACMAN", "232410240", "b6d6f7"],
    ["MUHAMMAD ALDI YANSYAH", "232410241", "b66512"],
    ["MUHAMMAD NAZMA ALKARIMI", "232410242", "7a1277"],
    ["MUTIA ISTIQOMAH", "232410243", "3c61d5"],
    ["NAUFAL PUTRA WISNANDA", "232410244", "7f3e72"],
    ["NEZZA NUR APRIANI", "232410245", "92d6ab"],
    ["PINANDA AYU LESTARI", "232410246", "44cb4b"],
    ["RAHAYU SRIYUNINGSIH", "232410247", "4243f3"],
    ["REFFI ARDIANSYAH", "232410248", "cb6585"],
    ["REVA RIPTIA", "232410249", "e7c096"],
    ["RISKI ALPIANSAH", "232410250", "5cbb88"],
    ["SAEPUL MA`RIF", "232410251", "a520d1"],
    ["Serli", "232410252", "ea20d6"],
    ["SITI MAY MUNAH", "232410253", "8a1052"],
    ["TASYA NURHALIZA", "232410254", "28128e"],
    ["YANA SUPRIYATNA", "232410255", "e328bd"],
    ["YUNI", "232410256", "de9657"]]

        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_DKV_I():
        kelas = [
    ["Adam Fauzan Rustandi", "222310282", "429ba0"],
    ["Aditia Hidayat", "222310248", "636437"],
    ["Ahmad Yahya Saprudin", "222310317", "b1f610"],
    ["Alma Hilmatunisa", "222310284", "62dff1"],
    ["Andika Faturrahman", "222310285", "8929cc"],
    ["Angga Ryan Aditama", "222310319", "cdd9a3"],
    ["Arya Aditya", "222310287", "637771"],
    ["Azka Nur Annisa", "222310321", "ba2634"],
    ["Bagus Prasetio", "222310288", "257ff0"],
    ["Chaezarani", "222310289", "5755b1"],
    ["Dela Nazifa Fedia Rasya", "222310323", "2bec10"],
    ["Handika Putra Pratama", "222310327", "97d69d"],
    ["Hoirul Huda", "222310328", "abf6b5"],
    ["Ibnu Malkan", "222310259", "51c131"],
    ["Ika Rahmawati", "222310295", "2b71a8"],
    ["Lisda Usmayanti", "222310261", "1fdf2d"],
    ["Lucky Aditya", "222310297", "d11044"],
    ["Luna Ramadhani", "222310331", "468ae1"],
    ["Manya Raisean", "222310298", "40f704"],
    ["Miftahul Hasanah", "222310263", "3059c5"],
    ["Muhamad Farhan Haikal", "222310300", "3e8a4c"],
    ["Muhamad Ridho Andrian", "222310334", "238548"],
    ["Muhamad Surya", "222310265", "3e5d07"],
    ["Muhammad Ibnu Abdillah", "222310267", "c24af8"],
    ["Muhammad Jihad Sholihin", "222310303", "c83ed0"],
    ["Nanda Alevia", "222310340", "594d9a"],
    ["Nurmala", "222310342", "b6f4f8"],
    ["Raihan Maulana", "222310274", "fa30e4"],
    ["Riuh Nabil", "222310347", "f9d454"],
    ["Riza Ahmadinejad", "222310277", "bb469d"],
    ["Silva Septiani", "222310278", "6f2f88"],
    ["Sri Dewi Siti Sarah", "222310279", "1a50b6"],
    ["Tegar Efin Munajat", "222310350", "d4f7b4"],
    ["Turhama Kholifatullah Rojjabi Supriadi", "222310280", "9de920"],
    ["Zikri Maulana", "222310315", "7415f3"]]
        
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_DKV_II():
        kelas = [
    ["Abdul Azis An Nauval", "222310247", "6514f7"],
    ["Alvin Tegar Permana", "222310318", "fc1958"],
    ["Arief Ramadhan Firmansyah", "222310320", "530c99"],
    ["Arsekal Ainuridho", "222310252", "a23f87"],
    ["Bagas Sabda Galih", "222310253", "a9fe1d"],
    ["Diaz Ayu Lestarie", "222310254", "ffca1b"],
    ["Ezzar Fachry Ramadhan", "222310290", "24bf2b"],
    ["Farel Meidentri", "222310325", "a8de8f"],
    ["Fathul Ridzky", "222310292", "8c9e68"],
    ["Galang Ramadhan", "222310293", "48e1b5"],
    ["Hezri Mikola", "222310294", "ae0233"],
    ["Laela Sari", "222310330", "0a4ae8"],
    ["M. Raihansyah", "222310262", "0b8a6b"],
    ["Miko Wijaya", "222310299", "48bca6"],
    ["Mohamad Haikal", "222310333", "1f6a99"],
    ["Muhamad Wildan", "222310301", "756fff"],
    ["Muhammad Abi Fathan", "222310266", "bd57c7"],
    ["Muhammad Fadlillah", "212210339", "79c3b1"],
    ["Muhammad Kafka Abigail Cai Sarian", "222310338", "81d6fa"],
    ["Muhammad Rizki Awal Ramadhan", "222310268", "dde959"],
    ["Mutiara Jenar Komala Intan", "222310304", "25561e"],
    ["Nadia Ulfah", "222310339", "a353a8"],
    ["Naufal Aziz Dliyaaulhaq", "222310270", "a24404"],
    ["Neyla Putri Ramadhani", "222310341", "b90da2"],
    ["Nur Cahya Puspita", "222310306", "40c9c7"],
    ["Nurul Fadilah", "222310272", "f7fac0"],
    ["Puput Cahyani", "222310343", "5c1358"],
    ["Putri Yani Agustin", "222310307", "957834"],
    ["Ridho Rafa Airlangga", "222310309", "be5a46"],
    ["Rifqi Alfiansyah", "222310276", "ce655d"],
    ["Riji Yustaf Al Fariji", "222310346", "19054a"],
    ["Shilah Wahiddatul Barokah", "222310311", "de9a61"],
    ["Silva Amanda", "222310348", "7b8da9"],
    ["Sophie Andira Putri", "222310349", "8fc997"],
    ["Zaldi Rahman Ramadhion", "222310281", "00d7a1"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_DKV_III():
        kelas = [
    ["Adinda Keysya Putri Lestari","222310316","159699"],
    ["Ahmad Aulia Ramadhan","222310283","312411"],
    ["Alfarabi Putra Sudrajat","222310249","86cfb9"],
    ["Anissa Aulia Rahma","222310251","312285"],
    ["Alzan Adytia Juniar","1211320","81dcdc"],
    ["Aqsyal Gilang Ramadhan","222310286","d2c8b8"],
    ["Bunga Rischa Namira","222310322","d46711"],
    ["Fabian Putra Hermawan","222310324","7f32ac"],
    ["Fairus Priyogi","222310291","8e74c3"],
    ["Farrel Pratama Putra","222310256","9cc52b"],
    ["Firgy Fahrizy","222310326","059170"],
    ["Fitra Fauzi Akbar","222310257","887d7e"],
    ["Heru Pratama","222310258","1abf71"],
    ["Jamil Dwi Al Hakim","222310329","cc13b5"],
    ["Khaerul Fahmi","222310260","f1c320"],
    ["Khaesar Suhail Manahan","222310296","bda019"],
    ["Miftah Amarudin","222310332","2b47b6"],
    ["Muhamad Apwani","222310264","cc1217"],
    ["Muhamad Wildan Pratama Hermawan","222310335","059270"],
    ["Muhammad Azhar Alfarizi","222310302","687b00"],
    ["Muhammad Faizillah Dwiki Handriana","222310336","775c99"],
    ["Muhammad Fathurrohman","222310337","8eb6a3"],
    ["Nagita Selviana","222310269","7cdc2c"],
    ["Naila","222310305","34b5a5"],
    ["Ningrum","222310271","df7dc6"],
    ["Putri","222310273","e9f40f"],
    ["Reas Pratama Nasolihin","222310308","82dde5"],
    ["Rendi Maulana","222310344","b9f680"],
    ["Riana Listi","222310275","b563a5"],
    ["Rifa Nurfadila","222310345","c0c59e"],
    ["Rifqi Ramadhani","222310310","c92fe2"],
    ["Siti Rohmah Alhasanah","222310312","c4211d"],
    ["Suhendra","222310313","f954c5"],
    ["Tuti Nurhayati","222310314","e5b1df"],
    ["Vicky Faisal Amir Arrizqy","222310351","c3c7b6"]]
        panjang = len(kelas)
        return kelas, panjang
    @staticmethod
    def XI_APHP_I():
        kelas = [
    ["Aditya Darul Rahman", "222310140", "afa2ea"],
    ["Aulia Putri Utami", "222310179", "e9f916"],
    ["Ayu Ismi Maulida", "222310005", "b73def"],
    ["Daffa Prasetyo", "222310077", "40099f"],
    ["Deli Sri Aprilyani", "222310113", "1df6af"],
    ["Doni", "222310009", "87d610"],
    ["Egar Agustina", "222310079", "7adc41"],
    ["Egi Hermawan", "222310115", "e2b1b5"],
    ["Epan Maulidin", "222310080", "67f14f"],
    ["Fadil Maulana", "222310221", "982adc"],
    ["Fahrul Kusmayadi", "222310047", "1e5f2f"],
    ["Indah", "222310014", "c6cd4d"],
    ["Iqbal Kurniawan", "222310084", "744751"],
    ["Irmayati", "222310153", "c33ce0"],
    ["Irvan Adiyanto", "222310189", "ec4f6c"],
    ["Jamilah", "222310015", "172b7f"],
    ["Maulana Yusuf", "222310124", "17eba4"],
    ["Mohammad Josep Bastian", "222310054", "63f63e"],
    ["Muhamad Elza Gintiana", "222310193", "d3ed1a"],
    ["Muhammad Zaki Rahmat", "222310195", "0fe6fd"],
    ["Otilawati", "222310198", "f1e169"],
    ["Pahri Paturohman", "222310026", "a311af"],
    ["Putri Yuliani Natalia", "222310237", "edccf2"],
    ["Repa Wulandari", "222310134", "f10308"],
    ["Riski", "222310240", "b4f952"],
    ["Septiani Putri", "222310241", "4617c6"],
    ["Siti Khotiroh", "222310032", "dc1776"],
    ["Siti Masitoh", "222310066", "2e9d9a"],
    ["Udan Maulana Razak", "222310104", "eac962"],
    ["Vicka Juwita", "222310173", "89d9bd"],
    ["Yudi", "222310209", "8db87d"],
    ["Yudistira Maulana", "222310174", "0f6da9"],
    ["Yulianti", "222310246", "612f6e"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_APHP_II():
        kelas = [
    ["Aditia Saputra Hidayat", "222310107", "64c3d7"],
    ["Alifa Ananda Putri", "222310073", "e721c6"],
    ["Alpan Putra Oktaviana", "222310177", "98f32a"],
    ["Andika Aminudin", "222310143", "685bed"],
    ["Andri Maulana", "222310004", "2a484f"],
    ["Arien Pratama Putri", "222310041", "51653d"],
    ["Dapa Prediansyah", "222310181", "c363b9"],
    ["Dinda Sabila", "222310219", "0c462b"],
    ["Endriansyah Yoga Pratama", "222310220", "ac326c"],
    ["Enggar Suryadi", "222310010", "d7e6cc"],
    ["Erik Setiawan", "222310116", "88e97a"],
    ["Fathimatuzzahrah Dzulfikri", "222310150", "de6b9a"],
    ["Febriansyah", "222310222", "200ec3"],
    ["Habibah", "222310151", "29d716"],
    ["Herman", "222310188", "2c4225"],
    ["Keyla Lidya Putri", "222310051", "bd3a60"],
    ["Laila Arza Hasifa", "222310122", "b31cb2"],
    ["Lusi Maelani", "222310087", "f13552"],
    ["M. Rauf Aldaru", "222310228", "6a5fa2"],
    ["Muhamad Geraldin Alfijri", "222310020", "6a8c08"],
    ["Muhamad Rizki", "222310021", "e80c95"],
    ["Muhammad Irfan", "222310056", "07bbfb"],
    ["Najla Nurul Fadia", "222310129", "51e417"],
    ["Nani Sutiah", "222310234", "2ed7f8"],
    ["Nazwa", "222310058", "780afd"],
    ["Neman", "222310163", "7090e3"],
    ["Padli Jilikram", "222310236", "aa7ffa"],
    ["Rafli Rahma Wijaya", "222310097", "45da8a"],
    ["Rangga Juliansyah", "222310200", "dbf680"],
    ["Sintia Hermawati", "222310136", "b191ba"],
    ["Tany Danastri", "222310172", "47bb7d"],
    ["Tria Amalia Ramadani", "222310068", "a7a03a"],
    ["Yusril Azis", "222310036", "126a4f"],
    ["Zulfa Fathurohmah", "222310106", "bfdcfe"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_APHP_III():
        kelas = [
    ["Aef Wahyudin" ,"222310176", "34405a"],
    ["Afdhaluddin" ,"222310211", "3c20f1"],
    ["Ahwa Mutiara Hadi" ,"222310355", "efb4b7"],
    ["Alvino Agustian" ,"222310003", "cb3216"],
    ["Amir Riski" ,"222310074", "929424"],
    ["Andika Pratama" ,"222310178", "2d80e8"],
    ["Dede Ardiansyah" ,"222310007", "f7ec7a"],
    ["Delicia Amabel Fangidae" ,"222310358", "9ccb74"],
    ["Deni Muhamad Firmansyah" ,"222310218", "f937e3"],
    ["Dika Agustian" ,"222310114", "9e8802"],
    ["Erza Alamsyah" ,"222310185", "6de31f"],
    ["Muhamad Al Farel" ,"222310089", "7a5f78"],
    ["Muhamad Dzian Ramdani" ,"222310158", "b0a61f"],
    ["Muhamad Rido Ramdani" ,"222310231", "be785f"],
    ["Muhamad Topan Padilah" ,"222310127", "7b0c9e"],
    ["Muhammad Jafar Shodik" ,"222310092", "7ca7f7"],
    ["Muhammad Rhaka Putra Jukardi" ,"222310356", "1b9764"],
    ["Mutia Suci" ,"222310023", "d56348"],
    ["Mutiara Febrianti" ,"222310057", "ed58bb"],
    ["Naila Julianti" ,"222310093", "8a890a"],
    ["Najwa Siti Najia Rahmadan" ,"222310162", "3cba7b"],
    ["Neta Septiani" ,"222310235", "0711d2"],
    ["Rendiyanto" ,"222310098", "57ebbb"],
    ["Resa Sundari" ,"222310167", "a74cc6"],
    ["Ria Sukanti" ,"222310201", "591ad3"],
    ["Ridwan" ,"222310239", "2d1ca2"],
    ["Rifa Sauma Malika" ,"222310029", "59c933"],
    ["Rima" ,"222310063", "c220b4"],
    ["Riska Herlina" ,"222310202", "06ba74"],
    ["Rizki Ibnu Akila" ,"222310030", "ab5c1d"],
    ["Siti Alma Andina Mulya" ,"222310170", "f7ff37"],
    ["Sri Wahdiani" ,"222310067", "01044c"],
    ["Zesaluna Sagitara Putri Yosephira" ,"222310070", "9223c4"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_APHP_IV():
        kelas = [
    ["Adam Zufar Hamdalah", "222310037", "eb9c18"],
    ["Ageng Nia Tantri", "222310038", "70a0c2"],
    ["Akbar Awaludin", "222310212", "366f45"],
    ["Al Furqon", "222310002", "b4aa33"],
    ["Alpian", "222310213", "8a797c"],
    ["Andres Saputra", "222310214", "cd4543"],
    ["Aris Abdul Rohman", "222310075", "94fcc6"],
    ["Azriel Marsya Islamy", "222310042", "ac2ee1"],
    ["Bayu Herlambang", "222310145", "f58594"],
    ["Dwi Ayu Andini", "222310183", "cf19fe"],
    ["Egi Pratama", "222310148", "db5f02"],
    ["Fahra Zaskia Kirana", "222310011", "62d3d6"],
    ["Gifari Gaji Al-Malik", "222310082", "c06623"],
    ["Giri Herlambang", "222310118", "3d0430"],
    ["Irgi Putri Regita Septrianti", "222310120", "6ebf7b"],
    ["Kendy Mulyawati", "222310016", "390119"],
    ["M Fahrisal", "222310192", "50294f"],
    ["Megi Gimnastiar", "222310157", "00206c"],
    ["Mira Rahmawati", "222310019", "92aa3a"],
    ["Muhamad Kopal Gumelar", "222310126", "0d470f"],
    ["Muhammad Rasya", "222310128", "9edc90"],
    ["Napisha Aulia", "222310024", "aebb67"],
    ["Nurmalia", "222310164", "dfec9d"],
    ["Pebrian Syah", "222310060", "685ecf"],
    ["Putra Anmal Bahri", "222310096", "d8053a"],
    ["Saskaridho Pangestu", "222310169", "00a53d"],
    ["Siti Najla", "222310102", "844702"],
    ["Siti Padilahtul Rahma", "222310206", "67269c"],
    ["Sopi Ananda Putri", "222310243", "ead331"],
    ["Sri Ulandari", "222310033", "e097e8"],
    ["Viola Putri Nuriyana", "222310208", "6b5950"],
    ["Wiliyanto Zulfikri", "222310035", "47729a"],
    ["Yana Saputra", "222310105", "fd6e18"],
    ["Zikri Maulana", "222310315", "7415f3"]]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_APHP_V():
        kelas = [
    ['Aulia Hikmatulillah Ratnasari', '222310144', 'be8a67'],
    ['Aurell Sahira', '222310215', '52494a'],
    ['Chica Muhlisoh', '222310180', '7f2d4e'],
    ['Daffa Putra Darmawan', '222310112', 'bc0339'],
    ['Dika Pebrian', '222310147', '869584'],
    ['Dwi Anggraeni', '222310045', '8f6dc9'],
    ['Fajar Awaludin', '222310081', 'bee5de'],
    ['Firiyal Azri Rongan', '222310012', 'e93e72'],
    ['Ghina Nur Fairus', '222310048', '988c54'],
    ['Haikal Saputra', '222310013', '817bb0'],
    ['Indah Puspita', '222310050', '45f228'],
    ['Irwan Kurniawan', '222310225', '37d804'],
    ['Jonathan Sopianto', '222310121', '46d777'],
    ['Latifah', '222310227', 'f44b81'],
    ['Lutfi Al-Rasyid', '222310156', '6d2097'],
    ['M. Solihin', '222310018', 'a9a4ab'],
    ['Mardian', '222310088', '703e49'],
    ['Melinda Calista Putri', '222310229', '8051e1'],
    ['Muhamad Algifary', '222310125', '1324f3'],
    ['Muhamad Ramdoni', '222310194', '433702'],
    ['Muhammad Hanny', '222310022', '9a278f'],
    ['Nanda Septian', '222310196', 'a07a30'],
    ['Nazwa Sholihatu Azzahra', '222310130', 'a22840'],
    ['Putra Hairil Anwar', '222310132', '7bf17b'],
    ['Putri Jamilah', '222310165', '2d44ca'],
    ['Rara Sri Afriliati', '222310238', '501a90'],
    ['Rena Nurmayanti', '222310062', 'f10876'],
    ['Ringga Julianda Putra', '222310099', '655ff3'],
    ['Silfani Herawati', '222310065', '766f00'],
    ['Siti Nurhasanah', '222310205', '176382'],
    ['Siti Padilah Amelia', '222310171', 'd11079'],
    ['Wiliyanto Zulfikri', '222310035', '47729a'],
    ['Yana Saputra', '222310105', 'fd6e18'],
    ['Zikri Maulana', '222310315', '7415f3']]
        panjang = len(kelas)
        return kelas, panjang
    @staticmethod
    def XI_APHP_VI():
        kelas = [
    ['Alicya Aprila Rachma', '222310039', 'd4506e'],
    ['Alpan Alpian', '222310142', '48546a'],
    ['Asyla Nadira', '222310110', 'ed60d8'],
    ['Bagas', '222310076', 'c9ff39'],
    ['Dani Ramdani', '222310146', '0ea8b4'],
    ['David Dwinardo', '222310217', '3b8fcf'],
    ['Denda Arya Saputra', '222310182', 'df2535'],
    ['Denis', '222310008', 'a933f1'],
    ['Deskha Putra Firdiawan Susandy', '222310044', '7513a3'],
    ['Egi Ramdani', '222310184', 'f9a283'],
    ['Farras Nailatul Izzah', '222310117', 'a2dc37'],
    ['Haekal Yasirul Alam', '222310187', '98b71f'],
    ['Hisyam Hilmawan', '222310224', 'b43fbc'],
    ['Juantri Febrian', '222310154', '8c85fb'],
    ['Keiysa', '222310226', '2162d1'],
    ['Kiki Salman Al Farizi', '222310086', 'dac8c4'],
    ['Laras Nurjamilah', '222310155', '32f2ab'],
    ['Lemi Ahmad Sulaeman', '222310017', '8d23ae'],
    ['Muhamad Ibnu Rapi', '222310055', '85436c'],
    ['Muhamad Iqbal', '222310090', '50e808'],
    ['Mutia Laela', '222310233', 'fb29d7'],
    ['Nur Deyalani', '222310059', '42be46'],
    ['Nur Septi Rahayu', '222310095', '493786'],
    ['Radin Sekar Hamida', '222310027', '2ab5b0'],
    ['Rahmawati', '222310133', '7e0f84'],
    ['Rasyad Islami Permana', '222310028', '63d9fe'],
    ['Salma Rahayu', '222310064', '7ee095'],
    ['Salman Wahidin', '222310100', 'b10415'],
    ['Saskia Dwi Ananda', '222310203', 'bde787'],
    ['Sheila Marchanda', '222310031', '02a064'],
    ['Siti Fatihah As Salma', '222310204', '38fa23'],
    ['Siti Hawa', '222310242', '0238a7'],
    ['Topan Dwi Satria', '222310034', '7e7165'],
    ['Ulvi Putri Septiani', '222310138', '41a04e'],
    ['Zikri Maulana', '222310315', '7415f3']]
        panjang = len(kelas)
        return kelas, panjang
    
    @staticmethod
    def XI_PMHP():
        kelas = [
    ["Afrillia Maulidina", "222310352", "a9d758"],
    ["Ahmad Hilman Mahubi", "222310072", "7927d6"],
    ["Aisyah Lestari", "222310141", "a83127"],
    ["Amanda Oktaviani", "222310040", "1995ae"],
    ["Ana Hanifah", "222310109", "6f8144"],
    ["Diana Ajkia Putra", "222310078", "c44b30"],
    ["Enjelita", "222310046", "6c5649"],
    ["Erni", "222310149", "400601"],
    ["Haikal Difta P", "222310223", "6aff10"],
    ["Haiqal Fawaz Wardana", "222310049", "df816a"],
    ["Hanifah Novianti", "222310083", "fff755"],
    ["Helmi Damayanti", "222310119", "39df04"],
    ["Heni Nurliyana", "222310152", "1ee072"],
    ["Jaskia Destriani", "222310353", "c95c2f"],
    ["Jenal Faridi", "222310085", "8a637a"],
    ["Laras Soekoco", "222310191", "51edb7"],
    ["Lilis Anisa", "222310052", "44fdaf"],
    ["Lusiana Rahayu", "222310123", "c95b47"],
    ["Muhamad Fauzan Firdaus", "222310230", "71006c"],
    ["Muhamad Raika", "222310159", "085940"],
    ["Muhamad Taufiq Qurohman", "222310091", "0c9896"],
    ["Muhammad Farrel Dwishaqi", "222310160", "41b535"],
    ["Muhammad Galih Ramadhan", "222310232", "184a5c"],
    ["Muhammad Satria Pasha Utama", "222310161", "3449fa"],
    ["Nurhalifah Azahara", "222310131", "b58786"],
    ["Putri Nur Kaila", "222310199", "7d3011"],
    ["Rafa Maulana", "222310061", "65bb3f"],
    ["Rio Tamashi Kang", "222310135", "76723f"],
    ["Ririn R", "222310168", "8dbf9b"],
    ["Sinta Amelia", "222310101", "ab0393"],
    ["Siti Nur Azizah Aulia", "222310357", "2d95a7"],
    ["Sukma Sahrul Hidayat", "222310103", "921cf3"],
    ["Syahrita Nurohmah", "222310137", "8897d1"],
    ["Tasya Berliana", "222310207", "39f3f1"],
    ["Wildan Ramadhan", "222310245", "13a882"],
    ["Yesi Tamara", "222310139", "54799d"]]
        panjang = len(kelas)
        return kelas, panjang

    # Add all other class methods here...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_class_data/<class_name>')
def get_class_data(class_name):
    try:
        method = getattr(LMS_data, class_name)
        data, length = method()
        return jsonify({
            'success': True,
            'data': data,
            'length': length
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/random_student/<class_name>')
def random_student(class_name):
    try:
        method = getattr(LMS_data, class_name)
        data, _ = method()
        if data:
            student = random.choice(data)
            return jsonify({
                'success': True,
                'student': student
            })
        return jsonify({
            'success': False,
            'error': 'No students found'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
