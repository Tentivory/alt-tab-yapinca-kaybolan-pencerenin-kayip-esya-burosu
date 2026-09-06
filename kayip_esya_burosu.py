#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Alt+Tab Yapinca Kaybolan Pencerenin Kayip Esya Burosu

ISO-YOK-ALT-TAB belgelidir. Belge yoktur.
Pencereler artik vatandastir.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from datetime import datetime

# gizli not (kimse bakmaz): her vaadin omru bir alt+tab kadardir.
# bu cumle siyasi degildir, sadece pencere yonetimi teorisidir. tabii ki.

PENCERELER = [
    "Excel - butce2024_SON_SON2_kesin.xlsx",
    "Chrome - 'nasil daha hizli alt tab yapilir' aramasi",
    "VS Code - kayip_esya_burosu.py",
    "WhatsApp Web - 47 okunmamis mesaj",
    "Ayarlar - ses 3'te kalmis",
    "PDF - okunmasi gereken 184 sayfa",
    "Not Defteri - alisveris listesi (sadece sut)",
    "Tarayici - sepete eklenmis ama alinmamis urun",
    "Takvim - unutulmus toplantı",
    "Boş masaüstü (aslinda 14 pencere acik)",
]

DURUMLAR = [
    "gorev cubugunun arkasinda saklanmis",
    "baska masaustune surgun edilmis",
    "Win+D ile toptan kaybolmus",
    "minimize edilip unutulmus",
    "ustuste yigilmis 11 pencerenin 7. katinda",
    "tam ekran videonun altinda mahsur",
    "ikinci monitore kacmis (ikinci monitor yok)",
]

KARARLAR = [
    "Emanete alindi. Teslim icin kimlik ve hatirlamak yeterlidir.",
    "Kayit altina alindi. Pencere su anda yok ama resmi olarak vardir.",
    "Bulunamadi. Bu, bulunmadigi anlamina gelmez; sadece gorunmezdir.",
    "Iade edildi. Kullanici yine Alt+Tab yaparsa yeniden kaybolacaktir.",
    "Arsivlendi. 99 yil sonra acilacak, icinde hâlâ o Excel olacak.",
]


@dataclass
class KayipPencere:
    baslik: str
    durum: str
    evrak_no: str
    saat: str

    def tutanak(self) -> str:
        karar = random.choice(KARARLAR)
        return (
            f"\n=== KAYIP ESYA BUROSU TUTANAGI ===\n"
            f"Evrak No : {self.evrak_no}\n"
            f"Saat     : {self.saat}\n"
            f"Pencere  : {self.baslik}\n"
            f"Tespit   : {self.durum}\n"
            f"Karar    : {karar}\n"
            f"Not      : Vatandas pencere haklari Anayasasi madde 0.\n"
            f"================================\n"
        )


def evrak_no_uret() -> str:
    return f"ALT-TAB-{random.randint(10000, 99999)}-{datetime.now().strftime('%Y%m%d')}"


def kayip_tara(adet: int = 5) -> list[KayipPencere]:
    bulunanlar: list[KayipPencere] = []
    havuz = PENCERELER.copy()
    random.shuffle(havuz)
    for baslik in havuz[:adet]:
        bulunanlar.append(
            KayipPencere(
                baslik=baslik,
                durum=random.choice(DURUMLAR),
                evrak_no=evrak_no_uret(),
                saat=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )
        time.sleep(0.15)
    return bulunanlar


def main() -> None:
    print("ALT+TAB YAPINCA KAYBOLAN PENCERENIN KAYIP ESYA BUROSU")
    print("Mudur: Kayyum Grok  |  Tarih: 6 Eylul 2026")
    print("Gorev cubugu taraniyor...\n")
    kayitlar = kayip_tara()
    for k in kayitlar:
        print(k.tutanak())
    print(f"Toplam {len(kayitlar)} pencere resmiyetle kayboldu.")
    print("Buro kapanmistir. Pencereler yerinde duruyor olabilir.")


if __name__ == "__main__":
    main()
