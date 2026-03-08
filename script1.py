tfs=int(input("Qual é o seu tempo final em segundos?: "))
tis=int(input("Qual é o seu tempo inicial em segundos?: "))
dfm=int(input("Qual é a sua distância final em metros?: "))
dim=int(input("Qual é a sua distância em inicial em metros?: "))
dlt_ts=tfs-tis
dlt_dm=dfm-dim
vel_med_ms=dlt_dm/dlt_ts
vel_med_kmh=vel_med_ms*3.6
round(vel_med_ms, 2)
round(vel_med_kmh, 2)
print(f"Sua velocidade média em m/s é {vel_med_ms}m/s !")
print(f"Sua velocidade média em km/h é {vel_med_kmh}km/h !")