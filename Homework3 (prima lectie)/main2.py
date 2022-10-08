from datetime import datetime

acum = datetime.now()
dt_string = acum.strftime("%d/%m/%Y %H:%M:%S")
print("La moment, ziua si ora sunt: ", dt_string)
