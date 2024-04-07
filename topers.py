from operator import itemgetter

def money_form(mon):
    mon = str(mon)
    idd = -1
    ctr = 1
    rez = ""
    for i in range(len(mon)):
        if ctr == 4:
            ctr = 1
            rez += ","
        rez += mon[idd]
        ctr += 1
        idd -= 1

    rez = rez[::-1]
    return rez

def top_do1(kkk, People, idd_cool, name):
    idd = 0
    dc = {}
    for i, y in People.items():
        if idd == 0:
            pass
        else:
            if name not in y.keys():
                pass
            else:
                dc[i]=y[name]

        idd+=1

    sorted_tuple = dict(sorted(dc.items(), key=itemgetter(1), reverse=True))
    #sorted_tuple = dict(reversed(sorted_tuple.items()))

    ufff = ""
    sml=""
    if name == "balance":
        ufff = "балансу"
        sml = "💰"
    if name == "boss_hp":
        ufff = "нанесённому урону боссу"
        sml = ""
    if name == "bitcoin":
        ufff = "фиткоину"
        sml = ""
    if name == "promo":
        ufff = "промокодам"
        sml = ""
    if name == "icecream":
        ufff = "мороженому"
        sml = ""

    txt = f"топ лист по {ufff}:\n\n"
    idd = 1
    for i,y in sorted_tuple.items():
        if idd_cool == -1001806713364:
            mention = "<a href='https://t.me/True_gb_bot'>" + People[i]['name'] + "</>"
        else:
            mention = "<a href='tg://user?id=" + i + "'>" + People[i]['name'] + "</>"
            mention = "<a href='tg://openmessage?user_id=" + i + "'>" + People[i]['name'] + "</>"

        txt_let1 = ""
        txt_let2 = ""
        if People[i]['state_prem']['true'] == 1:
            if People[i]['state_prem']['name'] == "Флэш":
                txt_let1 = "<b>"
                txt_let2 = "</b>"
        if idd == 1:
            txt += f"1️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 2:
            txt += f"2️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 3:
            txt += f"3️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 4:
            txt += f"4️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 5:
            txt += f"5️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 6:
            txt += f"6️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 7:
            txt += f"7️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 8:
            txt += f"8️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 9:
            txt += f"9️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} \n"
        if idd == 10:
            txt += f"1️⃣0️⃣ {txt_let1}{mention}{txt_let2} — {money_form(y)} "

        if kkk == i:
            txt_num = ""
            for i in str(idd):
                if i == "1":
                    txt_num += "1️⃣"
                if i == "2":
                    txt_num += "2️⃣"
                if i == "3":
                    txt_num += "3️⃣"
                if i == "4":
                    txt_num += "4️⃣"
                if i == "5":
                    txt_num += "5️⃣"
                if i == "6":
                    txt_num += "6️⃣"
                if i == "7":
                    txt_num += "7️⃣"
                if i == "8":
                    txt_num += "8️⃣"
                if i == "9":
                    txt_num += "9️⃣"
                if i == "0":
                    txt_num += "0️⃣"
            tp = f"\n\n{txt_num}.{txt_let1}{mention}{txt_let2} — {money_form(y)}"
        idd+= 1


    txt += tp
    return txt


def top_robby(kkk, People):
    idd = 0
    dc = {}
    for i, y in People.items():
        if idd == 0:
            pass
        else:
            if "balance" not in y.keys():
                pass
            else:
                dc[i]=y["balance"]

        idd+=1

    sorted_tuple = dict(sorted(dc.items(), key=itemgetter(1), reverse=True))
    #sorted_tuple = dict(reversed(sorted_tuple.items()))

    idd = 1
    txt = {}
    for i,y in sorted_tuple.items():
        txt_let1 = ""
        txt_let2 = ""
        if People[i]['state_prem']['true'] == 1:
            if People[i]['state_prem']['name'] == "Флэш":
                txt_let1 = "<b>"
                txt_let2 = "</b>"
        txt[i] = y
        idd+= 1

        if idd == 11:
            break

    return txt
