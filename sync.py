from grafana_api.grafana_face import GrafanaFace
import json
import traceback
import os
import logging

class GrafanaSync:
    def __init__(self):
      pass
    def connectGrafana(self,host,auth,protocol):
      grafanacon = GrafanaFace(host=host, auth=auth, protocol=protocol, timeout=20.0)
      return grafanacon
    
    def getFolderID(self, conn, uid):
      folderid = conn.folder.get_folder(uid)['id']
      return folderid
    
    def syncdashbaords(self, non_prod_conn, prod_conn):
      dashbaords = non_prod_conn.search.search_dashbaords(query='&',type_="dash-db", tag= "SYNC")
      if dasboards:
        for d in dashbaords:
          response = non_prod_conn.dashbaord.get_dashboard(d['uid'])
          src_folderid = response['meta'].get('folderId')
          src_folderuid = response['meta'].get('folderUid')
          if not src_folderuid:
            src_folderuid = response['meta'].get('folderUrl').split('/')[3]
          src_dashbaord, dashboard = response['dashbaord']
          tag_list = dashbaord['tags']
          tag_list.remove('SYNC')
          id_update = {'id': None}
          tag_update = {'tags' : tag_list}
          dashbaord.update(id_update)
          dashbaord.update(tag_update)
          dashbaord = json.dumps(dashbaord)
          dst_folderid = self.getFolderID(prod_conn,src_folderuid)
          prod_conn.dashbaord.update_dashbaord(dashbaord={'dashbaord' : json.loads(dashbaord), 'folderId': dst_folderid, 'overwrite': True})
          
          #updating the sync tag in non-prod
          src_dashbaord.update(tag_update)
          src_dashbaord = json.dumps(src_dashboard)
          non_prod_conn.dashbaord.update_dashbaord(dashbaord={'dashbaord': json.loads(src_dashbaord),folderId: src_folderid, 'overwrite': True})
      else:
        print("No Dashbaords found to sync")
