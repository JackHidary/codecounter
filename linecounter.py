from google.cloud import bigquery as bq

ID_INDEX = 0
SIZE_INDEX = 1
CONTENT_INDEX = 2
BINARY_INDEX = 3

def linecount():
  client = bq.Client()
  query="SELECT * FROM [bigquery-public-data:github_repos.sample_contents] WHERE binary = false"
  query_results = client.run_sync_query(query)
  query_results.run(allowLargeResults=True)
  rows, total_rows, page_token = query_results.fetch_data()


  with open("githubFiles.txt", 'w') as outFile:
      for githubFile in rows:
          outFile.write(githubFile[CONTENT_INDEX])


def main():

    linecount()

main()
