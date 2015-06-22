from Search import *

test_search=SpiresSearch("find+a+gardi")
result=test_search.parse_result()
article=Article(result[1])
