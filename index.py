import scattertext as st
from scattertext.external import phrasemachine
import spacy
import pandas as pd
from pprint import pprint
import spacy
from scattertext import SampleCorpora, PhraseMachinePhrases, dense_rank, RankDifference, AssociationCompactor, produce_scattertext_explorer
from scattertext.CorpusFromPandas import CorpusFromPandas

annotations_df = pd.read_csv('ps_dataset1_cleaned.csv')
#print(annotations_df.iloc[0])

nlp = spacy.load("en_core_web_sm")

corpus = st.CorpusFromPandas(annotations_df, 
                            category_col='category',
                            text_col='annotation_text', 
                            nlp=nlp).build()

#print(list(corpus.get_scaled_f_scores_vs_background().index[:10]))

#Class
term_freq_df = corpus.get_term_freq_df()

term_freq_df['Class Score'] = corpus.get_scaled_f_scores('Class')
class_score= list(term_freq_df.sort_values(by='Class Score', ascending=False).index[:10])

#Gender
term_freq_df['Gender Score'] = corpus.get_scaled_f_scores('Gender')
gender_score = list(term_freq_df.sort_values(by='Gender Score', ascending=False).index[:10])

#Pandemics
term_freq_df['Pandemics Score'] = corpus.get_scaled_f_scores('Pandemics')
pandemics_score=list(term_freq_df.sort_values(by='Pandemics Score', ascending=False).index[:10])

#Race
term_freq_df['Race Score'] = corpus.get_scaled_f_scores('Race')
race_score = list(term_freq_df.sort_values(by='Race Score', ascending=False).index[:10])

#Religion
term_freq_df['Religion Score'] = corpus.get_scaled_f_scores('Religion')
religion_score = list(term_freq_df.sort_values(by='Religion Score', ascending=False).index[:10])

#Sexuality
term_freq_df['Sexuality Score'] = corpus.get_scaled_f_scores('Sexuality')
sexuality_score = list(term_freq_df.sort_values(by='Sexuality Score', ascending=False).index[:10])

#class graph
class_html = st.produce_scattertext_explorer(corpus, 
            category='Class', 
            category_name = 'Class',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

#gender graph
gender_html = st.produce_scattertext_explorer(corpus, 
            category='Gender', 
            category_name = 'Gender',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

#pandemics graph
pandemics_html = st.produce_scattertext_explorer(corpus, 
            category='Pandemics', 
            category_name = 'Pandemics',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

#Race graph
race_html = st.produce_scattertext_explorer(corpus, 
            category='Race', 
            category_name = 'Race',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

#Religion graph
religion_html = st.produce_scattertext_explorer(corpus, 
            category='Religion', 
            category_name = 'Religion',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

#Religion graph
sexuality_html = st.produce_scattertext_explorer(corpus, 
            category='Sexuality', 
            category_name = 'Sexuality',
            not_category_name='All other categories',
            width_in_pixels=1000,
            metadata=corpus.get_df()['annotated_quote'])

open("Annotation-Visualization-CLASS.html", 'wb').write(class_html.encode('utf-8'))
open("Annotation-Visualization-GENDER.html", 'wb').write(gender_html.encode('utf-8'))
open("Annotation-Visualization-PANDEMICS.html", 'wb').write(pandemics_html.encode('utf-8'))
open("Annotation-Visualization-RACE.html", 'wb').write(race_html.encode('utf-8'))
open("Annotation-Visualization-RELIGION.html", 'wb').write(religion_html.encode('utf-8'))
open("Annotation-Visualization-SEXUALITY.html", 'wb').write(sexuality_html.encode('utf-8'))

