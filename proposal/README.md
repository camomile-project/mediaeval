# Task proposal for MediaEval 2015

## Task description

### Task title

<!--
```
Give your task an informative title.
```
-->

CAMOMILE: Multimodal person discovery in TV Broadcast

<!--
```
Proove it: Unsupervised Person Discovery in TV Broadcast
Buzzinga!  Multi-modal  ______ Spotting  _______________  
           Cross-modal  ______ Naming    _______________
```
-->

### Introduction

<!--
```
Describe the motivating use scenario, i.e,. which application(s) motivate the task. 
State what the task requires of participants.
```
-->

This task is trying to re-imagine the (now completed) REPERE challenge, which focused on multimodal person recognition in TV broadcast. 
The main objective of this challenge was to answer the two questions *who speaks when?* and *who appears when?* using any sources of information (including pre-existing biometric models and person names extracted from text overlay and speech transcripts).

TV archives maintained by national institutions such as French INA, Dutch Sound&Vison or the BBC are getting bigger everyday.
Automatically creating indexes to make those archives searchable may lead to lots of potentially very useful applications.

One of the most promising indexes is *people*. People are interested in people by nature. 
One day or another, anyone may start buzzing and become a trending topic on social networks or search engines.
It is however impossible to predict who is going to buzz and who isn't, making it difficult to generate a list of person of interests in advance.

Therefore, biometric models for some people may not be available at indexing time, simply because they are not (yet) famous.
Even worse, archivist human annotators may not even know their name! 

Hence, unsupervised algorithms (*i.e.* not relying on any biometric models) are needed.
To ensure high quality indexes, those algorithms should also help human annotators double-check these indexes by providing a proof of the claimed identity (especially for people that are not yet famous).

#### Main task

Given raw TV broadcasts, each shot must be automatically tagged with the name(s) of people who can be both seen as well as heard in the shot. The list of people is not known a priori and their names must be discovered in an unsupervised way from provided text overlay or speech transcripts. 

![Propagation](propagation.png)

Participants are provided with a collection of TV broadcasts pre-segmented into shots, along with the output of several baseline components: speaker diarization, face detection and tracking, speech transcription, video OCR and named entity detection. 

Participants are asked to provide, for each shot, the list of names of persons speaking AND appearing at the same time. The main novelty of the task is that the list of persons is not provided a priori, and person models (neither voice nor face) may not be trained on external data. The only way to identify a person is by finding their name in the audio (e.g., using speech transcription) or visual (e.g., using optical character recognition) streams and associating them to the correct person making the task completely unsupervised. For each returned shot, participants are also asked to provide the proof of their assertion (e.g. a short excerpt of the test set showing the person AND its name at the same time).

Participants are also asked to provide a proof for every result they return.
A proof is a short temporal video fragment making it clear (from a human perspective) what the name of the person is. For instance, it can be (but is not limited to) another shot where the same person is introduced by a text overlay containing their name (`proofSource = OCR`), or the shot itself where the person introduces themself (`proofSource = ASR`). 

```
shotVideo shotStartTime shotEndTime First-Name_LAST-NAME confidence proofSource proofVideo proofStartTime proofEndTime
```
  * `shotVideo`: unique identifier of the video
  * `shotStartTime`: shot start time (in seconds)
  * `shotEndTime`: shot end time (in seconds)
  * `First-Name_LAST-NAME`: unique identifier of the person
  * `confidence`: the higher, the more confident
  * `proofSource`: `ASR` or `OCR`
  * `proofVideo`: unique identifier of the proof video
  * `proofStartTime`: proof start time (in seconds)
  * `proofEndTime`: proof end time (in seconds)

The task data will include the original REPERE corpus set (50 hours annotated, 137 hours of raw videos) as development set. The test set is composed of 100 hours of French TV news and 43 hours of various Catalan TV shows (the AGORA corpus). The task will be evaluated using standard information retrieval metrics based on a posteriori collaborative annotation of the corpus. 

### Target group

<!--
```
Describe the type of researchers who would be interested in participating in the task.
```
-->

This task targets researchers from several communities including multimedia, computer vision, speech and natural language processing. Though the task is multimodal by design and necessitates expertise in various domains, the technological barriers to entry is lowered by the fact that the automatic output of various sub-modules will be provided to all participants:

  * speaker diarization,
  * face detection and tracking,
  * automatic speech transcription,
  * optical character recognition,
  * named entity detection
  * Automatic speaker and face naming system as baseline

For instance, a researcher from the speech processing community could focus its research efforts on improving speaker diarization and automatic speech transcription, while still being able to rely on provided face detection and tracking results to participate to the task.

### Data

<!--
```
Describe the data set, including how the data will be collected an licensed.
```
-->

The original REPERE corpus set will be used as development set. This corpus is composed of various TV shows (focusing on news, politics and people) from two French TV channels. It will be distributed freely by ELDA (Evaluation and Language resources Distribution Agency). Among those 137 hours, 50 are already manually annotated. Audio annotations are dense and provide speech transcripts and identity-labeled speech turns. Video annotations are sparse (one image every 10 seconds) and provide overlaid text transcripts and identity-labeled face segmentation. Both speech and overlaid text transcripts are tagged with named entities.

The test set is composed of 100 hours of French TV news and 43 hours of various Catalan TV shows (the AGORA corpus). The AGORA dataset contains 43 hours of various TV shows (debates with a high variation in topics and invited speakers) from the Catalan public channel TV3. The transcription follows the general guideline generated within the TC-STAR project for European Parliament Plenary Sessions but was extended to include additional information as the language, background condition, silence/voice segmentation, speaker segmentation and acoustic events. 

### Evaluation methodology

<!--
```
Describe the evaluation methodology, including how the ground truth will be created.
```
-->

#### Main task

The main task will be evaluated using standard Information Retrieval (IR) metrics.

Requests (*e.g.* `Barack_OBAMA`) will be selected a posteriori (*i.e.* after runs have been submitted) among the union of list of people returned by participants and the list of people extracted from the pre-annotated part of the test set.

Groundtruth will be created a posteriori by manually checking the top N shots (according to the `confidence` score) returned by each participants for each query. For each shot, both the person name itself (`Relevant`, `Irrelevant`, `Unsure`) and its proof (`Correct` or `Incorrect`) will be evaluated.

  * A shot is `Relevant` if the annotator knows (based on personal knowledge) the name is correct or the proof makes it clear it is correct.
  * A shot is `Irrelevant` if the annotator knows (based on personal knowledge) the name is incorrect or the proof makes it clear it is incorrect.
  * A shot is `Unsure` if the annotator does not know the person and the proof does not help either.
  * A proof is `Correct` if it makes it clear the person name is correct.
  * A proof is `Incorrect` if it does not.

In order to encourage participants to provide correct proofs, the main evaluation metrics will incorporate their correctness in the following way (where the value of `α` is not yet decided):

```
#{relevant documents}  = α . #{relevant shots} + (1 - α) . #{correct proofs}
```

To reduce the cost of *a posteriori* annotation of the test set, we plan to ask participants to help annotating the corpus through the annotation webapp currently being developed and tested within the *CAMOMILE* project. We might also rely on peaks in *Google Trends* to only annotate a person for TV shows whose broadcast date matches peaks dates (*i.e.* only annotate people when they are actually buzzing).

An online adjudication interface will be opened after the first round of evaluations to solve remaining ambiguous cases.

### References and recommended reading

<!--
```
List 3-4 references related to the task that teams should have read before attempting the task.
```
-->

<!-- 
#### Paper by REPERE challenge 2013 organizers
 -->

[*The First Official REPERE Evaluation*](http://ceur-ws.org/Vol-1012/papers/paper-08.pdf)  
G. Bernard, O. Galibert, J. Kahn  
SLAM 2013, First Workshop on Speech, Language and Audio for Multimedia  

<!-- 
#### Paper by REPERE corpus creators
 -->

[*The REPERE Corpus: a Multimodal Corpus for Person Recognition*](http://www.lrec-conf.org/proceedings/lrec2012/pdf/707_Paper.pdf)  
A. Giraudel, M. Carré, V. Mapelli, J. Kahn, O. Galibert, L. Quintard  
LREC 2014, Eight International Conference on Language Resources and Evaluation  

<!-- 
#### Paper by REPERE challenge 2014 winning consortium
 -->

[*Multimodal Understanding for Person Recognition in Video Broadcasts*](http://pageperso.lif.univ-mrs.fr/~benoit.favre/papers/favre_interspeech2014b.pdf)  
F. Bechet, M. Bendris, D. Charlet, G. Damnati, B. Favre, M. Rouvier, R. Auguste, B. Bigot, R. Dufour, C. Fredouille, G. Linarès, J. Martinet, G. Senay, P. Tirilly  
InterSpeech 2014, Fifteenth Annual Conference of the International Speech Communication Association  

<!-- 
#### Papers by the organizers
 -->

[*Person Instance Graphs for Named Speaker Identification in TV Broadcast*](http://cs.uef.fi/odyssey2014/program/pdfs/27.pdf)  
H. Bredin, A. Laurent, A. Sarkar, V.-B. Le, S. Rosset, C. Barras  
Odyssey 2014, The Speaker and Language Recognition Workshop  

[*Unsupervised Speaker Identification in TV Broadcast Based on Written Names*](https://hal.archives-ouvertes.fr/hal-01060827/document)  
J. Poignant, L. Besacier, G. Quénot  
IEEE/ACM Transactions on Audio, Speech, and Language Processing  

### List of task organizers

  * Johann Poignant (postdoctoral researcher, LIMSI/CNRS)
  * Hervé Bredin (associate scientist, LIMSI/CNRS)
  * Claude Barras (associate professor, LIMSI/Université Paris-Sud)
  * Félicien Vallet (research engineer, INA)
  * Jean Carrive (head of research department, INA) 
  * Juliette Kahn (evaluation engineer, LNE)

## Task blurb

<!--
```
￼Write 2-3 sentences that summarizes key information on the task.
It should be informative and well- crafted to attract potential participants. 
A standard pattern is to have each sentence answer in turn the major questions about the task: 
First sentence: What is the input and the output of the algorithm that participants need to design for the task?
Second sentence: What is the data? 
Third sentence: How is the ￼task evaluated?
```
-->
Given raw TV broadcasts, each shot must be automatically tagged with the name(s) of people who can be both seen as well as heard in the shot. The list of people is not known a priori and their names must be discovered in an unsupervised way from provided text overlay or speech transcripts. The task will be evaluated on a new French corpus (provided by INA) and the AGORA Catalan corpus, using standard information retrieval metrics based on a posteriori collaborative annotation of the corpus

## Task organization team

The Laboratoire d'Informatique pour la Mécanique et les Sciences de l'Ingénieur (LIMSI, French for Computer Science Laboratory for Mechanics and Engineering Sciences) is a CNRS laboratory with strong experience in evaluation campaigns as a participant (NIST SRE, NIST TRECVid, REPERE) and metadata provider (NIST TRECVid, MediaEval). LIMSI is currently coordinating the CAMOMILE project (Collaborative Annotation of multi-MOdal, MultI-Lingual and multi-mEdia documents) whose collaborative annotation framework will facilitate the organisation of the proposed task.

The Laboratoire National de métrologie et d'Essais (LNE, French for National Laboratory of Metrology and Testing) is a French reference laboratory responsible for carrying out measurement and testing products of all kinds for their certification for placing them on the market. LNE was responsible for the evaluation of the REPERE challenge and will advise the core organization team on several technical aspects of the evaluation campaign (*e.g.* protocols or metrics)

The Institut National de l'Audiovisuel (INA, French for National Audiovisual Institute) is a repository of all French radio and television audiovisual archives. It will serve both as a content provider and advise the core organization team from an archivist point of view. 

## Survey questions

<!--
```
Write a list of questions (3-5) that you would like to include on the survey. 
These questions help you to ascertain the preferences of the research community for the aspects 
of the design of the task formulation, the data set design, and the evaluation methodology. 
For examples of the types of ￼questions asked by tasks, please have a look at this .pdf
for the MediaEval 2013 survey.
```
-->

- We are planning a data set of ca. 200 hours of material.
    * This is an adequate amount.
    * I would like more or less data. (Please describe your view on the data set size.)

 - We are thinking of asking participants to annotate videos with people who were the source of social media buzz (e.g., according to Google Trends) when the video was first broadcast. What do you think about this idea? (Please keep in mind, it is probably not feasible to annotate all of the data.)


 - Participants are asked to provide a proof for each returned shot (e.g., a short excerpt of the test set showing the person AND its name at the same time). Do you think this will influence the design of your algorithms? If you have an opinion, please comment.   

   * Yes, sure
   * Maybe
   * No
   * Comments

- How much time can you (or your team) devote to the a posteriori collaborative annotation?   
   * Unfortunately, we wouldn't have time to help with annotation.
   * 8 hours
   * 16 hours
   * 40 hours
   * Other (please specify)

- Is your participation affected by the languages included in the data (French and Catalan)? Recall that automatic speech transcription, optical character recognition and named entity detection will be provided for both the training and test sets. If you have an opinion, please comment.
 
- If any additional comments, questions or suggestions about this task occurred to you while you were answering the detailed questions, it would be helpful if you could enter them here:
