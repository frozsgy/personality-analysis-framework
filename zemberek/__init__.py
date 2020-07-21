#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

import grpc

import zemberek.language_id_pb2 as z_langid
import zemberek.language_id_pb2_grpc as z_langid_g
import zemberek.normalization_pb2 as z_normalization
import zemberek.normalization_pb2_grpc as z_normalization_g
import zemberek.preprocess_pb2 as z_preprocess
import zemberek.preprocess_pb2_grpc as z_preprocess_g
import zemberek.morphology_pb2 as z_morphology
import zemberek.morphology_pb2_grpc as z_morphology_g

channel = grpc.insecure_channel('localhost:6789')

langid_stub = z_langid_g.LanguageIdServiceStub(channel)
normalization_stub = z_normalization_g.NormalizationServiceStub(channel)
preprocess_stub = z_preprocess_g.PreprocessingServiceStub(channel)
morphology_stub = z_morphology_g.MorphologyServiceStub(channel)

def find_lang_id(i):
    response = langid_stub.Detect(z_langid.LanguageIdRequest(input=i))
    return response.langId

def tokenize(i):
    response = preprocess_stub.Tokenize(z_preprocess.TokenizationRequest(input=i))
    return response.tokens

def normalize(i):
    response = normalization_stub.Normalize(z_normalization.NormalizationRequest(input=i))
    return response

def analyze(i):
    response = morphology_stub.AnalyzeSentence(z_morphology.SentenceAnalysisRequest(input=i))
    return response