import utils.preprocess
import zemberek


orig = "RT @ODTUKuzeyKibris: Aynı gökyüzü altında ama birbirinden uzak ODTÜ'lülere; https://t.co/Y9MWOCdvgY via @YouTube"

orig = "ya işte ben de dedim ki bu ış boyle olmaz kank braeber gitmmz lazım oraya. o da sinemaya gelecekse gidelim yoksa buiş en baştan yatar yani. tmmsa gidelim?"


text = utils.preprocess.preprocess(orig)

print("-" * 80)
print("original    : " + orig)
print("-" * 80)
print("preprocessed: " + text)
print("-" * 80)


try :
	lang_id = zemberek.find_lang_id(text)
	print("Language of [" + text + "] is: " + lang_id)

	print("-" * 80)
	tokenization_input = text
	print('Tokens for input : ' + tokenization_input)
	tokens = zemberek.tokenize(tokenization_input)
	for t in tokens:
	    print(t.token + ':' + t.type)

	print("-" * 80)
	normalization_input = text
	print('Normalization result for input : ' + normalization_input)
	n_response = zemberek.normalize(normalization_input)
	if n_response.normalized_input:
	    print(n_response.normalized_input)
	else:
	    print('Problem normalizing input : ' + n_response.error)

	print("-" * 80)
	analysis_input = text
	print('Analysis result for input : ' + analysis_input)
	analysis_result = zemberek.analyze(analysis_input)
	for a in analysis_result.results:
	    best = a.best
	    lemmas = ""
	    for l in best.lemmas:
	        lemmas = lemmas + " " + l
	        print("Word = " + a.token + ", Lemmas = " + lemmas + ", POS = [" + best.pos + "], Full Analysis = {" + best.analysis + "}")

except zemberek.grpc._channel._InactiveRpcError:
    print("Cannot communicate with Zemberek, exiting.")
    exit()