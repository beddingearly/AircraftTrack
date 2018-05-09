DATABASE=./database/2018-4-15.db
TABLE=ident
IDENT=CCA1316 
CSVFILE=out.csv
KMLFILE=out.kml

python gr-air-modes/apps/get_history_track.py \
  --database ${DATABASE} \
  --table ${TABLE} \
  --plane ${IDENT} \
  --csvfile ${CSVFILE} \
  --kmlfile ${KMLFILE}
