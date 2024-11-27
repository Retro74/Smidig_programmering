from tkinter import *
from tkinter.ttk import *
import les_postnummer
from datetime import datetime
import re  # For å validere e-postformat
from pathlib import Path
fileName_icon = 'form.ico'
fileName_eye = 'eye2.png'
fileName_ceye = 'ceye2.png'
imagesFolder = "images"
pyFilePath = Path(__file__).resolve().parent

fullFilePath_icon = pyFilePath.joinpath(imagesFolder).joinpath(fileName_icon)
fullFilePath_eye = pyFilePath.joinpath(imagesFolder).joinpath(fileName_eye)
fullFilePath_ceye = pyFilePath.joinpath(imagesFolder).joinpath(fileName_ceye)

# Opprette hovedvinduet
root = Tk()
root.title("Registreringsskjema")
root.geometry("450x800")
root.iconbitmap(fullFilePath_icon)

phIm_eye = PhotoImage(file=fullFilePath_eye)  # Sett inn et ikon
phIm_ceye = PhotoImage(file=fullFilePath_ceye)  # Sett inn et ikon

dict_postnrpostSted=les_postnummer.get_list_postnummer_poststed()
list_entryFag_spinKarakter_btnSlett = []

def add_placeholder(entry, placeholder_text):
    # Setter initial placeholder-tekst
    entry.insert(0, placeholder_text)
    entry.config(foreground="grey")

    # Fjerner placeholder når brukeren klikker
    def on_focus_in(event):
        if event.widget.get() == placeholder_text:
            event.widget.delete(0, "end")
            event.widget.config(foreground="black")
    
    # Legger til placeholder hvis feltet er tomt når brukeren forlater
    def on_focus_out(event):
        if event.widget.get() == "":
            event.widget.insert(0, placeholder_text)
            event.widget.config(foreground="grey")

    # Binder hendelsene til den aktuelle widgeten (Entry)
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def slett_fag(event):
    removeId = event.widget.name
    print (removeId)
    for verdi in list_entryFag_spinKarakter_btnSlett[removeId].values():
        verdi.destroy()
    list_entryFag_spinKarakter_btnSlett.pop(removeId)

    teller =0
    for fag in list_entryFag_spinKarakter_btnSlett:
        fag["entry_fag"].grid_configure(row=teller)
        fag["spB_karakter"].grid_configure(row=teller)
        fag["btn_slettFag"].grid_configure(row=teller)
        fag["btn_slettFag"].name =teller
        teller +=1
    

def legg_til_fag():
    
    list_entryFag_spinKarakter_btnSlett.append({
        "entry_fag": Entry(frm_fag, width=20), 
        "spB_karakter": Spinbox(frm_fag, width=3, from_=1, to=6, state="readonly"), 
        "btn_slettFag": Button(frm_fag, text="Slett")})
    
    list_entryFag_spinKarakter_btnSlett[-1]["entry_fag"].grid(row=len(list_entryFag_spinKarakter_btnSlett)-1, column=0,sticky="W", padx=0, pady=5)
    add_placeholder(list_entryFag_spinKarakter_btnSlett[-1]["entry_fag"], "Fag")
    list_entryFag_spinKarakter_btnSlett[-1]["spB_karakter"].set(3)
    list_entryFag_spinKarakter_btnSlett[-1]["spB_karakter"].grid(row=len(list_entryFag_spinKarakter_btnSlett)-1, column=1,sticky="W", padx=0, pady=5)
    list_entryFag_spinKarakter_btnSlett[-1]["btn_slettFag"].grid(row=len(list_entryFag_spinKarakter_btnSlett)-1, column=2,sticky="W", padx=0, pady=5)
    list_entryFag_spinKarakter_btnSlett[-1]["btn_slettFag"].name = len(list_entryFag_spinKarakter_btnSlett)-1
    list_entryFag_spinKarakter_btnSlett[-1]["btn_slettFag"].bind("<Button-1>", slett_fag)
    btn_leggTilFag.grid_configure(row=len(list_entryFag_spinKarakter_btnSlett))

#Se passord
def btn_password_reveal_press(event):
    event.widget.config(image=phIm_eye)
    if event.widget.name == "btn_password_reveal1":
        entry_password1.config(show="")
    else:
        entry_password2.config(show="")

def btn_password_reveal_release(event):
        event.widget.config(image=phIm_ceye)
        if event.widget.name == "btn_password_reveal1":
            entry_password1.config(show="*")
        else:
            entry_password2.config(show="*")


##Poststedoppslag
def on_postnummer_change(*args):
    #Heneter inn data
    postnummer = strvar_postnummer.get() 
    #Sjekker om postummeret er i ordboken
    if postnummer in dict_postnrpostSted:
        lbl_postSted.config(text=dict_postnrpostSted[postnummer])
    else:
        lbl_postSted.config(text="-")

# Valideringsfunksjoner
def valider():
    fornavn = entry_fornavn.get().strip()
    etternavn = entry_etternavn.get().strip()    
    gatenavn = entry_gatenavn.get().strip()    
    husnr = entry_husnr.get().strip()
    postnummer = strvar_postnummer.get() 
    f_dato = cmb_fodselsdato.get()
    f_mnd = cmb_fodselsmnd.get()
    f_aar = cmb_fodselsaar.get()
    telefon = entry_telefon.get().strip()
    kjonn = var_kjonn.get().strip()
    email = entry_email.get().strip()
    feil = []

    # Valider navn
    if not fornavn:
        feil.append("Fornavn er obligatorisk!")
    if not etternavn:
        feil.append("Etternavn er obligatorisk!")
    if not gatenavn:
        feil.append("Gateadresse er obligatorisk!")
    if not husnr:
        feil.append("Husnummer er obligatorisk!")

    if not postnummer in dict_postnrpostSted:
        feil.append("Ugyldig postnummer!")
    
    try:
        # Forsøk å konvertere strengen til en dato
        date_string = f_dato + "." + f_mnd + "." + f_aar
        datetime.strptime(date_string, r"%d.%m.%Y")
    except ValueError:
        # Hvis det oppstår en feil, er det ikke en gyldig dato
        feil.append("Fødselsdato er ikke en gyldig dato!")

    # Valider telefonnummer (må være 8 siffer)
    if not telefon.isdigit() or len(telefon) != 8:
        feil.append("Telefonnummer må være et 8-sifret tall!")

    # Valider e-postadresse
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        feil.append("E-postadressen er ikke gyldig!")

    # Sjekk at kjønn er valgt
    if kjonn=="":
        feil.append("Kjønn er ikke valgt!")

    # Oppdater resultatet
    if feil:
        lbl_resultat.config(text="\n".join(feil), foreground="red")
    else:
        forerkortklasser=""
        for nokkel, verdi in dict_forerkortklasser.items():
            if verdi.get():
                forerkortklasser += nokkel + ", "
        skole_fag_karakterer = ""
        for fag in list_entryFag_spinKarakter_btnSlett:
            if fag["entry_fag"].get().strip() != "":
                skole_fag_karakterer += f"{fag['entry_fag'].get().strip()}, {fag['spB_karakter'].get().strip()}\n" 
        lbl_resultat.config(
            text=f"Registrering fullført!"
            f"\nFornavn: {fornavn}"
            f"\nEtternavn: {etternavn}"
            f"\nGatenavn: {gatenavn}"
            f"\nHusnummer: {husnr}"
            f"\nPostadr.: {postnummer} - {dict_postnrpostSted[postnummer]}"
            f"\nFødselsdato: {date_string}"
            f"\nTelefon: {telefon}"
            f"\nKjønn: {kjonn}"
            f"\nE-post: {email}"
            f"\nFørerkortklasser: {forerkortklasser}"
            f"\nSkolefag: {skole_fag_karakterer}",
            foreground="green")


row_count =0
#Legg inn en overskrift til skjemaet
lbl_title = Label(root, text="Registreringsskjema", font=("Arial", 16))
lbl_title.grid(row=row_count, column=0, columnspan=2, pady=10)

# Lag etiketter og inputfelt for
#Fornavn
row_count+=1
lbl_fornavn = Label(root, text="Fornavn:")
lbl_fornavn.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)
entry_fornavn = Entry(root, width=40)
entry_fornavn.grid(row=row_count, sticky="W", column=1, padx=10, pady=5)
add_placeholder(entry_fornavn, "Skriv inn fornavn")

#Etternavn
row_count+=1
lbl_etternavn = Label(root, text="Etternavn:")
lbl_etternavn.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)
entry_etternavn = Entry(root, width=40)
entry_etternavn.grid(row=row_count, column=1, padx=10,sticky="W", pady=5)
add_placeholder(entry_etternavn, "Skriv inn etternavn")

#Adresse
row_count+=1
lbl_adresse = Label(root, text="Adresse:")
lbl_adresse.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_adresse = Frame(root)
entry_gatenavn = Entry(frm_adresse, width=32)
entry_gatenavn.pack(side=LEFT, padx=5)
add_placeholder(entry_gatenavn, "Skriv inn gatenavn")

#Husnr
entry_husnr = Entry(frm_adresse, width=5)
entry_husnr.pack(side=LEFT, padx=5)
add_placeholder(entry_husnr, "Husnr")

#Legg til Adresse
frm_adresse.grid(row=row_count, column=1, padx=5, pady=5,sticky="W")

#PostAdresse
row_count+=1
lbl_postAdresse = Label(root, text="Postadresse:")
lbl_postAdresse.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_postAdresse = Frame(root)
#Postnummer
strvar_postnummer = StringVar()
strvar_postnummer.trace_add("write", on_postnummer_change)
entry_postNummer = Entry(frm_postAdresse, width=4, textvariable=strvar_postnummer)
entry_postNummer.pack(side=LEFT, padx=5)
add_placeholder(entry_postNummer, "Postnr.")

lbl_postSted = Label(frm_postAdresse, text="-")
lbl_postSted.pack(side=LEFT, padx=5)
#Legg til PostAdresse
frm_postAdresse.grid(row=row_count, column=1,sticky=W, padx=5, pady=5)

#Fødselsdato
row_count+=1
lbl_fodselsdato = Label(root, text="Fødselsdato:")
lbl_fodselsdato.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_fosdselsdato = Frame(root)
cmb_fodselsdato = Combobox(frm_fosdselsdato, values=[dato for dato in range(1,32)], state="readonly", width=2)
cmb_fodselsdato.pack(side=LEFT, padx=5)
cmb_fodselsmnd = Combobox(frm_fosdselsdato, values=[mnd for mnd in range(1,13)], state="readonly", width=2)
cmb_fodselsmnd.pack(side=LEFT, padx=5)
cmb_fodselsaar = Combobox(frm_fosdselsdato, values=[dato for dato in range(datetime.now().year-15,datetime.now().year-115,-1)], state="readonly", width=4)
cmb_fodselsaar.pack(side=LEFT, padx=5)
frm_fosdselsdato.grid(row=row_count, column=1,sticky=W, padx=5, pady=5)



#Telefonnummer
row_count+=1
lbl_telefnnummer = Label(root, text="Telefonnummer:")
lbl_telefnnummer.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)
entry_telefon = Entry(root, width=12)
entry_telefon.grid(row=row_count, column=1, padx=10, pady=5, sticky="W")
add_placeholder(entry_telefon, "8 siffer")

#E-mail
row_count+=1
lbl_email = Label(root, text="E-postadresse:")
lbl_email.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)
entry_email = Entry(root, width=40)
entry_email.grid(row=row_count, column=1, padx=10, pady=5,sticky="W")

#Førerkort
row_count+=1
lbl_forerkort = Label(root, text="Førerkort:")
lbl_forerkort.grid(row=row_count, column=0, sticky="NE", padx=10, pady=5)

frm_forerkort = Frame(root)
dict_forerkortklasser = {"Personbil":IntVar(value=0), 
                         "Personbil med henger":IntVar(value=0), 
                         "Liten lastebil":IntVar(value=0),
                         "Lastebil":IntVar(value=0), 
                         "Buss":IntVar(value=0),
                         "Trailer":IntVar(value=0)}
forerkort_row =0
forerkort_column =0
for key, verdi in dict_forerkortklasser.items():
    Checkbutton(frm_forerkort, 
                text=key, 
                variable=verdi).grid(row=forerkort_row, 
                                     column=forerkort_column, 
                                     padx=10, pady=5, sticky="W")

    forerkort_column +=1
    if forerkort_column == 2:
        forerkort_column =0
        forerkort_row +=1    

frm_forerkort.grid(row=row_count, column=1, padx=10, pady=5,sticky="W")

#Fag
row_count+=1
lbl_fag = Label(root, text=f"Registrer fag \nog karakter:")
lbl_fag.grid(row=row_count, column=0, sticky="NE", padx=10, pady=5)

frm_fag = Frame(root)
btn_leggTilFag = Button(frm_fag, text="Legg til", command=legg_til_fag, width=30)
btn_leggTilFag.grid(row=0, column=0, padx=1, pady=5,sticky="W", columnspan=2)
frm_fag.grid(row=row_count, column=1, sticky="W", padx=5, pady=5)

#velg kjønn
row_count+=1
lbl_kjonn = Label(root, text="Kjønn:")
lbl_kjonn.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_kjonn = Frame(root)
var_kjonn = StringVar(value=" ")
rb_han = Radiobutton(frm_kjonn, text="Han", variable=var_kjonn, value="Han")
rb_han.pack(side=LEFT, padx=5)
rb_hun = Radiobutton(frm_kjonn, text="Hun", variable=var_kjonn, value="Hun")
rb_hun.pack(side=LEFT, padx=5)
rb_hen = Radiobutton(frm_kjonn, text="Hen", variable=var_kjonn, value="Hen")
rb_hen.pack(side=LEFT, padx=5)
frm_kjonn.grid(row=row_count, column=1, padx=5, pady=5, sticky="W")

#Passordregistrering
row_count+=1
lbl_passord1 = Label(root, text="Velg passord:")
lbl_passord1.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_password1 = Frame(root)
entry_password1 = Entry(frm_password1, show="*", width=30)
entry_password1.pack(side=LEFT, padx=5)

btn_password_reveal1 = Button(frm_password1, image=phIm_ceye, compound=LEFT, width=0)
btn_password_reveal1.name="btn_password_reveal1"
btn_password_reveal1.pack(side=LEFT, padx=5)
frm_password1.grid(row=row_count, column=1, padx=5, pady=5, sticky="W")
#Legger til lyttere på knappen
btn_password_reveal1.bind("<ButtonPress>", btn_password_reveal_press)
btn_password_reveal1.bind("<ButtonRelease>", btn_password_reveal_release)


#Passordregverifisering
row_count+=1
lbl_passord2 = Label(root, text="Velg passord:")
lbl_passord2.grid(row=row_count, column=0, sticky="E", padx=10, pady=5)

frm_password2 = Frame(root)
entry_password2 = Entry(frm_password2, show="*", width=30)
entry_password2.pack(side=LEFT, padx=5)
btn_password_reveal2 = Button(frm_password2, image=phIm_ceye, compound=LEFT, width=0)
btn_password_reveal2.name="btn_password_reveal2"
btn_password_reveal2.pack(side=LEFT, padx=5)
frm_password2.grid(row=row_count, column=1, padx=5, pady=5, sticky="W")
#Legger til lyttere på knappen
btn_password_reveal2.bind("<ButtonPress>", btn_password_reveal_press)
btn_password_reveal2.bind("<ButtonRelease>", btn_password_reveal_release)



# Knapp for validering
row_count+=1
btn_submit = Button(root, text="Registrer", command=valider, width="20")
btn_submit.grid(row=row_count, column=0, columnspan=2, pady=10)

# Label for resultater eller feilmeldinger
row_count+=1
lbl_resultat = Label(root, text="", font=("Arial", 6))
lbl_resultat.grid(row=row_count, column=0, columnspan=2, pady=10)

# Start hovedløkken
root.mainloop()
