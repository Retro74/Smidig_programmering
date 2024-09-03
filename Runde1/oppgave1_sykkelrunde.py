# 1. Initielle startvariabler
radius = 31.83
langside = 100
gjennomsnittsfart_km_t = 50

# 2. Beregninger
gjennomsnittsfart_m_s = gjennomsnittsfart_km_t / 3.6
baneOmkrets = 2* langside + 2*3.14*radius
tid_10_runder_sek = (baneOmkrets*10)/gjennomsnittsfart_m_s 
tid_10_runder_min = tid_10_runder_sek // 60
tid_10_runder_sek = tid_10_runder_sek % 60

# 3. Visning
print(f"Banen er {baneOmkrets:.1f} meter lang")
print(f"Syklisten sykler med en gjennomsnittsfart på {gjennomsnittsfart_m_s:.1f} m/s")
print(f"Sykelisten bruker {tid_10_runder_min:.0f} minutter og {tid_10_runder_sek:.0f} sekunder på 10 runder.")
