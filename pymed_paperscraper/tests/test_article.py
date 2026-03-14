import xml.etree.ElementTree as ET

from pymed_paperscraper import PubMed
from pymed_paperscraper.article import PubMedArticle


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


def test_inline_tags_are_preserved_in_title_and_abstract():
	article_xml = ET.fromstring(
		"""
		<PubmedArticle>
		  <MedlineCitation>
		    <Article>
		      <ArticleTitle><i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import</ArticleTitle>
		      <Abstract>
		        <AbstractText>Remodeling <i>Yersinia pseudotuberculosis</i> to generate a highly immunogenic outer membrane vesicle vaccine against pneumonic plague.</AbstractText>
		      </Abstract>
		    </Article>
		  </MedlineCitation>
		  <PubmedData>
		    <ArticleIdList>
		      <ArticleId IdType="pubmed">123456</ArticleId>
		    </ArticleIdList>
		    <History>
		      <PubMedPubDate PubStatus="pubmed">
		        <Year>2022</Year>
		        <Month>03</Month>
		        <Day>12</Day>
		      </PubMedPubDate>
		    </History>
		  </PubmedData>
		</PubmedArticle>
		"""
	)

	article = PubMedArticle(xml_element=article_xml)

	assert article.title == (
		"TIC236 gain-of-function mutations unveil the link between plastid division "
		"and plastid protein import"
	)
	assert article.abstract == (
		"Remodeling Yersinia pseudotuberculosis to generate a highly immunogenic "
		"outer membrane vesicle vaccine against pneumonic plague."
	)
