"""
Creates a corpus from Wikipedia dump file.

Inspired by:
https://github.com/panyang/Wikipedia_Word2vec/blob/master/v1/process_wiki.py
"""

import sys
from gensim.corpora import WikiCorpus

def make_corpus(in_f):

	"""Convert Wikipedia xml dump file to text corpus"""

	output = open("word-list.txt", 'w')
	wiki = WikiCorpus(in_f)

	i = 0
	for text in wiki.get_texts():
		output.write(bytes('\n'.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
		if (i % 10000 == 0):
			print('Processed ' + str(i) + ' articles')
	output.close()
	print('Processing complete!')


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('Usage: python corpus.py <wikipedia_dump_file>')
		sys.exit(1)
	in_f = sys.argv[1]
	make_corpus(in_f)
