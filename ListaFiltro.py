#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI() 

#Levantamos el server Uvicorn
#-uvicorn ListaFiltro:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class moto(BaseModel):
    codigo:int
    marca: str
    modelo:str
    año:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  


motoslits=[

    moto(codigo=1, marca="Gottlieb", modelo="Daimler Reitwagen", año="1885"),
    moto(codigo=2, marca="Flying Merkel", modelo="Model V", año="1911"),
    moto(codigo=3, marca="Harley Davidson", modelo="Modelo 7D", año="1911"),
    moto(codigo=4, marca="Peugeot", modelo="Paris Nice", año="1913"),
    moto(codigo=5, marca="Indian", modelo="Valve Board", año="1915"),
    moto(codigo=6, marca="Megola ", modelo="Sport", año="1920"),
    moto(codigo=7, marca="Bmw", modelo="R32", año="1923"),
    moto(codigo=8, marca="Bohmerland", modelo="Model 598", año="1925"),
    moto(codigo=9, marca="Ariel Square Four", modelo="MK", año="1931"),
    moto(codigo=10, marca="Indian", modelo="Sport Scout", año="1934"),
    moto(codigo=11, marca="Triumph", modelo="Speed Twin", año="1938"),
    moto(codigo=12, marca="Vespa", modelo="Gts", año="1946"),
    moto(codigo=13, marca="Solex ", modelo="Velosolex", año="1946"),
    moto(codigo=14, marca="Gilera", modelo="Saturno", año="1947"),
    moto(codigo=15, marca="Indian", modelo="Chief", año="1948"),
    moto(codigo=16, marca="BSA", modelo="Gold Star", año="1952"),
    moto(codigo=17, marca="Montesa ", modelo="Brio 90", año="1953"),
    moto(codigo=18, marca="Vespa", modelo="Gs", año="1955"),
    moto(codigo=19, marca="Vespa", modelo="180SS", año="1911"), 
    moto(codigo=20, marca="Montesa", modelo="Cappra", año="1955"),
    moto(codigo=21, marca="Montesca", modelo="Enduro", año="1944"),
    moto(codigo=22, marca="Harley Davidson", modelo="Sportster XL", año="1957"),
    moto(codigo=23, marca="Honda", modelo="Super club", año="1958"),
    moto(codigo=24, marca="Triumph", modelo="Bonneville", año="1958"),
    moto(codigo=25, marca="Harley Davidson", modelo="Duo Glide", año="1959"),
    moto(codigo=26, marca="Bultaco", modelo="Tralla", año="1959"),
    moto(codigo=27, marca="Honda", modelo="CB", año="1960"),
    moto(codigo=28, marca="Montesa", modelo="Impala", año="1962"),
    moto(codigo=29, marca="OSSA", modelo="GT", año="1962"),
    moto(codigo=30, marca="Norton", modelo="Manx", año="1962"),
    moto(codigo=31, marca="Bultaco", modelo="Sherpa T", año="1962"),
    moto(codigo=32, marca="Bultaco", modelo="Metralla MK2", año="1966"),
    moto(codigo=33, marca="Derbi", modelo="Antorcha 50", año="1965"),
    moto(codigo=34, marca="Norton", modelo="Commando 750", año="1967"),
    moto(codigo=35, marca="Buell", modelo=" Mach III", año="1968"),
    moto(codigo=36, marca="Vespa", modelo=" Vespino", año="1968"),
    moto(codigo=37, marca=" Kawasaki", modelo=" Mach III", año="1968"),
    moto(codigo=38, marca="Montesa", modelo="Cota", año="1968"),
    moto(codigo=39, marca="Honda", modelo="Four", año="1969"),
    moto(codigo=40, marca="Suzuki", modelo="Gt", año="1968"),
    moto(codigo=41, marca="Brixton", modelo="Z1", año="1972"),
    moto(codigo=42, marca="Yamaha", modelo="RD", año="1972"),
    moto(codigo=43, marca="Benelli", modelo="Sei", año="1973"),
    moto(codigo=44, marca="Ducati", modelo="Road", año="1973"),
    moto(codigo=45, marca="Sanglas", modelo="E", año="1973"),
    moto(codigo=46, marca="Bultaco", modelo="Pursang MK8", año="1974"), 
    moto(codigo=47, marca="Ducati", modelo="SS 750", año="1974"),
    moto(codigo=48, marca="Laverda", modelo="SF 750", año="1974"),
    moto(codigo=49, marca="Honda", modelo="Gold Wing", año="1975"),
    moto(codigo=50, marca="Bultaco", modelo="Frontera", año="1975"),
    moto(codigo=51, marca="BMW", modelo="R 90", año="1976"),
    moto(codigo=52, marca="OSSA", modelo="Yankee", año="1976"),
    moto(codigo=53, marca="Guzzi", modelo="Le Mans", año="1977"),
    moto(codigo=54, marca="Ariic", modelo="XT 500", año="1977"),
    moto(codigo=55, marca="Honda", modelo="CBX", año="1978"),
    moto(codigo=56, marca="Buell", modelo=" Z 1300", año="1978"),
    moto(codigo=57, marca="Yamaha", modelo="SR 500", año="1975"),
    moto(codigo=58, marca="BMW", modelo="R 80", año="1980"),
    moto(codigo=59, marca="Suzuki", modelo="Katana", año="1981"),
    moto(codigo=60, marca="Suzuki", modelo="RG 250", año="1975"),
    moto(codigo=61, marca="BMW", modelo="K 100", año="1984"),
    moto(codigo=62, marca="Kawasaki", modelo="GPZ 900", año="1984"),
    moto(codigo=63, marca="Yamaha", modelo="rd 500", año="1984"),
    moto(codigo=64, marca="Arena", modelo="Max V", año="1985"),
    moto(codigo=65, marca="Bicose", modelo="GSX", año="1985"),
    moto(codigo=66, marca="Yamaha", modelo="FZ 750", año="1985"),
    moto(codigo=67, marca="Ariic", modelo="VFR", año="1986"),
    moto(codigo=68, marca="Arc", modelo="FZR", año="1984"),
    moto(codigo=69, marca="Beta", modelo="Zero", año="1989"),
    moto(codigo=70, marca="Yamaha", modelo="Super Tenere", año="1989"),
    moto(codigo=71, marca="Bimota", modelo="Tesi", año="1990"),
    moto(codigo=72, marca="Honda", modelo="Africa Twin", año="1990"),
    moto(codigo=73, marca="Kawasaki", modelo="ZZ-R", año="1990"),
    moto(codigo=74, marca="Caviga", modelo="DR Big", año="1990"),
    moto(codigo=75, marca="Honda", modelo="CBR", año="1991"),
    moto(codigo=76, marca=" Honda", modelo="NR", año="1992"),
    moto(codigo=77, marca="Ducati", modelo="Monster", año="1993"),
    moto(codigo=78, marca="Sanglas", modelo="LS", año="1994"),
    moto(codigo=79, marca="Triumph", modelo="Speed Triple", año="1994"),
    moto(codigo=80, marca="KTM", modelo="Duke", año="1994"),
    moto(codigo=81, marca="BMW", modelo="R 1200", año="1997"),
    moto(codigo=82, marca="MV ", modelo="Agusta", año="1998"),
    moto(codigo=83, marca="Suzuki", modelo="Burgman", año="1998"),
    moto(codigo=84, marca="Caviga", modelo="R1J", año="1998"),
    moto(codigo=85, marca="Suzuki", modelo="GSX 1300", año="1999"),
    moto(codigo=86, marca="Yamaha", modelo="T max", año="2000"),
    moto(codigo=87, marca="BMW", modelo="C1", año="2001"),
    moto(codigo=88, marca="Harley Davidson", modelo="V Rod", año="2001"),
    moto(codigo=89, marca="KTM", modelo="Adventure", año="2003"),
    moto(codigo=90, marca="Honda", modelo="CBR RR", año="2004"),
    moto(codigo=91, marca="Montesa", modelo="Cota RT", año="2005"),
    moto(codigo=92, marca="Piaggio", modelo="MP3", año="2006"),
    moto(codigo=93, marca="Triumph", modelo="Street Triple", año="2007"),
    moto(codigo=94, marca="Zero", modelo="S", año="2009"),
    moto(codigo=95, marca="BMW", modelo="C Evolution", año="2011"),
    moto(codigo=96, marca="BMW", modelo="C 650", año="2012"),
    moto(codigo=97, marca="Yamaha", modelo="MT 09", año="2013"),
    moto(codigo=98, marca="Ducati", modelo="Scrambler", año="2015"),
    moto(codigo=99, marca="Honda", modelo="X ADV", año="2017"),
    moto(codigo=100, marca="Ducati", modelo="Superleggera", año="2017"),
    moto(codigo=101, marca="BMW", modelo="HP4", año="2017"),
    moto(codigo=102, marca="Yamaha", modelo="Nlken", año="2018"),
    moto(codigo=103, marca="KYMCO", modelo="Lonex", año="2018"),
    moto(codigo=104, marca="Harley Davidson", modelo="Livewire", año="2019"),
    moto(codigo=105, marca="Daelim", modelo="Daystar", año="2015"),
    moto(codigo=106, marca="Yamaha", modelo="Fazer N", año="2011"),
    moto(codigo=107, marca="Hyosung", modelo="Karion", año="2012"),
    moto(codigo=108, marca="Hyosung", modelo="GT Pro comet", año="2012"),
    moto(codigo=109, marca="Hyosung", modelo="ST7", año="2012"), 
    moto(codigo=110, marca="KTM", modelo="SMC R", año="2001"),
    moto(codigo=111, marca="KTM", modelo="Super Duke R", año="2017"),
    moto(codigo=112, marca="Yamaha", modelo="SR400", año="2013"),
    moto(codigo=113, marca="Kawasaki", modelo="ERN", año="2012"),
    moto(codigo=114, marca="Colove", modelo="Inazumas 250", año="2013"),
    moto(codigo=115, marca="Suzuki", modelo="Vanvan", año="2014"),
    moto(codigo=116, marca="Suzuki", modelo="GSX R", año="2014"),
    moto(codigo=117, marca="Colove", modelo="Intruder M", año="2002"),
    moto(codigo=118, marca="KTM", modelo="RCB R", año="2003"),
    moto(codigo=119, marca="BMW", modelo="GS R", año="2003"),
    moto(codigo=120, marca="Derbi", modelo="S XR", año="2014"),
    moto(codigo=121, marca="BMW", modelo="RR SL", año="2003"),
    moto(codigo=122, marca="Suzuki", modelo="Bandit s", año="2014"),
    moto(codigo=123, marca="Derbi", modelo="V strom ABS", año="2013"),
    moto(codigo=124, marca="Suzuki", modelo="Hayabusa", año="2004"),
    moto(codigo=125, marca="Kawasaki", modelo="Vulcan S", año="2004"),
    moto(codigo=126, marca="BMW", modelo="GUM", año="2004"),
    moto(codigo=127, marca="Triumph", modelo="Trophy", año="2005"),
    moto(codigo=128, marca="Felo", modelo="ZSL", año="2005"),
    moto(codigo=129, marca="Suzuki", modelo="Gladius T", año="2017"),
    moto(codigo=130, marca="Kawasaki", modelo="Ninja", año="2014"),
    moto(codigo=131, marca="Hanway", modelo="Versy L", año="2006"),
    moto(codigo=132, marca="Ducati", modelo="Panigale", año="2013"),
    moto(codigo=133, marca="Triumpg", modelo="Tiger XC", año="2012"),
    moto(codigo=134, marca="Hanway", modelo="Gold Wing", año="2012"),
    moto(codigo=135, marca="Honda", modelo="Fireblade", año="2007"),
    moto(codigo=136, marca="Kawasaki", modelo="Z", año="2007"),
    moto(codigo=137, marca="Felo", modelo="VFR", año="2007"),
    moto(codigo=138, marca="Ducati", modelo="Urban Enduro", año="2007"),
    moto(codigo=139, marca="KTM", modelo="Adventure K", año="2007"),
    moto(codigo=140, marca="Triumph", modelo="Tiger Explorer XC", año="2012"),
    moto(codigo=141, marca="Kawasaki", modelo="Versys", año="2011"),
    moto(codigo=142, marca="Ducati", modelo="Monster 821", año="20012"),
    moto(codigo=143, marca="Ducati", modelo="Multistrada", año="2008"),
    moto(codigo=144, marca="CfMoto", modelo="Nike", año="2018"),
    moto(codigo=145, marca="Benelli", modelo="BN R", año="2018"),
    moto(codigo=146, marca="Royal Enfield", modelo="Himalaya", año="2018"),
    moto(codigo=147, marca="Fantic Caballero", modelo="Flat Track", año="2018"),
    moto(codigo=148, marca="Aprilia", modelo="Factory", año="2017"),
    moto(codigo=149, marca="Husqvarna", modelo="Vitpilen", año="2018"),
    moto(codigo=150, marca="Husqvarn", modelo="Svartpilen", año="2016"),
    moto(codigo=151, marca="Goes ", modelo="GP", año="2018"),
    moto(codigo=152, marca="Goes", modelo="TK", año="2017"),
    moto(codigo=153, marca="MV Agusta", modelo="F3", año="2018"),
    moto(codigo=154, marca="MV Agusta", modelo="Brutale", año="2019"),
    moto(codigo=155, marca="CFMoto", modelo="Papio", año="2018"),
    moto(codigo=156, marca="Moto Guzzi", modelo="Milano", año="2017"),
    moto(codigo=157, marca="Mitt", modelo="Scrambler", año="2017"),
    moto(codigo=158, marca="MH", modelo="WYN", año="2019"),
    moto(codigo=159, marca="MH", modelo="Lord Martin", año="2019"),
    moto(codigo=160, marca="MH", modelo="Bogga", año="2019"),
    moto(codigo=161, marca="Malaguti", modelo="XTM", año="2019"),
    moto(codigo=162, marca="Malaguti", modelo="Monte Pro", año="2020"),
    moto(codigo=163, marca="Brixton", modelo="BX", año="2020"),
    moto(codigo=164, marca="Brixton", modelo="Saxby", año="2020"),
    moto(codigo=165, marca="Macbor", modelo="Fun", año="2021"),
    moto(codigo=166, marca="Keeway", modelo="RKF", año="2021"),
    moto(codigo=167, marca="Triumph", modelo="Street Triple R", año="2021"),
    moto(codigo=168, marca="Voge", modelo="R500", año="2020"),
    moto(codigo=169, marca="Keeway", modelo="Superlight", año="2020"),
    moto(codigo=170, marca="Zero", modelo="SR", año="2020"),
    moto(codigo=171, marca="Zontes", modelo="V", año="2021"),
    moto(codigo=172, marca="MV", modelo="Dragster", año="2020"),
    moto(codigo=173, marca="Voge", modelo="DS", año="2020"),
    moto(codigo=174, marca="FB Mondial", modelo="HPS", año="2021"),
    moto(codigo=175, marca="OX One", modelo="Tokyo", año="2021"),
    moto(codigo=176, marca="Motron", modelo="Revolver", año="2021"), 
    moto(codigo=177, marca="Motron", modelo="Vizion", año="2022"),
    moto(codigo=178, marca="Zontes", modelo="GX1", año="2022"),
    moto(codigo=179, marca="Urbet", modelo="Gadiro", año="2023"),
    moto(codigo=180, marca="Orcal", modelo="Astor", año="2022"),
    moto(codigo=181, marca="Zontes", modelo="U1", año="2023"),
    moto(codigo=182, marca="Urbet", modelo="Nura", año="2023"),
    moto(codigo=183, marca="Bimoto", modelo="Tesi", año="2022"),
    moto(codigo=184, marca="Super Soco", modelo="TS Street Hunter", año="2022"),
    moto(codigo=185, marca="QJ SRK", modelo="S", año="2023"),
    moto(codigo=186, marca="Mutt", modelo="Mushman", año="2023"),
    moto(codigo=187, marca="QJ SRK", modelo="X", año="2023"),
    moto(codigo=188, marca="RGNT", modelo="Scrambler", año="2022"),
    moto(codigo=189, marca="RGNT", modelo="Clasicc", año="2023"),
    moto(codigo=190, marca="OX One", modelo="Montecarlo", año="2021"),
    moto(codigo=191, marca="Orcal", modelo="SK03", año="2021"),
    moto(codigo=192, marca="Leonart", modelo="Rigger", año="2023"),
    moto(codigo=193, marca="Macbor Rockster", modelo="Flat", año="2017"),
    moto(codigo=194, marca="Triumph", modelo="Trident", año="2024"),
    moto(codigo=195, marca="Rieju", modelo="Century", año="2024"),
    moto(codigo=196, marca="Keeway", modelo="V3C", año="2023"),
    moto(codigo=197, marca="Energica", modelo="Experia", año="2024"),
    moto(codigo=198, marca="Triumph", modelo="Rocket 3", año="2017"),
    moto(codigo=199, marca="Macbor Rockster", modelo="Mot", año="2024"),
    moto(codigo=200, marca="Vmoto", modelo="Stash", año="2024") 
    ] 
 

#***Get
@app.get("/Motosclass/")
async def motosclass():
    return (motoslits)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
@app.get("/Motosclass/{codigo}") 
async def motosclass(codigo:int):
    motos=filter (lambda moto: moto.codigo == codigo, motoslits)  #Función de orden superior
    try:
        return list(motos)
    except:
        return{"error":"No se ha encontrado el usuario"}
    


@app.get("/Motosclass/Modelos/{modelo}")
async def motosclass(modelo:str):
    motos=filter (lambda moto: moto.modelo == modelo, motoslits)  #Función de orden superior
    try:
        return list(motos)
    except:
        return{"error":"No se ha encontrado el usuario"}
 