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
The main objective of this challenge was to answer the two questions **who speaks when?** and **who appears when?** using any sources of information (including pre-existing biometric models and person names extracted from text overlay and speech transcripts).

TV archives maintained by national institutions such as French INA, Dutch Sound&Vison or the BBC are getting bigger everyday.
Automatically creating indexes to make those archives searchable may lead to lots of potentially very useful applications.

One of the most promising indexes is **people**. People are interested in people by nature. 
One day or another, anyone may start buzzing and become a trending topic on social networks or search engines.
It is however impossible to predict who is going to buzz and who isn't, making it difficult to generate a list of person of interests in advance.

Therefore, biometric models for some people may not be available at indexing time, simply because they are not (yet) famous.
Even worse, archivist human annotators may not even know their name! 

Hence, unsupervised algorithms (*i.e.* not relying on any biometric models) are needed.
To ensure high quality indexes, those algorithms should also help human annotators double-check these indexes by providing a proof of the claimed identity (especially for people that are not yet famous).

#### Main task

Given a collection of TV broadcasts pre-segmented into shots, participants are asked to provide, for each shot, the list of names of persons speaking AND appearing at the same time.

The main novelty is that the list of persons is not provided *a priori* and the use of pre-existing biometric models (either from voice or from face) is forbidden. The only way to identify a person is by finding their name in the audio (*e.g.* using automatic speech recognition) or visual (*e.g.* using optical character recognition) streams and associating them to the correct person - making the task completely unsupervised.

![Propagation](propagation.png)

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

#### Optional task

As we expect most submissions to internally rely on two-steps approaches (*i.e.* speaking-face diarization followed by propagation of detected names), an optional task is dedicated to the evaluation of underlying audio-visual diarization technologies.

In this optional task, participants are asked to provide a temporal segmentation of the whole test corpus containing every temporal fragment where at least one person is speaking and appearing at the same time. Moreover, each person should be uniquely identified by an anonymous label (*e.g.* `person1`, `person2`, ...)

```
video startTime endTime personLabel
```
  * `video`: unique identifier of the video
  * `startTime`: fragment start time
  * `endTime`: fragment end time
  * `personLabel`: unique identifier of the person

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

For instance, a researcher from the speech processing community could focus its research efforts on improving speaker diarization and automatic speech transcription, while still being able to rely on provided face detection and tracking results to participate to the task.

### Data

<!--
```
Describe the data set, including how the data will be collected an licensed.
```
-->

The REPERE dataset (distributed by ELDA) contains 137 hours of various TV shows (focusing on news, politics and people) from two French TV channels. It will be distributed freely by ELDA (Evaluation and Language resources Distribution Agency). Among those 137 hours, 50 are already manually annotated. Audio annotations are dense and provide speech transcripts and identity-labeled speech turns. Video annotations are sparse (one image every 10 seconds) and provide overlaid text transcripts and identity-labeled face segmentation. Both speech and overlaid text transcripts are tagged with named entities.

The AGORA dataset contains 43 hours of various TV shows (debates with a high variation in topics and invited speakers) from the Catalan public channel TV3. The transcription follows the general guideline generated within the TC-STAR project for European Parliament Plenary Sessions but was extended to include additional information as the language, background condition, silence/voice segmentation, speaker segmentation and acoustic events. The transcriptions have four layers. Transcriptions follow the TRS format produced by the Transcriber transcribing tool.

We are currently in discussion with INA to augment the REPERE dataset with 50+ hours of TV shows from additional TV channels, matching the broadcast dates of the original REPERE dataset.

We are also in discussion (through Turkish partners of the CAMOMILE project) with Digiturk to add TV shows in a third language (*i.e.* Turkish).

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

In order to encourage participants to provide correct proofs, the main evaluation metrics will incorporate their correctness in the following way (where the value of `A` is not yet decided):

```
#{relevant documents}  = A x #{relevant shots} + (1 - A) x #{correct proofs}
```

To reduce the cost of *a posteriori* annotation of the test set, we plan to ask participants to help annotating the corpus through the annotation webapp currently being developed and tested within the `CAMOMILE` project. We might also rely on peaks in `Google Trends` to only annotate a person for TV shows whose broadcast date matches peaks dates (i.e. only annotate people when they are actually buzzing).

An online adjudication interface will be opened after the first round of evaluations to solve remaining ambiguous cases.

#### Optional task

The optional task will be evaluated on a subset (10 hours) of the test set which is already densely annotated in terms of people speaking AND appearing at the same time. We will use the Diarization Error Rate (DER) classicaly used in the speech community.


### References and recommended reading

<!--
```
List 3-4 references related to the task that teams should have read before attempting the task.
```
-->

#### Paper by REPERE challenge 2013 organizers

G. Bernard, O. Galibert, J. Kahn  
[*The First Official REPERE Evaluation*](http://ceur-ws.org/Vol-1012/papers/paper-08.pdf)  
SLAM 2013, First Workshop on Speech, Language and Audio for Multimedia  

#### Paper by REPERE corpus creators

A. Giraudel, M. Carré, V. Mapelli, J. Kahn, O. Galibert, L. Quintard  
[*The REPERE Corpus: a Multimodal Corpus for Person Recognition*](http://www.lrec-conf.org/proceedings/lrec2012/pdf/707_Paper.pdf)  
LREC 2014, Eight International Conference on Language Resources and Evaluation  

#### Paper by REPERE challenge 2014 winning consortium

F. Bechet, M. Bendris, D. Charlet, G. Damnati, B. Favre, M. Rouvier, R. Auguste, B. Bigot, R. Dufour, C. Fredouille, G. Linarès, J. Martinet, G. Senay, P. Tirilly  
[*Multimodal Understanding for Person Recognition in Video Broadcasts*](http://pageperso.lif.univ-mrs.fr/~benoit.favre/papers/favre_interspeech2014b.pdf)  
InterSpeech 2014, Fifteenth Annual Conference of the International Speech Communication Association  

#### Papers by the organizers

H. Bredin, A. Laurent, A. Sarkar, V.-B. Le, S. Rosset, C. Barras  
[*Person Instance Graphs for Named Speaker Identification in TV Broadcast*](http://cs.uef.fi/odyssey2014/program/pdfs/27.pdf)  
Odyssey 2014, The Speaker and Language Recognition Workshop  

J. Poignant, L. Besacier, G. Quénot  
[*Unsupervised Speaker Identification in TV Broadcast Based on Written Names*](https://hal.archives-ouvertes.fr/hal-01060827/document)  
IEEE/ACM Transactions on Audio, Speech, and Language Processing  

### List of task organizers

  * Johann Poignant (postdoctoral researcher, LIMSI/CNRS)
  * Hervé Bredin (associate scientist, LIMSI/CNRS)
  * Claude Barras (associate professor, LIMSI/Université Paris-Sud)
  * TO BE CONFIRMED: Félicien Vallet (research engineer, INA)
  * TO BE CONFIRMED: Jean Carrive (head of research department, INA) 
  * TO BE CONFIRMED: Juliette Kahn (evaluation engineer, LNE)

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

Given raw TV broadcasts, each shot must be automatically tagged with the name of people both audible and visible.
The list of people is not known *a priori* and their names must be discovered in an unsupervised way from text overlay or speech transcripts.
The task will be evaluated on the extended REPERE corpus using standard information retrieval metrics based on *a posteriori* collaborative annotation of the corpus.

## Task organization team

```
Write a short paragraph describing the organizing team. 
Your team should be large enough to handle organizing the task. 
Teams should consists of members from multiple research sites and multiple projects. 
A mix of experienced and early-career researchers is recommended. 
Note that your task team ￼can add members after the proposal has been accepted.
```



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

- Keeping in mind that baseline monomodal modules will be provided (e.g. speaker diarization, face detection and tracking), what category of people should the task be evaluated on:  
 * audible people (I am only interested in audio processing)
 * visible people (I am only interested in video processing)
 * people either audible or visible
 * people both audible and visible (the task should be about the "multi" in "multimedia")

- Keeping in mind that your algorithm must not rely on prior biometric models, what should be the size of the development set for parameter tuning?
 * I don't need any development set.
 * 5 hours.
 * 10 hours.
 * 20 hours.

- Would you be interested in submitting contrastive runs using supervised person identification algorithms?
 * yes
 * no

- Keeping in mind that we will (very likely) not be able to annotate the whole test corpus, what do you think of only annotating videos with people that were actually buzzing (e.g. according to Google Trends) when the video was aired?
 * it is a good idea
 * I'd rather annotate less videos but more people
 * I'd rather annotate less people but more videos
 * I have a better idea: ...........................................

- Keeping in mind that we will (very likely) not be able to annotate the whole test corpus, what do you think of NOT annotating recurring TV anchors and journalists?
 * I agree: there is no need to annotate anchors and journalists
 * I disagree.

- How much time can you (or your team) devote to the a posteriori collaborative annotation?
 * None
 * 1 day
 * 2 days
 * a week
 * I annotate for fun - keep them coming!

- If any additional comments, questions or suggestions about this task occurred to you while you were answering the detailed questions, it would be helpful if you could enter them here:
