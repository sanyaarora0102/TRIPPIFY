print("----------------------------------------")
print("    @@ ✈️      TRIPPIYFY   ✈️ @@      ")
print("----------------------------------------")

name_user = input("Please Enter Your Name: ")
print("         🙏🏻 WELCOME", name_user)
print("----------------------------------------")

budget = int(input("Enter your budget💰: "))
guest = int(input("Enter number of people: "))
number_of_days = input("Enter your stay days: ")

print("Tell us your dream destination")


if budget <= 30000:

    print("1) Is it mountains?")
    print("       OR")
    print("2) Is it a beach?")

    Choice = int(input("Enter your choice: "))
    print("So it's", Choice, "GREAT CHOICE! Here We Go")

    if Choice==1:

        print("Here are your options")
        print("Click one and let us know!")
        print("i) KASOL")
        print("^^^^^^^^^^^")
        print("ii) DHARAMSHALA")
        print("^^^^^^^^^^^")
        print("iii) PACHMARHI")
        print("^^^^^^^^^^^")
        print("iv) SHIMLA")
        print("^^^^^^^^^^^")
        print("v) AULI")

    elif Choice==2:

        print("Here are your options")
        print("Click one and let us know!")
        print("vi) SOUTH GOA")
        print("^^^^^^^^^^^")
        print("vii) PURI, ODISHA")
        print("^^^^^^^^^^^")
        print("viii) DAMAN AND DIU")

    else:
        print("Invalid choice! Please enter 1 or 2.")


    if Choice==1 or Choice==2:

        destination = input("Enter your destination: ")

        if destination == "i":

            print("The preferred list of hotels are")
            print("HOTEL PANCHALI")
            print("THE HILLSIDE")
            print("THE PINE VIEW")
            print("**********************************")
            print("The preferred places to visit are")
            print("PARVATI RIVER")
            print("KASOL MARKET")
            print("GURUDWARA MANIKARAN SAHIB")

        elif destination=="ii":

            print("The preferred list of hotels are")
            print("PEMA THANG")
            print("SERKONG RABSEL")
            print("ALPINE BNB")
            print("**********************************")
            print("The preferred places to visit are")
            print("McLEOD GANJ")
            print("NAMGYAL MONASTERY")
            print("BHAGSU WATERFALL")

        elif destination=="iii":

            print("The preferred list of hotels are")
            print("THE SUMMER HOUSE")
            print("TOWNHOUSE")
            print("HOTEL DIVINE PEAK")
            print("**********************************")
            print("The preferred places to visit are")
            print("BEE FALLS")
            print("PANDAV CAVES")
            print("JATASHANKAR CAVES")

        elif destination=="iv":

            print("The preferred list of hotels are")
            print("WILLOW BANKS")
            print("HOTEL SILVERINE")
            print("WOODVILLE PALACE")
            print("**********************************")
            print("The preferred places to visit are")
            print("RIDGE & MALL ROAD")
            print("KUFRI")
            print("GREEN VALLEY")

        elif destination=="v":

            print("The preferred list of hotels are")
            print("MOUNTAIN ROVER SKI")
            print("FARAWAY COTTAGES")
            print("CASA HIMALAYA")
            print("**********************************")
            print("The preferred places to visit are")
            print("GURSO BUGYAL")
            print("CHATTRAKUND")
            print("JOSHIMATH")

        elif destination=="vi":

            print("The preferred list of hotels are")
            print("HOTEL PAULINO")
            print("CASA BEACH HUT")
            print("OXYGEN PALOLEM")
            print("**********************************")
            print("The preferred places to visit are")
            print("GOA CHITRA MUSEUM")
            print("COLVA BEACH")
            print("PALOLEM BEACH")

        elif destination=="vii":

            print("The preferred list of hotels are")
            print("FORTUNE BEACHFRONT")
            print("PARK INN")
            print("STERLING ARKA")
            print("**********************************")
            print("The preferred places to visit are")
            print("JAGANNATH TEMPLE")
            print("SHREE GUNDICHA TEMPLE")
            print("LOKNATH TEMPLE")

        elif destination=="viii":

            print("The preferred list of hotels are")
            print("THE DELTIN")
            print("THE FERN SEASIDE")
            print("URBANE")
            print("**********************************")
            print("The preferred places to visit are")
            print("JAMPORA BEACH")
            print("DEVKA BEACH")
            print("MOTI DAMAN FORT")

        else:
            print("Invalid destination choice!You have to try once again!")


    if Choice==1:

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("----- PACKING CHECKLIST -----")
        print("O Warm clothes")
        print("O Comfortable shoes")
        print("O Jacket")
        print("O Sunglasses")
        print("O Medicines")
        print("O Power bank")

    elif Choice==2:

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("----- PACKING CHECKLIST -----")
        print("O Sunscreen")
        print("O Light clothes")
        print("O Sunglasses")
        print("O Slippers")
        print("O Power bank")


else:

    print("I) Is it mountains?")
    print("       OR")
    print("II) Is it a beach?")

    Options = (input("Enter your choice: ")).upper()
    print("So it's", Options, "GREAT OPTION! Here We Go")

    if Options=="I":

        print("Here are your options")
        print("Click one and let us know!")
        print("a) LEH LADAKH")
        print("^^^^^^^^^^^")
        print("b) SPITI VALLEY, HIMACHAL PRADESH")
        print("^^^^^^^^^^^")
        print("c) PAHALGAM, KASHMIR")
        print("^^^^^^^^^^^")
        print("d) GANGTOK & NORTH SIKKIM")
        print("^^^^^^^^^^^")
        print("e) CHOPTA, UTTARAKHAND")

    elif Options=="II":

        print("Here are your options")
        print("Click one and let us know!")
        print("f) ANDAMAN & NICOBAR")
        print("^^^^^^^^^^^")
        print("g) LAKSHADWEEP")
        print("^^^^^^^^^^^")
        print("h) VARKALA & KOVALAM, KERALA")

    else:
        print("Invalid choice! Please enter 1 or 2.")


    if Options=="I" or Options=="II":

        dream_place=input("Enter your dream place: ")

        if dream_place=="a":

            print("The preferred list of hotels are")
            print("THE VINTAGE VILLAS")
            print("THE GAWALING LADAKH")
            print("LEH STUMPA")
            print("**********************************")
            print("The preferred places to visit are")
            print("SANGAM POINT")
            print("HALL OF FAME")
            print("PANGONG TSO")

        elif dream_place=="b":

            print("The preferred list of hotels are")
            print("ZOSTEL HOMES TABO")
            print("SOL ECO HOTEL")
            print("KUKU HOMESTAY")
            print("**********************************")
            print("The preferred places to visit are")
            print("TABO MONASTERY")
            print("KOMIC")
            print("CHANDRATAL LAKE")

        elif dream_place=="c":

            print("The preferred list of hotels are")
            print("THE VALE LODGE")
            print("WOODS RESORT")
            print("VELOUR PINES")
            print("**********************************")
            print("The preferred places to visit are")
            print("BETAAB VALLEY")
            print("CHANDANWARI")
            print("ARU VALLEY")

        elif dream_place=="d":

            print("The preferred list of hotels are")
            print("CLARION HOTEL")
            print("THE GOLDEN CREST")
            print("HIMALAYAN HEIGHTS")
            print("**********************************")
            print("The preferred places to visit are")
            print("MG MARG")
            print("NATHULA PASS")
            print("TASHI VIEW POINT")

        elif dream_place=="e":

            print("The preferred list of hotels are")
            print("HOTEL BATTALION")
            print("SUNRIVER RESORTS")
            print("PEACE TRIPS")
            print("**********************************")
            print("The preferred places to visit are")
            print("TUNGNATH TEMPLE")
            print("CHANDRASHILA PEAK")
            print("DEORIA TAL")

        elif dream_place=="f":

            print("The preferred list of hotels are")
            print("HOTEL CORAL INN")
            print("RAINFOREST RESORT")
            print("SILVER SAND BEACH")
            print("**********************************")
            print("The preferred places to visit are")
            print("ROSS ISLAND")
            print("CHIDIYA TAPU")
            print("CELLULAR JAIL")

        elif dream_place=="g":

            print("The preferred list of hotels are")
            print("BEACHSIDE AGATTI")
            print("HORIZON NEST")
            print("CORAL PEARL")
            print("**********************************")
            print("The preferred places to visit are")
            print("KADMATH ISLAND")
            print("MINICOY ISLAND")
            print("KALPENI ISLAND")

        elif dream_place=="h":

            print("The preferred list of hotels are")
            print("THE BEACH CLUB")
            print("UDAY SAMUDRA HOTEL")
            print("HOTEL MARINE PALACE")
            print("**********************************")
            print("The preferred places to visit are")
            print("VARKALA BEACH")
            print("KAPPIL LAKE & BEACH")
            print("LIGHTHOUSE BEACH")

        else:
            print("Invalid destination choice!You have to try once again.")


    if Options=="I":

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("----- PACKING CHECKLIST -----")
        print("O Warm clothes")
        print("O Comfortable shoes")
        print("O Jacket")
        print("O Sunglasses")
        print("O Medicines")
        print("O Power bank")

    elif Options=="II":

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("----- PACKING CHECKLIST -----")
        print("O Sunscreen")
        print("O Light clothes")
        print("O Sunglasses")
        print("O Slippers")
        print("O Power bank")
print("==========================================")
print("          HAVE A GREAT TRIP! ✈️")
print("==========================================")