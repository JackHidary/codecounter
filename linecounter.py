

from google.cloud import bigquery as bq



def linecount():

  client = bq.Client()
  query="SELECT * FROM [bigquery-public-data:github_repos.sample_contents] LIMIT 100"     
  query_results = client.run_sync_query(query)





def main():

  linecount()



main():
