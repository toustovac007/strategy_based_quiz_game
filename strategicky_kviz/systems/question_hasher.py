import hashlib
import json


# tento soubor se doporučuje před publikováním odstranit

questions = [
  {
    "question": "Co znamená zkratka CPU?",
    "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User"],
    "correct": "Central Processing Unit"
  },
  {
    "question": "Jaký jazyk se používá pro stylování webu?",
    "options": ["HTML", "Python", "CSS", "C++"],
    "correct": "CSS"
  },
  {
    "question": "Které číslo je binární zápis čísla 5?",
    "options": ["101", "110", "111", "100"],
    "correct": "101"
  },
  {
    "question": "Co dělá příkaz 'print' v Pythonu?",
    "options": ["Načítá data", "Vypisuje text", "Maže proměnnou", "Ukončuje program"],
    "correct": "Vypisuje text"
  },
  {
    "question": "Jaký typ dat je číslo 3.14 v Pythonu?",
    "options": ["int", "str", "float", "bool"],
    "correct": "float"
  },
  {
    "question": "Co znamená HTML?",
    "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "High Text Machine Language", "Hyper Tool Multi Language"],
    "correct": "Hyper Text Markup Language"
  },
  {
    "question": "Který symbol se používá pro komentář v Pythonu?",
    "options": ["//", "#", "<!-- -->", "/* */"],
    "correct": "#"
  },
  {
    "question": "Co je proměnná?",
    "options": ["Typ funkce", "Místo pro uložení hodnoty", "Druh cyklu", "Operátor"],
    "correct": "Místo pro uložení hodnoty"
  },
  {
    "question": "Který z těchto jazyků je kompilovaný?",
    "options": ["Python", "JavaScript", "C++", "HTML"],
    "correct": "C++"
  },
  {
    "question": "Co je to IP adresa?",
    "options": ["Typ souboru", "Identifikátor zařízení v síti", "Programovací jazyk", "Operační systém"],
    "correct": "Identifikátor zařízení v síti"
  },
  {
    "question": "K čemu slouží operační systém?",
    "options": ["Pouze k hraní her", "Správa hardware a software", "Vytváření webů", "Editace obrázků"],
    "correct": "Správa hardware a software"
  },
  {
    "question": "Jaký je výsledek 2**3 v Pythonu?",
    "options": ["6", "8", "9", "5"],
    "correct": "8"
  },
  {
    "question": "Co znamená zkratka RAM?",
    "options": ["Random Access Memory", "Read Access Memory", "Run Active Memory", "Rapid Access Module"],
    "correct": "Random Access Memory"
  },
  {
    "question": "Jaký datový typ je True/False?",
    "options": ["int", "bool", "str", "float"],
    "correct": "bool"
  },
  {
    "question": "Co dělá funkce len() v Pythonu?",
    "options": ["Vrací délku", "Sčítá hodnoty", "Tiskne text", "Mazá seznam"],
    "correct": "Vrací délku"
  },
  {
    "question": "Co je to loop (cyklus)?",
    "options": ["Podmínka", "Opakování kódu", "Proměnná", "Chyba"],
    "correct": "Opakování kódu"
  },
  {
    "question": "Jaký symbol se používá pro rovnost v Pythonu?",
    "options": ["=", "==", "!=", "<>"],
    "correct": "=="
  },
  {
    "question": "Co je funkce?",
    "options": ["Typ chyby", "Blok kódu, který lze opakovaně volat", "Proměnná", "Operátor"],
    "correct": "Blok kódu, který lze opakovaně volat"
  },
  {
    "question": "Který z těchto je webový prohlížeč?",
    "options": ["Windows", "Chrome", "Python", "Linux"],
    "correct": "Chrome"
  },
  {
    "question": "Co je Git?",
    "options": ["Programovací jazyk", "Systém pro správu verzí", "Operační systém", "Databáze"],
    "correct": "Systém pro správu verzí"
  },
  {
    "question": "Co znamená zkratka URL?",
    "options": ["Uniform Resource Locator", "Universal Reference Link", "User Resource Location", "Unified Routing Link"],
    "correct": "Uniform Resource Locator"
  },
  {
    "question": "Který jazyk běží v prohlížeči?",
    "options": ["Python", "C++", "JavaScript", "Java"],
    "correct": "JavaScript"
  },
  {
    "question": "Co je API?",
    "options": ["Typ paměti", "Rozhraní pro komunikaci mezi programy", "Databáze", "Programovací jazyk"],
    "correct": "Rozhraní pro komunikaci mezi programy"
  },
  {
    "question": "Jaký příkaz v Pythonu vytvoří seznam?",
    "options": ["{}", "[]", "()", "<>"],
    "correct": "[]"
  },
  {
    "question": "Co znamená 'bug' v programování?",
    "options": ["Funkce", "Chyba v kódu", "Typ proměnné", "Editor"],
    "correct": "Chyba v kódu"
  },
  {
    "question": "Co je databáze?",
    "options": ["Program", "Uložiště dat", "Operační systém", "Typ souboru"],
    "correct": "Uložiště dat"
  },
  {
    "question": "Který příkaz ukončí cyklus v Pythonu?",
    "options": ["stop", "exit", "break", "end"],
    "correct": "break"
  },
  {
    "question": "Co je algoritmus?",
    "options": ["Program", "Postup řešení problému", "Chyba", "Paměť"],
    "correct": "Postup řešení problému"
  },
  {
    "question": "Jaký je výsledek 10 // 3 v Pythonu?",
    "options": ["3.33", "3", "4", "1"],
    "correct": "3"
  },
  {
    "question": "Co znamená zkratka SSD?",
    "options": ["Solid State Drive", "Super Speed Disk", "System Storage Device", "Secure Storage Data"],
    "correct": "Solid State Drive"
  },
  {
    "question": "Co znamená zkratka GPU?",
    "options": ["Graphics Processing Unit", "General Processing Unit", "Graphical Power Unit", "Global Processing Unit"],
    "correct": "Graphics Processing Unit"
  },
  {
    "question": "Jaký port používá HTTP?",
    "options": ["21", "80", "443", "22"],
    "correct": "80"
  },
  {
    "question": "Jaký port používá HTTPS?",
    "options": ["80", "21", "443", "25"],
    "correct": "443"
  },
  {
    "question": "Jaký datový typ je 'hello' v Pythonu?",
    "options": ["int", "str", "bool", "list"],
    "correct": "str"
  },
  {
    "question": "Co dělá funkce input() v Pythonu?",
    "options": ["Vypisuje text", "Načítá vstup od uživatele", "Ukončuje program", "Importuje modul"],
    "correct": "Načítá vstup od uživatele"
  },
  {
    "question": "Jaký symbol se používá pro AND v Pythonu?",
    "options": ["&&", "&", "and", "&&&"],
    "correct": "and"
  },
  {
    "question": "Jaký symbol se používá pro OR v Pythonu?",
    "options": ["||", "|", "or", "++"],
    "correct": "or"
  },
  {
    "question": "Co znamená SQL?",
    "options": ["Structured Query Language", "Simple Query Language", "Standard Question Language", "System Query Logic"],
    "correct": "Structured Query Language"
  },
  {
    "question": "K čemu slouží CSS?",
    "options": ["Logika programu", "Stylování webu", "Databáze", "Backend"],
    "correct": "Stylování webu"
  },
  {
    "question": "Co je to server?",
    "options": ["Klient", "Počítač poskytující služby", "Programovací jazyk", "Databáze"],
    "correct": "Počítač poskytující služby"
  },
  {
    "question": "Co je to klient?",
    "options": ["Server", "Zařízení využívající služby", "Operační systém", "Databáze"],
    "correct": "Zařízení využívající služby"
  },
  {
    "question": "Jaký operátor se používá pro násobení v Pythonu?",
    "options": ["x", "*", "×", "%"],
    "correct": "*"
  },
  {
    "question": "Co znamená JSON?",
    "options": ["JavaScript Object Notation", "Java Source Open Network", "Joint System Object Node", "Java Standard Output Name"],
    "correct": "JavaScript Object Notation"
  },
  {
    "question": "Jaký typ kolekce je seznam v Pythonu?",
    "options": ["immutable", "mutable", "constant", "static"],
    "correct": "mutable"
  },
  {
    "question": "Co dělá metoda append()?",
    "options": ["Mazání položky", "Přidání položky do seznamu", "Třídění seznamu", "Kopírování seznamu"],
    "correct": "Přidání položky do seznamu"
  },
  {
    "question": "Jaký je výsledek 5 % 2?",
    "options": ["2.5", "2", "1", "0"],
    "correct": "1"
  },
  {
    "question": "Co znamená OOP?",
    "options": ["Object Oriented Programming", "Open Object Program", "Original Output Process", "Object Output Protocol"],
    "correct": "Object Oriented Programming"
  },
  {
    "question": "Co je třída (class)?",
    "options": ["Proměnná", "Šablona pro objekty", "Funkce", "Chyba"],
    "correct": "Šablona pro objekty"
  },
  {
    "question": "Co je objekt?",
    "options": ["Instance třídy", "Typ chyby", "Proměnná", "Cyklus"],
    "correct": "Instance třídy"
  },
  {
    "question": "Jaký příkaz importuje modul v Pythonu?",
    "options": ["include", "import", "require", "using"],
    "correct": "import"
  },
  {
    "question": "Co znamená LAN?",
    "options": ["Local Area Network", "Large Area Network", "Long Access Node", "Local Access Network"],
    "correct": "Local Area Network"
  },
  {
    "question": "Co znamená WAN?",
    "options": ["Wide Area Network", "Web Access Node", "Wireless Area Network", "Wide Access Node"],
    "correct": "Wide Area Network"
  },
  {
    "question": "Jaký je výsledek 7 > 3?",
    "options": ["True", "False", "Error", "None"],
    "correct": "True"
  },
  {
    "question": "Jaký je výsledek 3 == 4?",
    "options": ["True", "False", "None", "Error"],
    "correct": "False"
  },
  {
    "question": "Co dělá break?",
    "options": ["Pokračuje cyklus", "Ukončí cyklus", "Restartuje cyklus", "Přeskočí iteraci"],
    "correct": "Ukončí cyklus"
  },
  {
    "question": "Co dělá continue?",
    "options": ["Ukončí program", "Přeskočí iteraci", "Zastaví cyklus", "Restartuje cyklus"],
    "correct": "Přeskočí iteraci"
  },
  {
    "question": "Jaký je výsledek len('abc')?",
    "options": ["2", "3", "4", "1"],
    "correct": "3"
  },
  {
    "question": "Co je dictionary v Pythonu?",
    "options": ["Seznam", "Kolekce klíč-hodnota", "Řetězec", "Číslo"],
    "correct": "Kolekce klíč-hodnota"
  },
  {
    "question": "Jaký symbol používá dictionary?",
    "options": ["[]", "{}", "()", "<>"],
    "correct": "{}"
  },
  {
    "question": "Co znamená IDE?",
    "options": ["Integrated Development Environment", "Internal Data Engine", "Input Device Engine", "Integrated Debug Engine"],
    "correct": "Integrated Development Environment"
  },
  {
    "question": "Co je compiler?",
    "options": ["Překladač kódu", "Editor", "Debugger", "Databáze"],
    "correct": "Překladač kódu"
  },
  {
    "question": "Co je interpreter?",
    "options": ["Překládá kód za běhu", "Editor", "Server", "Database"],
    "correct": "Překládá kód za běhu"
  },
  {
    "question": "Co znamená HTTP?",
    "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol", "Hyper Tool Transfer Program", "Home Transfer Text Protocol"],
    "correct": "HyperText Transfer Protocol"
  },
  {
    "question": "Co znamená HTTPS?",
    "options": ["Secure HTTP", "Simple HTTP", "System HTTP", "Static HTTP"],
    "correct": "Secure HTTP"
  },
  {
    "question": "Jaký je výsledek 4 + 5 * 2?",
    "options": ["18", "14", "13", "10"],
    "correct": "14"
  },
  {
    "question": "Jaký je výsledek (4 + 5) * 2?",
    "options": ["18", "14", "13", "10"],
    "correct": "18"
  },
  {
    "question": "Co je boolean?",
    "options": ["Číslo", "True/False", "Text", "Seznam"],
    "correct": "True/False"
  },
  {
    "question": "Jaký příkaz vypíše proměnnou x?",
    "options": ["echo x", "print(x)", "output x", "write x"],
    "correct": "print(x)"
  },
  {
    "question": "Co znamená loop while?",
    "options": ["Cyklus s podmínkou", "Nekonečný cyklus vždy", "Funkce", "Proměnná"],
    "correct": "Cyklus s podmínkou"
  },
  {
    "question": "Co znamená loop for?",
    "options": ["Cyklus přes kolekci", "Podmínka", "Proměnná", "Funkce"],
    "correct": "Cyklus přes kolekci"
  },
  {
    "question": "Co je index v seznamu?",
    "options": ["Hodnota", "Pozice prvku", "Typ dat", "Funkce"],
    "correct": "Pozice prvku"
  },
  {
    "question": "Jaký je první index v Pythonu?",
    "options": ["1", "0", "-1", "2"],
    "correct": "0"
  },
  {
    "question": "Co znamená None?",
    "options": ["0", "Prázdná hodnota", "False", "Error"],
    "correct": "Prázdná hodnota"
  },
  {
    "question": "Co dělá funkce type()?",
    "options": ["Vrací typ proměnné", "Mění typ", "Maže typ", "Vytváří typ"],
    "correct": "Vrací typ proměnné"
  },
  {
    "question": "Jaký je výsledek 10 / 2?",
    "options": ["5", "5.0", "4", "2"],
    "correct": "5.0"
  },
  {
    "question": "Jaký je výsledek 10 // 2?",
    "options": ["5", "5.0", "4", "2"],
    "correct": "5"
  },
  {
    "question": "Co je string?",
    "options": ["Číslo", "Text", "Boolean", "Seznam"],
    "correct": "Text"
  },
  {
    "question": "Jaký znak ukončuje příkaz v Pythonu?",
    "options": [";", ".", "nic", ":"],
    "correct": "nic"
  }

]

def hash_text(text):
    return hashlib.sha256(text.strip().lower().encode("utf-8")).hexdigest()

output = []

for q in questions:
    output.append({
        "question": q["question"],
        "options": q["options"],
        "correct_hash": hash_text(q["correct"])
    })

with open("../data/questions_hashed.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)