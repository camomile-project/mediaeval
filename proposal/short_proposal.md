#The 2015 Multimodal Person Discovery in Broadcast TV

This task is trying to re-imagine the (now completed) REPERE challenge, which focused on multimodal person recognition in TV broadcast. The main objective of this challenge was to answer the two questions "who speaks when?" and "who appears when?" using any sources of information (including pre-existing biometric models and person names extracted from text overlay and speech transcripts).

TV archives maintained by national institutions such as French INA, Dutch Sound&Vison or the BBC are getting bigger everyday. Automatically creating indexes to make those archives searchable may lead to lots of potentially very useful applications.

One of the most promising indexes is people. People are interested in people by nature. One day or another, anyone may start buzzing and become a trending topic on social networks or search engines. It is however impossible to predict who is going to buzz and who isn't, making it difficult to generate a list of person of interests in advance.

Therefore, biometric models for some people may not be available at indexing time, simply because they are not (yet) famous. Even worse, archivist human annotators may not even know their name! 

Hence, unsupervised algorithms (i.e. not relying on any biometric models) are needed. To ensure high quality indexes, those algorithms should also help human annotators double-check these indexes by providing a proof of the claimed identity (especially for people that are not yet famous).

![Propagation](propagation.png)

Given raw TV broadcasts, each shot must be automatically tagged with the name(s) of people who can be both seen as well as heard in the shot. The list of people is not known a priori and their names must be discovered in an unsupervised way from provided text overlay or speech transcripts. 

Participants are provided with a collection of TV broadcasts pre-segmented into shots, along with the output of several baseline components: speaker diarization, face detection and tracking, speech transcription, video OCR and named entity detection. 

Participants are asked to provide, for each shot, the list of names of persons speaking AND appearing at the same time. The main novelty of the task is that the list of persons is not provided a priori, and person models (neither voice nor face) may not be trained on external data. The only way to identify a person is by finding their name in the audio (e.g., using speech transcription) or visual (e.g., using optical character recognition) streams and associating them to the correct person making the task completely unsupervised. For each returned shot, participants are also asked to provide the proof of their assertion (e.g. a short excerpt of the test set showing the person AND its name at the same time).

##Target group
This task targets researchers from several communities including multimedia, computer vision, speech and natural language processing. Though the task is multimodal by design and necessitates expertise in various domains, the technological barriers to entry is lowered by the fact that the automatic output of various sub-modules will be provided to all participants (speaker diarization, face detection and tracking, automatic speech transcription, optical character recognition, named entity detection and an automatic speaker and face naming system as baseline).

For instance, a researcher from the speech processing community could focus its research efforts on improving speaker diarization and automatic speech transcription, while still being able to rely on provided face detection and tracking results to participate to the task.

##Data
The original REPERE corpus set will be used as development set. This corpus is composed of various TV shows (focusing on news, politics and people) from two French TV channels. It will be distributed freely by ELDA (Evaluation and Language resources Distribution Agency). Among those 137 hours, 50 are already manually annotated. Audio annotations are dense and provide speech transcripts and identity-labeled speech turns. Video annotations are sparse (one image every 10 seconds) and provide overlaid text transcripts and identity-labeled face segmentation. Both speech and overlaid text transcripts are tagged with named entities.

The test set is composed of 100 hours of French TV news and 43 hours of various Catalan TV shows (the AGORA corpus). The AGORA dataset contains 43 hours of various TV shows (debates with a high variation in topics and invited speakers) from the Catalan public channel TV3. 

##Ground truth and evaluation
The evaluation will be done on a set of requests (person, video). These requests will be selected a posteriori (i.e. after runs have been submitted) among the union of list of people returned by participants. To create these requests, participants are asked to provide for each person-video a list of shots with an associated confidence score.
 
The person names must have the following format : "first name last name" (in lowercase with only the 26 characters of the latin alphabet without diacritical).

Not to miss shots proposed by participants due to misspellings in person name, we will group the shots of a video where the hypotheses names that are close to the request name (according to the Levenshtein distance and a threshold on this distance). Hypotheses selected are ranked according to the confidence score. 

Groundtruth will be created a posteriori by manually checking the top N shots proposed by participants for each request. To reduce the cost of a posteriori annotation of the test set, we plan to ask participants to help annotating the corpus through the annotation webapp currently being developed and tested within the CAMOMILE project. 

A request will be evaluated by the standard Average Precision which we integrate the correctness of the proof (the value of α is not yet decided): 

{precision of a shot}  = α . {the shot is relevant} + (1 - α) . {the proof is correct}

Not to give too much weight to persons often present in the corpus, we compute the Mean Average Precision of requests on a person and finally compute a Mean Mean Average Precision as global score.

An online adjudication interface will be opened after the first round of evaluations to solve remaining ambiguous cases.

##Recommended reading
[1] G. Bernard, O. Galibert, J. Kahn. The First Official REPERE Evaluation. SLAM 2013, First Workshop on Speech, Language and Audio for Multimedia. 
http://ceur-ws.org/Vol-1012/papers/paper-08.pdf

[2] A. Giraudel, M. Carré, V. Mapelli, J. Kahn, O. Galibert, L. Quintard. The REPERE Corpus: a Multimodal Corpus for Person Recognition. LREC 2014, Eight International Conference on Language Resources and Evaluation  
http://www.lrec-conf.org/proceedings/lrec2012/pdf/707_Paper.pdf

[3] F. Bechet, M. Bendris, D. Charlet, G. Damnati, B. Favre, M. Rouvier, R. Auguste, B. Bigot, R. Dufour, C. Fredouille, G. Linarès, J. Martinet, G. Senay, P. Tirilly. Multimodal Understanding for Person Recognition in Video Broadcasts. InterSpeech 2014, Fifteenth Annual Conference of the International Speech Communication Association  
http://pageperso.lif.univ-mrs.fr/~benoit.favre/papers/favre_interspeech2014b.pdf

[4] H. Bredin, A. Laurent, A. Sarkar, V.-B. Le, S. Rosset, C. Barras. Person Instance Graphs for Named Speaker Identification in TV Broadcast. Odyssey 2014, The Speaker and Language Recognition Workshop  
http://cs.uef.fi/odyssey2014/program/pdfs/27.pdf

[5] J. Poignant, L. Besacier, G. Quénot. Unsupervised Speaker Identification in TV Broadcast Based on Written Names. IEEE/ACM Transactions on Audio, Speech, and Language Processing 
https://hal.archives-ouvertes.fr/hal-01060827/document

##Task organizers
  * Johann Poignant, postdoctoral researcher at LIMSI/CNRS, France
  * Hervé Bredin, associate scientist at LIMSI/CNRS, France
  * Claude Barras, associate professor at LIMSI/Université Paris-Sud, France

##Task auxiliaries <delete this if you have no auxiliaries>
  * Félicien Vallet, research engineer at INA, France
  * Jean Carrive, head of research department at INA, France
  * Juliette Kahn, evaluation engineer at LNE, France
  * Javier Hernando, UPC, Spain

##Task schedule
 - 1 April: Development data release
 - 1 May: Test data release
 - 1 July: Run submission
 - 28 August: Working notes paper deadline
 - 14-15 September MediaEval 2015 Workshop

##Acknowledgments
https://camomile.limsi.fr/




