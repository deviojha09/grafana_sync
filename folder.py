from  grafana_api.grafana_face import GrafanaFace

def connectGrafana(authkey,host):
    grafanaconn = GrafanaFace(auth=authkey,host=host)
    return grafanaconn


GRAFANA_NON_PROD_API_KEY = '<api_key>'
GRAFANA_NON_PROD_HOST = '<host>'
GRAFANA_PROD_API_KEY = '<api_key>'
GRAFANA_PROD_HOST = '<host>'
FOLD
#creating foler in non-prod
grafana_non_prod_conn = connectGrafana(GRAFANA_NON_PROD_API_KEY,GRAFANA_NON_PROD_HOST)
title = "Linux Metrics"
#In the cerate folder fucnction if we just pass the title Grafna will create the folder and internally generate a UID for same
status = grafana_non_prod_conn.folder.create_folder(title=title)
print(status)

#Once the folder is created successfully in non-prod get the UID of the folder, u can use GUI too
#getting all folder names and  UID from non-prod

folder_details = grafana_non_prod_conn.folder.get_all_folders()
folder_dict = {}
for folder in folder_details:
    folder_dict[folder['title']]=folder['uid']
for i in folder_dict:
    print(i,folder_dict[i])
    
#Once we get the the folder UID from Non prod use the same foder ID while cerating the folder in PROD 
uid = folder_dict[title] #get the folder UID
grafana_prod_conn = connectGrafana(GRAFANA_PROD_API_KEY,GRAFANA_PROD_HOST)
status = grafana_prod_conn.folder.create_folder(title=title,uid=uid)
print(status)

#Please note that, u can pass your own menaingfull UID too, and pass same while cerating in non-prod and prod if you dont
#want to use the grafana auto generated ones.

    
