from  grafana_api.grafana_face import GrafanaFace

def connectGrafana(authkey,host):
    grafanaconn = GrafanaFace(auth=authkey,host=host)
    return grafanaconn


GRAFANA_NON_PROD_API_KEY = ''
GRAFANA_PROD_API_KEY = ''

grafana_non_prod_conn = 
