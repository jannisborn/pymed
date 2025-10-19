from pymed_paperscraper import PubMed


def test_unique_id():
	pubmed = PubMed(tool="MyTool", email="my@email.address")
	query = '((Haliaeetus leucocephalus[Title/Abstract])) AND ((prey[Title/Abstract]) OR (diet[Title/Abstract]))'
	results = pubmed.query(query, max_results=30)

	for r in results:
		ids = r.pubmed_id.strip().split("\n")
		assert len(ids) == 1

def test_unique_doi():
	pubmed = PubMed(tool="MyTool", email="my@email.address")
	query = '((Haliaeetus leucocephalus[Title/Abstract])) AND ((prey[Title/Abstract]) OR (diet[Title/Abstract]))'
	results = pubmed.query(query, max_results=30)

	for r in results:
		if r.doi is None:
			continue
		dois = r.doi.strip().split("\n")
		assert len(dois) == 1